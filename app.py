from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form["name"]

        marks = [
            int(request.form["m1"]),
            int(request.form["m2"]),
            int(request.form["m3"]),
            int(request.form["m4"]),
            int(request.form["m5"])
        ]

        total = sum(marks)
        average = total / 5

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        if min(marks) >= 35:
            status = "PASS"
        else:
            status = "FAIL"

        result = {
            "name": name,
            "total": total,
            "average": round(average, 2),
            "grade": grade,
            "status": status
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)