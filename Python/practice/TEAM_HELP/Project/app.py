from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/leader")
def leader():

    name = "Han"
    profile = "Who i am"
    tag = "Leader"

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("leader.html", data=context)


@app.route("/member1")
def member1():

    name = "Shin"
    profile = "Who i am"
    tag = "Member"

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("member1.html", data=context)


@app.route("/member2")
def member2():

    name = "Kim"
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

    name = "Kang"
    profile = "Who i am"
    tag = "Member"

    context = {
        "name": name,
        "profile": profile,
        "tag": tag
    }
    return render_template("member3.html", data=context)


if __name__ == "__main__":
    app.run(debug=True)
