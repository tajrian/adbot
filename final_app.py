from flask import Flask, render_template, request ,jsonify

import re 
import random
import sqlite3
import string


app = Flask(__name__)



corpus = {"sec":["sec","public","sust","about"],
     "seats": ["seats","accepted","how many students","available"],
     "locate" : ["location","located","where"],
     "campus" : ["building"],
     "study_abroad" : ["study abroad"],
     "alumnai" : ["alumnai","achievements"],
     "labs" : ["equipments","facilities","labs"],
     "library" : ["library","books"],
     "interent" : ["wifi","net","internet","broadband"],
     "academic" : ["courses","credit"],
     "tution_fee" : ["tution","expense"],
     "second_timer": ["2nd time","2nd","second time","second"],
     "ap_qualification" : ["qualification","minimum gpa","gpa minimum"],
     "ad_date" : ["admission test","date","day"],
     "eligiable" : ["diploma","eligible","eligibility"],
     "admission_fee" : ["admission fee","apply fee","application fee"],
     "quota" : ["quota","tribal","freedom fighter"],
     "admission_test" : ["exam","format"],
     "gpa" : ["gpa","ssc","hsc","grade"],
     "marking" : ["partial","negative","marking"],
     "email_contact" : ["email","contact","authorities"],
     "phone" : ["phone","call"],
     "path" : ["reach","way","path","minimum cost","get"],
     "session" : ["session","jot"],
     "website" : ["website"],
     "dept" : ["how many dept","departments","department"],
     "cse_dept" : ["cse","computer science"],
     "eee_dept" : ["eee","electrical"],
     "ce_dept" : ["ce","civil"],
     "facebook" : ["group","page","facebook","help","aid"],
     "scholarship" : ["scholarship"],
     "dorm" : ["hall","hostel","dormitories","residential","dorm"],
     "apply" : ["circular","published","apply","procedure"],
     }

def find_reply(msg):
    table=None
    for key,values in corpus.items():
        for value in values:
            if(re.search(value,msg)!=None):
                table=key
                break
            
    if(table==None):
        return None 
    else:
        conn = sqlite3.connect('info.db')
        c  = conn.cursor()
        c.execute("SELECT * FROM {0};".format(table))
        z = c.fetchall()
        reply = random.choice(z)
        conn.commit()
        conn.close()
        return reply
    
admiration = ["cool","wow","nice","good","glad","joss","great"]
admiration_reply = ["Glad to know! ","I will try my best for your service! ","so nice of you! ","Ask me anything you need!","I appriciate it","I will keep developing!"]
fallout = ["Sorry couldnt understand you!","I dont have access to your question yet!","Hey ! I have limitations!","Sorry buddy! type help for further info!"]
greet = ["hello","hi","greetings","sup","whats up","hey"]
greet_back = ["hi!","hey!","*nods*","hi there!","hello!","I am glad you are talking to me!"]

def if_any(msg,bags_of_word = []):
    for word in bags_of_word:
        if(re.search(word,msg)!=None):
            return True
    return False




def final_func(msg):
     msg= msg.lower()
     pattern1 = "bye"
     pattern2 = "thank" 
     
     
     if(re.search(pattern1,msg)!=None):
     	re_val = "SEC AdBoT : Bye! Take care !"
     	return re_val
     elif(find_reply(msg)!=None):
        re_val = "SEC AdBoT : "+ find_reply(msg)[0]
        return re_val
     elif(re.search(pattern2,msg)!=None):
        re_val = "SEC AdBoT : Welcome! :)"
        return re_val
     elif(if_any(msg,greet)==True):
        re_val = "SEC AdBoT : "+ random.choice(greet_back)
        return re_val
     elif(if_any(msg,admiration)==True):
        re_val = "SEC AdBoT : "+ random.choice(admiration_reply)
        return re_val
     else:
        re_val = "SEC AdBoT : "+ random.choice(fallout)
        return re_val

        
@app.route('/')
def home():
   return render_template("home.html")

@app.route("/get")
def get_msg():
    user_text = request.args.get('msg')
    return str(final_func(user_text))

#test route
@app.route("/wow")
def wow():
	return jsonify(final_func("SEC"))


if __name__ == '__main__':
    app.run(debug=True)
