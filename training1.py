from __future__ import print_function
import argparse
import chainer
import chainer.functions as F
import chainer.links as L
import chainer.initializers as I
import Image
import numpy as np
from chainer import training
from chainer.training import extensions
from chainer.datasets import split_dataset_random

class MLP(chainer.Chain):
	insize = 256
	def __init__(self):
		w=I.HeNormal()
		super(MLP,self).__init__(

			conv1=L.Convolution2D(1, 96, 8, stride=4),
			bn1=L.BatchNormalization(96),
			conv2=L.Convolution2D(96,256,5,pad=2),
			bn2=L.BatchNormalization(256),
			conv3=L.Convolution2D(256,384,5,pad=1),
			conv4=L.Convolution2D(384,384,3,pad=1),
			conv5=L.Convolution2D(384,256,3,pad=1),
			fc6=L.Linear(None, 4096,initialW=w),
			fc7=L.Linear(None, 4096,initialW=w),
			fc8=L.Linear(None, 1000,initialW=w),
		)
		self.train = True
		
	def clear(self):
		self.loss = None
		self.accuracy = None
	
	def __call__(self,x):
		self.clear()
		h=F.relu(self.conv1(x))
		h=self.bn1(h)
		h=F.max_pooling_2d(h,2,stride=2)
		h=F.relu(self.conv2(h))
		h=self.bn2(h)
		h=F.max_pooling_2d(h,2,stride=2)
		h=F.relu(self.conv3(h))
		h=F.relu(self.conv4(h))
		h=F.relu(self.conv5(h))
		h=F.relu(self.fc6(h))
		h=F.dropout(h)
		h=F.relu(self.fc7(h))
		h=F.dropout(h)
		h=self.fc8(h)
		return h

def preprocessing(matrix,dirc_path,n,label):
	for i in range(n):
		openImg=dirc_path+str(i)+".png"
		img = Image.open(openImg)
		img = img.resize((256,256),Image.ANTIALIAS)
		imgArray = np.asarray(img).astype(np.float32)/255.
		imgA=imgArray[np.newaxis,:,:]
		data=(imgA,np.int32(label))
		matrix.append(data)

def main():
	parser=argparse.ArgumentParser(description='Chanier example: MNIST')
	parser.add_argument('--batchsize','-b',type=int,default=32,help='Number of sweeps over the dataset to train')
	parser.add_argument('--gpu','-g',type=int,default=-1,help='GPU ID (negative value indicates CPU)')
	parser.add_argument('--epoch','-e',type=int,default=40,help='Number of sweeps over the datasdt to train')
	parser.add_argument('--out','-o',default='result',help='Directory to output the result')
	parser.add_argument('--resume','-r',default='',help='Resume the training from snapshot')
	parser.add_argument('--unit','-u',type=int,default=1000,help='Number of units')
	args=parser.parse_args()
	print('GPU: {}'.format(args.gpu))
	print('# unit: {}'.format(args.unit))
	print('# Minibatch-size: {}'.format(args.batchsize))
	print('# epoch: {}'.format(args.epoch))
	print('')

	dataset_gomi=[]
	preprocessing(dataset_gomi,"sample_images_can1/pic",10,1)
	preprocessing(dataset_gomi,"sample_images_can2/pic",10,1)
	preprocessing(dataset_gomi,"sample_images_can3/pic",20,1)
	preprocessing(dataset_gomi,"sample_images_can4/pic",10,1)
	preprocessing(dataset_gomi,"sample_images_can5/pic",10,1)
	preprocessing(dataset_gomi,"sample_images_bin1/pic",10,2)
	preprocessing(dataset_gomi,"sample_images_bin2/pic",10,2)
	preprocessing(dataset_gomi,"sample_images_bin3/pic",20,2)
	preprocessing(dataset_gomi,"sample_images_pet1/pic",10,3)
	preprocessing(dataset_gomi,"sample_images_pet2/pic",10,3)
	preprocessing(dataset_gomi,"sample_images_pet3/pic",10,3)
	preprocessing(dataset_gomi,"sample_images_pet4/pic",10,3)

	train, test=split_dataset_random(dataset_gomi,120,seed=0)

	model=L.Classifier(MLP(),lossfun=F.softmax_cross_entropy)
	if args.gpu >= 0:
		chainer.cuda.get_device(args.gpu).user()
		model.to_gpu()
	optimizer = chainer.optimizers.Adam()
	optimizer.setup(model)
	train_iter = chainer.iterators.SerialIterator(train,args.batchsize)
	test_iter = chainer.iterators.SerialIterator(test,args.batchsize,repeat=False,shuffle=False)
	updater = training.StandardUpdater(train_iter,optimizer,device=args.gpu)
	trainer = training.Trainer(updater, (args.epoch, 'epoch'), out=args.out)
	trainer.extend(extensions.Evaluator(test_iter, model, device=args.gpu))
	trainer.extend(extensions.dump_graph('main/loss'))
	trainer.extend(extensions.snapshot(),trigger = (args.epoch,'epoch'))
	#trainer.extend(extensions.PlotReport(['main/loss','validation/main/accuracy'],'epoch',file_name='loss.png'))
	trainer.extend( extensions.PlotReport(['main/accuracy', 'validation/main/accuracy'], 'epoch', file_name='accuracy.png'))
	trainer.extend(extensions.PrintReport(['epoch','main/loss','validation/main/loss','main/accuracy','validation/main/accuracy','elapsed_time']))
	trainer.extend(extensions.ProgressBar())
	trainer.extend(extensions.LogReport())

	if args.resume:
		chainer.serializers.load_npz(args.resume,trainer)

	trainer.run()
	model.to_cpu()

	modelname = args.out + "/MLP.model"
	print('same the trained model: {}'.format(modelname))
	chainer.serializers.save_npz("model.npz",model)

if __name__=='__main__':
	main()
