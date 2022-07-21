from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:post123@localhost/CC_data_from_Webapp'
else:
    app.debug = False
    # establishing connection
    #app.config['SECRET_KEY'] = 'secret'
    #app.config['SQLALCHEMY_DATABASE_URI']='postgresql://vpeqshfclyduif:3a1c6f963c3b4390196e86074be4da2bc0f9d97084a8884c6db36dbe91b15fd8@ec2-52-70-205-234.compute-1.amazonaws.com:5432/d50n95dk857dq9'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qoqyavbvyfnayk:ab03c518f30737074be3da81c926175bbb82f7022bf6b62eefd49f6533bbf27d@ec2-34-235-198-25.compute-1.amazonaws.com:5432/d5a612laoule09'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class CCdata(db.Model):

    def __init__(self, date, ccStartTime, line, loaderName, shiftChangeTime, rpm, lineSpeed, regrindUsed, shadeIssue, dosingIssue, ccFrom, ccTo, ccRej):
        self.date = date
        self.ccStartTime = ccStartTime
        self.line = line
        self.loaderName = loaderName
        self.shiftChangeTime = shiftChangeTime
        self.rpm = rpm
        self.lineSpeed = lineSpeed
        self.regrindUsed = regrindUsed
        self.shadeIssue = shadeIssue
        self.dosingIssue = dosingIssue
        self.ccFrom = ccFrom
        self.ccTo = ccTo
        self.ccRej = ccRej

    __tablename__ ='CC_data_from_Webapp'
    srNo = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    ccStartTime = db.Column(db.Time)
    line = db.Column(db.String(10))
    loaderName = db.Column(db.String(10))
    shiftChangeTime = db.Column(db.String(5))
    rpm = db.Column(db.Float)
    lineSpeed = db.Column(db.Float)
    regrindUsed = db.Column(db.String(5))
    shadeIssue = db.Column(db.String(5))
    dosingIssue = db.Column(db.String(5))
    ccFrom = db.Column(db.String(10))
    ccTo = db.Column(db.String(10))
    ccRej = db.Column(db.Integer)




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        date = request.form['date']
        ccStartTime = request.form['ccStartTime']
        line = request.form['line']
        loaderName = request.form['loaderName']
        shiftChangeTime = request.form['shiftChangeTime']
        rpm = request.form['rpm']
        lineSpeed = request.form['lineSpeed']
        regrindUsed = request.form['regrindUsed']
        shadeIssue = request.form['shadeIssue']
        dosingIssue = request.form['dosingIssue']
        ccFrom = request.form['ccFrom']
        ccTo = request.form['ccTo']
        ccRej = request.form['ccRej']
        colorChange = CCdata(date, ccStartTime, line, loaderName, shiftChangeTime, rpm, lineSpeed, regrindUsed, shadeIssue, dosingIssue, ccFrom, ccTo, ccRej)
        db.session.add(colorChange)
        db.session.commit()
        return render_template('success.html', c1=ccFrom, c2=ccTo, cc=ccRej)


if __name__ == "__main__":
    app.run()