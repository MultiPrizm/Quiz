from flask import *
import Core.admin, Core.login, Core.quizService

app = Flask("main")
app.secret_key = "hb8yh&*&*HYY&*VFYbiuh879jk44543."

@app.route("/")
def main():
    
    return render_template("index.html")


Core.admin.activate(app)
Core.login.activate(app)
Core.quizService.activate(app)
