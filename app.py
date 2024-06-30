from flask import Flask,render_template, abort

app = Flask("__name__")

# 作品集的資訊
projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://udemy.com",
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
    },
]
# 建立 slug dict，把slug 特別挑出來
slug_to_project = {project["slug"]: project for project in projects}
print(slug_to_project)
@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    # 如果輸入的 slug 不存在 404
    if slug not in slug_to_project:
        abort(404)
    
    return render_template(f"project_{slug}.html",project=slug_to_project[slug])
    

# 如果出現未定義的url
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404