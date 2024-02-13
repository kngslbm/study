from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/member")
def member():

    name = "Han"
    profile = "Who i am"
    tag = "Leader"

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("member.html", data=context)


@app.route("/member2")
def member2():

    name = "Shin"
    profile = "Who i am"
    tag = "Member"

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("member2.html", data=context)


@app.route("/member3")
def member3():

    name = "Kim"
    profile = "Who i am"
    tag = "Member"

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("member3.html", data=context)


@app.route("/member4")
def member4():

    name = "Kang"
    profile = "Who i am"
    tag = "Member"

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("member4.html", data=context)


if __name__ == "__main__":
    app.run(debug=True)
