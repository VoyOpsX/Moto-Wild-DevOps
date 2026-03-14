#version 1

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
MOTO_FOLDER = os.path.join(UPLOAD_FOLDER, "motoglimpse")
WILD_FOLDER = os.path.join(UPLOAD_FOLDER, "wildography")

os.makedirs(MOTO_FOLDER, exist_ok=True)
os.makedirs(WILD_FOLDER, exist_ok=True)

app.config['MOTO_FOLDER'] = MOTO_FOLDER
app.config['WILD_FOLDER'] = WILD_FOLDER


@app.route("/")
def home():
    moto_images = os.listdir(app.config['MOTO_FOLDER'])
    wild_images = os.listdir(app.config['WILD_FOLDER'])

    return render_template(
        "index.html",
        moto_images=moto_images,
        wild_images=wild_images
    )


@app.route("/upload/moto", methods=["POST"])
def upload_moto():
    file = request.files["file"]
    if file:
        file.save(os.path.join(app.config['MOTO_FOLDER'], file.filename))
    return redirect(url_for("home"))


@app.route("/upload/wild", methods=["POST"])
def upload_wild():
    file = request.files["file"]
    if file:
        file.save(os.path.join(app.config['WILD_FOLDER'], file.filename))
    return redirect(url_for("home"))


@app.route("/uploads/<category>/<filename>")
def uploaded_file(category, filename):
    return send_from_directory(f"uploads/{category}", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
