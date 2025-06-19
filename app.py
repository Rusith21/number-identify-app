from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename

# ----- Configuration -----
MODEL_PATH = "NSDataset_model.h5"
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
IMAGE_SIZE = (64, 64)
CLASS_NAMES = [
    "Number 0", "Number 1", "Number 2", "Number 3", "Number 4",
    "Number 5", "Number 6", "Number 7", "Number 8", "Number 9",
    "rectangle", "round", "triangle"
]

# ----- App Setup -----
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the model
model = load_model(MODEL_PATH)
print("✅ Model Loaded Successfully!")

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(img_path):
    img = image.load_img(img_path, target_size=IMAGE_SIZE)
    x = image.img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)[0]
    idx = np.argmax(preds)
    confidence = preds[idx]
    return CLASS_NAMES[idx], float(confidence)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return redirect(request.url)
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(save_path)
            label, conf = predict_image(save_path)
            return render_template(
                "index.html",
                filename=filename,
                label=label,
                confidence=f"{conf*100:.2f}%"
            )
    return render_template("index.html", filename=None)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return redirect(url_for("static", filename=f"uploads/{filename}"), code=301)

if __name__ == "__main__":
    app.run(debug=True)
