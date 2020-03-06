from flask import Flask, render_template, request ,jsonify


from flask import Flask

import nltk

from nltk.stem import WordNetLemmatizer

import string

import random

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer  

from sklearn.metrics.pairwise import cosine_similarity


import io

import warnings

import re

warnings.filterwarnings('ignore')



app = Flask(__name__)


with open('newSEC.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()# converts to lowercase



sent_tokens = nltk.sent_tokenize(raw) # converts to list of sentences

word_tokens = nltk.word_tokenize(raw) # converts to list of words



lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]  #function etake call kore tokens pathano eta lemmatize kore dibe
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation) #jokhon token e banaisi tokhon punctuation gulao chole asche , segula bad disi ekhane
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


#keyword Matching

GREETING_INPUTS = ("hello","hi","greetings","sup","whats up","hey",)

GREETING_RESPONSES = ["hi","hey","*nods*","hi there","hello","I am glad you are talking to me"]

fallout = ["Sorry couldnt understand you!","I dont have access to your question yet!","Hey ! I have limitations!","Sorry buddy! type help for further info!"]


def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

#Praise response
        

PRAISE_INPUTS = ("good","nice","oh","great","amazing","praise","good job",)
PRAISE_RESPONSES = ["Thank you.","I will keep up the great work.","I appricitae it.","I will keep developing.","Thanks for collaborating"]

def praise(sentence):
    
    for word in sentence.split():
        if word.lower() in PRAISE_INPUTS:
            return random.choice(PRAISE_RESPONSES)

#generating response



def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    Tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(Tfidf[-1], Tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response= robo_response + random.choice(fallout)
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


def final_func(user_response):
    
    user_response = user_response.lower()
    pattern = "bye"
    if(re.search(pattern,user_response)==None):
        if(user_response=='thanks' or user_response=='thank you'):
            res = "SEC AdBOT : \n  You are welcome.. "
            return res
        else:
            if(greeting(user_response)!=None):
               res = "SEC AdBOT : \n  "+ greeting(user_response)+" "
               return res
            elif(praise(user_response)!=None):
               res= "SEC AdBOT : \n  "+ praise(user_response)+" "
               return res
            else:
                res = "SEC AdBOT : \n  "+ response(user_response)+" "
                sent_tokens.remove(user_response)
                return res
    else:
        res = "AdBoT : \n  Bye! take care.."
        return res

	
@app.route('/')
def home():
	return render_template("home.html") 

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return  str(final_func(userText))

@app.route("/wow")
def wow():
	return jsonify(final_func("SEC"))


if __name__ == '__main__':
    app.run(debug=True)
	
	