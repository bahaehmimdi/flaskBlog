from helpers import sqlite3, render_template, Blueprint, session, redirect

adminPanelBlueprint = Blueprint("adminPanel", __name__)


@adminPanelBlueprint.route("/admin")
def adminPanel():
    if "userName" in session:
            connection = sqlite3.connect("db/users.db")
            cursor = connection.cursor()
            cursor.execute(
                f'select role from users where userName = "{session["userName"]}"'
            )
            role = cursor.fetchone()[0]
            match role == "admin":
                case True:
                    return render_template("adminPanel.html")
                case False:
                    return redirect("/")
    else:
            return redirect("/")
