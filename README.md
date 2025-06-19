# Number & Shape Identifier (Flask)

A simple Flask web app that loads a Keras `.h5` model and lets you upload an image to predict digits (0–9) and shapes (rectangle, round, triangle).

---

## 📂 Project Structure

```
flask_app/
├── app.py
├── NSDataset_model.h5      # your trained Keras model
├── uploads/                # user-uploaded images (auto-created)
├── templates/
│   └── index.html
└── screenshots/
    ├── upload_form.png
    └── result_screen.png
```

---

## 📋 Requirements

- Python 3.7+
- `flask`
- `tensorflow`
- `pillow`
- `werkzeug`

Install with:

```bash
pip install flask tensorflow pillow werkzeug
```

---

## 🚀 Quick Start

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Rusith21/number-identify-app.git
   cd number-identify-app
   ```

2. **Add your model**  
   Copy your `NSDataset_model.h5` into the project root:
   ```bash
   cp /path/to/NSDataset_model.h5 .
   ```

3. **Run the app**  
   ```bash
   python app.py
   ```
   Open your browser at [http://localhost:5000](http://localhost:5000).

---

## 🖼️ Screenshots

1. **Upload Form**  
   ![Upload Form](/Users/rusith/Desktop/ml/Screenshot 2025-06-19 at 11.18.58 AM.png)

2. **Prediction Result**  
   ![Result Screen](/Users/rusith/Desktop/ml/Screenshot 2025-06-19 at 11.39.19 AM.png)

---

## 🔧 How It Works

- **`app.py`**  
  - Loads your Keras model on startup.  
  - Serves an HTML form (`index.html`) to upload images.  
  - Saves uploaded images to `uploads/`.  
  - Preprocesses each image to `(64×64)` and normalizes it.  
  - Runs `model.predict()` and shows the predicted class with confidence.

- **`templates/index.html`**  
  - A simple upload form + result display.

---

## ⚙️ Configuration

- **Model filename**: If your model is named differently, edit the top of `app.py`:
  ```python
  MODEL_PATH = "your_model_name.h5"
  ```
- **Allowed extensions**: Edit `ALLOWED_EXTENSIONS` in `app.py` if you need more formats.

---

## 📝 License

This project is licensed under the MIT License. Feel free to use and modify!
