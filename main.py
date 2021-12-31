from flask import Flask, render_template, request, url_for, redirect, flash, session
import bcrypt, random

app =Flask(__name__)

app.secret_key = ''.join([random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' + 
                                         'abcdefghijklmnopqrstuvxyz' +
                                         '0123456789'))
                          for i in range(20)])

@app.route("/home/")
def home():
    ## if session not present then
    return render_template("home.html")
    ## else redirect to start.html and resume virtual tour

@app.route("/start/")
def start(progress_index):
    if progress_index:
        #load kitchens within an array and pass it to template
        progress_index+=1
        return render_template("start.html", prog=progress_index, kitchen=kitchens)
    ## else if no progess index redirect to index
    
@app.route("/end/")
def end():
    ##if visit.ended():
        # return render_tamplate("end.html")
    ##else find progress index and redirect to home if not initialised else resume visit.

if __name__=="__main__":
    app.run(port=443)