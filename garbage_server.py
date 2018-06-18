from flask import Flask, render_template
import datetime

app = Flask(__name__)


#th process of the top page
@app.route("/")
def put_out_num():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")

    templateData = {
        'time': timeString;
        'num_pet':,
        'num_bin':,
        'num_cam':
    }

    return render_template('main.html', **templateData)




if __name__=="__main__":
    app.run(host='0.0.0.0', port=80, debug=True)