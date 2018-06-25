import training1
import chainer.serializers
import chainer.functions as F
import chainer.links as L
import argparse
import numpy as np
from PIL import Image

def prd(image):
	parser = argparse.ArgumentParser(description='TEST_NN')
	parser.add_argument('--inputimage', '-i', action='store', default=100,help='image file name')
	args = parser.parse_args()
	filename = args.inputimage
	#print("{}".format(filename) )
	model = L.Classifier(training1.MLP())
	chainer.serializers.load_npz("./model1.npz", model)
	#image = Image.open("./sample_images_bin1/pic0.png")
	img = image.resize((256,256),Image.ANTIALIAS)
	imgArray = np.asarray(img).astype(np.float32)/255.
	imgA=imgArray[np.newaxis,:,:]
	
	a=np.array([imgA])
	y = model.predictor(a)
	prediction = F.softmax(y)
	m = np.argmax(prediction.data)
	#print("result={}".format(m) )
	return m

if __name__ == '__main__':
	main()
\