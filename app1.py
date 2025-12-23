from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# HALAMAN 1 (FORM)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form.get("nama")
        return redirect(url_for("hasil", nama=nama))
    return render_template("index.html")

# HALAMAN 2 (HASIL)
@app.route("/hasil")
def hasil():
    nama = request.args.get("nama")
    return render_template("hasil.html", nama=nama)

if __name__ == "__main__":
    app.run(debug=True)