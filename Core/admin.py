from flask import *
import Core.SqlInterface

def admin():

    return render_template("admin.html")


def setConf():    
    if request.remote_addr in session:
        data = request.get_json()

        response = Core.SqlInterface.SetQuezConf(data, session[request.remote_addr]["name"])

        if response:
            return ""

    return "", 404

def AdminQuiz():

    if request.remote_addr in session:
    
        return {"response":Core.SqlInterface.GetUserQuiz(session[request.remote_addr]["name"])}
    
    return "", 401

def GetCode(quiz):

    if request.remote_addr in session:
    
        return {"response":Core.SqlInterface.GetCode(session[request.remote_addr]["name"], quiz)}
    
    return "", 401

def activate(app):
    app.add_url_rule("/admin.html", "admin", admin)
    app.add_url_rule("/admin/setconf", "adminconf", setConf, methods=["POST"])
    app.add_url_rule("/admin/quizlist", "getAdminQuiz", AdminQuiz)
    app.add_url_rule("/admin/quizcode/<quiz>", "getcode", GetCode)
