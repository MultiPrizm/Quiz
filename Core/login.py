from flask import *
import Core.SqlInterface

def login_html():
    
    return render_template("login.html")

def log():

    if request.remote_addr in session:
        return session[request.remote_addr]
    
    return "", 401

def delog():

    if request.remote_addr in session:
        session.pop(request.remote_addr)
        return "200"
    
    return "", 401

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

def activate(app):
    app.add_url_rule("/login.html", "loghtml", login_html)
    app.add_url_rule("/log", "log", log)
    app.add_url_rule("/delog", "delog", delog)
    app.add_url_rule("/log/login", "checklog", login, methods=["POST"])

