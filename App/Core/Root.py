from flask import *
import Core.SqlInterface

App = Flask("main")
App.secret_key = "hb8yh&*&*HYY&*VFYbiuh879jk44543."

Session = {}

def main():
    
    return render_template("index.html")

App.add_url_rule("/", 'main', main)

@App.route("/quiz")
def quiz():
    
    return render_template("quiz.html")

@App.route("/log")
def log():

    if request.remote_addr in session:
        return session[request.remote_addr]
    
    return "", 401

@App.route("/admin")
def admin():

    if request.remote_addr in session and session[request.remote_addr]["type"] == "admin":
        return render_template("admin.html")

    return "", 404

@App.route("/delog")
def delog():

    if request.remote_addr in session:
        session.pop(request.remote_addr)
        return "200"
    
    return "", 401

@App.route("/login.html")
def login_html():
    
    return render_template("login.html")

@App.route("/log/login", methods=['POST'])
def login():

    data = request.get_json()

    if data["type"] == "log":
        flag1, flag2, user_type = Core.SqlInterface.CheckPassword(data["name"], data["password"])

        if not flag1:
            return "<h1>402</h1>", 402
        elif not flag2:
            return "<h1>418</h1>", 418
        else:
            session[request.remote_addr] = {
                "name": data["name"],
                "type": user_type
            }
            return redirect(url_for("main"))

    elif data["type"] == "reg":

        check = Core.SqlInterface.AddUser(data["name"], data["password"])
        if not check:
            return "<h1>402</h1>", 418
        return"<h1>200</h1>"
    
@App.route("/get/quizlist")
def Quiz():
    
    return {"response":Core.SqlInterface.GetQuiz()}

@App.route("/get/question/<quez>")
def Question(quez):
    response = Core.SqlInterface.GetQuestion(quez)

    if response:    
        return {"response": response}
    else:
        return "", 404

@App.route("/admin/setconf", methods=['POST'])
def setConf():    
    if request.remote_addr in session and session[request.remote_addr]["type"] == "admin":
        data = request.get_json()

        response = Core.SqlInterface.SetQuezConf(data)

        if response:
            return ""

    return "", 404
    
def RunApp():
    App.run(port=80)
