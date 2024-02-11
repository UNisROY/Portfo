from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subjects = data["subjects"]
        message = data["message"]
        file = database.write(f"\n{email},{subjects},{message}")


def write_to_csv(data):
    with open("datas.csv", mode="a") as database1:
        email = data["email"]
        subjects = data["subjects"]
        message = data["message"]
        csv_writer = csv.writer(
            database1, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subjects, message])


@app.route("/Submit_Form", methods=["POST", "GET"])
def Submit_Form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/ThankYou.html")
    else:
        return "SomethinG WronG"

    # return render_template('login.html',error=error)


# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     return render_template("index.html", name=username, pd=post_id)
