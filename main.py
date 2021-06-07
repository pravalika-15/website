from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()


@app.route('/')
def hello():
    return render_template("index.html", all_posts=posts)


@app.route("/post.html/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact',  methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_mail(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


@app.route('/index')
def index():
    return render_template('index.html', all_posts=posts)


def send_mail(name, email, phone, message):
    email_msg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP('pravalikaelsa123@gmail.com', 587) as connection:
        connection.starttls()
        connection.login('pravalikaelsa123@gmail.com', 'pahryj-8zunsa-Mujbed')
        connection.sendmail(from_addr='pravalikaelsa123@gmail.com', to_addrs='pravalikaelsa123@gmail.com', msg=email_msg)


if __name__ == "__main__":
    app.run(debug=True)