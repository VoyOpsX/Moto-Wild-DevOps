from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
MOTO_FOLDER = os.path.join(UPLOAD_FOLDER, "motoglimpse")
WILD_FOLDER = os.path.join(UPLOAD_FOLDER, "wildography")
DATA_FILE = "data.json"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "mp4", "mov", "webm"}

os.makedirs(MOTO_FOLDER, exist_ok=True)
os.makedirs(WILD_FOLDER, exist_ok=True)

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"motoglimpse": [], "wildography": []}, f)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# 🏠 HOME PAGE
@app.route("/")
def home():
    return render_template("home.html")


# 📂 GALLERY PAGE
@app.route("/gallery/<category>")
def gallery(category):
    if category not in ["motoglimpse", "wildography"]:
        return redirect(url_for("home"))

    data = load_data()
    return render_template("gallery.html", category=category, items=data[category])


# 📤 UPLOAD
@app.route("/upload/<category>", methods=["POST"])
def upload(category):
    if category not in ["motoglimpse", "wildography"]:
        return redirect(url_for("home"))

    file = request.files["file"]
    title = request.form.get("title")
    description = request.form.get("description")

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        folder = MOTO_FOLDER if category == "motoglimpse" else WILD_FOLDER
        filepath = os.path.join(folder, filename)
        file.save(filepath)

        data = load_data()
        data[category].append({
            "filename": filename,
            "title": title,
            "description": description,
            "type": filename.rsplit(".", 1)[1].lower()
        })
        save_data(data)

    return redirect(url_for("gallery", category=category))


# 🗑 DELETE
@app.route("/delete/<category>/<filename>")
def delete_file(category, filename):
    folder = MOTO_FOLDER if category == "motoglimpse" else WILD_FOLDER
    filepath = os.path.join(folder, filename)

    if os.path.exists(filepath):
        os.remove(filepath)

    data = load_data()
    data[category] = [item for item in data[category] if item["filename"] != filename]
    save_data(data)

    return redirect(url_for("gallery", category=category))


# ✏ EDIT
@app.route("/edit/<category>/<filename>", methods=["POST"])
def edit_file(category, filename):
    new_title = request.form.get("title")
    new_description = request.form.get("description")

    data = load_data()

    for item in data[category]:
        if item["filename"] == filename:
            item["title"] = new_title
            item["description"] = new_description
            break

    save_data(data)
    return redirect(url_for("gallery", category=category))


@app.route("/uploads/<category>/<filename>")
def uploaded_file(category, filename):
    return send_from_directory(f"uploads/{category}", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
