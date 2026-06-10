from flask import Flask, render_template, request, redirect, session
import pickle
import random

app = Flask(__name__)
app.secret_key = "cybershield123"

model = pickle.load(open("model.pkl", "rb"))

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        otp = str(random.randint(100000, 999999))

        session["otp"] = otp

        print("Your OTP is:", otp)

        return redirect("/verify")

    return render_template("login.html")


@app.route("/verify", methods=["GET", "POST"])
def verify():

    if request.method == "POST":

        user_otp = request.form["otp"]

        if user_otp == session.get("otp"):
            return redirect("/")

        return "Invalid OTP"

    return render_template("otp.html")


@app.route("/", methods=["GET", "POST"])
def home():

    if "otp" not in session:
        return redirect("/login")

    result = ""

    if request.method == "POST":

        email = request.form["email"]

        prediction = model.predict([email])[0]

        if prediction == 1:
            result = "⚠️ Phishing Email Detected"
        else:
            result = "✅ Safe Email"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)