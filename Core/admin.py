from flask import *
import Core.SqlInterface

def admin():

    if request.remote_addr in session and session[request.remote_addr]["type"] == "admin":
        return render_template("admin.html")

    return "", 404

def setConf():    
    if request.remote_addr in session and session[request.remote_addr]["type"] == "admin":
        data = request.get_json()

        response = Core.SqlInterface.SetQuezConf(data)

        if response:
            return ""

    return "", 404

def activate(app):
    app.add_url_rule("/admin", "admin", admin)
    app.add_url_rule("/admin/setconf", "adminconf", setConf, methods=["POST"])