# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 20:55:22 2020

@author: user
"""
import smtplib

import os

import pandas as pd

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mail():
    
    #date = datetime.date.today().strftime("%B %d, %Y")
    path = 'Attendance'
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]
    filename = newest
    col_list = ["Date", "Time", "Mail"]
    df = pd.read_csv(filename, usecols=col_list)
    col_list = ["Name", "Date", "Time", "Mail"]
    df = pd.read_csv(filename, usecols=col_list)

    for name in df["Name"]:
        mm = df.loc[df['Name'] == name]['Mail'].values
        ti = df.loc[df['Name'] == name]['Time'].values
        da = df.loc[df['Name'] == name]['Date'].values
        nn = df.loc[df['Name'] == name]['Name'].values
        mm=str(mm)[2:-2]
        da=str(da)[2:-2]
        ti=str(ti)[2:-2]
        nn=str(nn)[2:-2]
        fromaddr = 'amachinelearner@gmail.com'
        toaddrs  = mm
        msg = 'Dear '+ nn+ ' your attendance has been marked!\n'+ 'Entry Date: '+da+' Entry Time: '+ti
        msg = MIMEMultipart()
        msg['Subject'] = 'Attendance Marked!'

        body = 'Dear '+ nn+ ' your attendance has been marked!\n'+ 'Entry Date: '+da+' Entry Time: '+ti
        msg.attach(MIMEText(body,'plain'))
        text = msg.as_string()
    
        username = 'mail'
        password = 'pass'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        
    print("Mails for Attendance Marked sent!")
        
    
 
