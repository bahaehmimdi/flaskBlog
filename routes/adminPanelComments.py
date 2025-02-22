from helpers import (
    sqlite3,
    render_template,
    Blueprint,
    session,
    redirect,
    request,
)
from delete import deleteComment

adminPanelCommentsBlueprint = Blueprint("adminPanelComments", __name__)


@adminPanelCommentsBlueprint.route("/admin/comments", methods=["GET", "POST"])
@adminPanelCommentsBlueprint.route("/adminpanel/comments", methods=["GET", "POST"])
def adminPanelComments():
    if "userName" in session:
            connection = sqlite3.connect("db/users.db")
            cursor = connection.cursor()
            cursor.execute(
                f'select role from users where userName = "{session["userName"]}"'
            )
            role = cursor.fetchone()[0]
            if request.method == "POST":
                if "commentDeleteButton" in request.form:
                    deleteComment(request.form["commentID"])
                    return redirect(f"/admin/comments")
            if role == "admin":
                    connection = sqlite3.connect("db/comments.db")
                    cursor = connection.cursor()
                    cursor.execute("select * from comments")
                    comments = cursor.fetchall()
                    return render_template("adminPanelComments.html", comments=comments)
            else: 
                    return redirect("/")
    else: 
            return redirect("/")
