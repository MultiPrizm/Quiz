from flask import *
import Core.SqlInterface

App = Flask("main")
App.secret_key = "hb8yh&*&*HYY&*VFYbiuh879jk44543."

Session = {}

@App.route("/")
def main():
    
    return render_template("index.html")

@App.route("/log")
def log():
    print(session, request.remote_addr)

    if request.remote_addr in session:
        print(1)
        return session[request.remote_addr]
    
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
            print(2)
            print(request.remote_addr)
            session[request.remote_addr] = {
                "name": data["name"],
                "type": user_type
            }
            return"<h1>200</h1>"

    elif data["type"] == "reg":

        check = Core.SqlInterface.AddUser(data["name"], data["password"])
        if not check:
            return "<h1>402</h1>", 402
        return"<h1>200</h1>"
    

def RunApp():
    App.run(port=80)