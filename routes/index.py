from helpers import (
    sqlite3,
    render_template,
    Blueprint,
)

indexBlueprint = Blueprint("index", __name__)



@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')
@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms_of_service.html')

@indexBlueprint.route("/")
def index():
    connection = sqlite3.connect("db/posts.db")
    cursor = connection.cursor()
    cursor.execute("select * from posts")
    posts = cursor.fetchall()
    categories = ["Home", "Depremler", "Category 2", "Category 3", "Category 4"]

    return render_template(
        "index.html",
        posts=posts, categories=categories
    )
