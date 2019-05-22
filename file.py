from flask import Flask,render_template,request
from werkzeug import secure_filename
app=Flask(__name__)
import pymongo

#connect with database
myclient =pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['local']
mycol = mydb['logined']


@app.route('/uploader',methods = ['POST'])
def upload():
	f=request.files['file']
	f.save(secure_filename(f.filename))
	return 'File is uploaded succesfully!!'

if __name__ =='__main__':
	app.run(debug=True)
	app.config['/home/nero/Projects/Flask-LoginApp/file.py']

