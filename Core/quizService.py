from flask import *
import Core.SqlInterface

def quiz():
    
    return render_template("quiz.html")

def Quiz():
    
    return {"response":Core.SqlInterface.GetQuiz()}

def Question(quiz):
    response = Core.SqlInterface.GetQuestion(quiz)

    if response:    
        return {"response": response}
    else:
        return "", 404

def CodeQuestion(quiz):
    response = Core.SqlInterface.GetQuestion(quiz)

    if response:    
        return {"response": response}
    else:
        return "", 404

def activate(app):
    app.add_url_rule("/quiz.html", "quizhtml", quiz)
    #app.add_url_rule("/get/quizlist", "getQuiz", Quiz)
    app.add_url_rule("/get/question/<quiz>", "getQuestion", Question)