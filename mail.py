# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 08:21:43 2016

@author: david
"""
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '273495636@qq.com'
app.config['MAIL_PASSWORD'] = 'dnzzsurtydxzbgib'

mail = Mail(app)

msg = Message('邮件主题', sender='273495636@qq.com', recipients=['273495636@qq.com'])
msg.body = '邮件内容'
msg.html = "<h1>邮件的html模板<h1> body"

with app.app_context():
    mail.send(msg)





