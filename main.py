from flask import Flask, render_template, request, url_for, redirect, flash, session
import bcrypt, random

from handler import *


app =Flask(__name__)

app.secret_key = ''.join([random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' + 
                                         'abcdefghijklmnopqrstuvxyz' +
                                         '0123456789'))
                          for i in range(20)])


@app.route("/")
def home():
    session['progress'] = 0
    return render_template("home.html")

@app.route("/virtual_tour/<string:offset>")
def virtual_tour(offset):

    if 'progress' in session and session["progress"] < len(kitchen):
        prog=session['progress']
        if (offset=="next"):
            session['progress'] += 1
        elif offset=="previous":
            session['progress'] += -1
        else:
            return render_template("home.html")

        imagespath=f'static/kitchen/{kitchen[prog]}/image'
        front=''
        food=''
        images, front, food=retrieve_image(imagespath)
        

        try:
            narrative=f'static/kitchen/{kitchen[prog]}/narrative.docx'
            recipe=f'static/kitchen/{kitchen[prog]}/recipe.docx'
            data={"title":f'kitchen @ {kitchen[prog]}' , "article": retrieve_text(narrative) , "recipe": retrieve_text(recipe), 'front':front, 'food': food}
            
            return render_template("virtual_tour.html", data=data, images=images)
        except:
            ingredients=f'static/kitchen/{kitchen[prog]}/ingredients.docx'
            instructions=f'static/kitchen/{kitchen[prog]}/instructions.docx'
            preamble=f'static/kitchen/{kitchen[prog]}/preamble.docx'
            data={"title":f'kitchen @ {kitchen[prog]}' , "article": retrieve_text(narrative) , "ingredients": retrieve_text2(ingredients), "instructions":retrieve_text(instructions),
            "preamble":retrieve_text(preamble), 'front': front, 'food': food}
            
            return render_template("virtual_tour.html", data=data, images=images)
       
    else:
        return redirect(url_for('end'))
    return render_template("home.html")
    
@app.route("/end/")
def end():
    session['progress']=0
    return render_template('end.html')

if __name__=="__main__":
    kitchen=['sdivisionst','redhawk','alvarado', 'deerhaven', 'oldmilton','russellcreek', 'wallowa']
    app.run(port=8080, debug=True)
