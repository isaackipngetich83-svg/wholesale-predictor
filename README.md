# Wholesale Predictor — Professional Guide

This repository contains a minimal, professional Flask front-end for running predictions with your trained `decision_tree_regressor.pkl` model.

Quick files:

- `app.py` — backend exposing `/` and `/predict` endpoints.
- `index.html`, `styles.css`, `script.js` — lightweight, responsive UI for single-row predictions.
- `decision_tree_regressor.pkl` — your serialized scikit-learn model.

Local development

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

2. Run the app (development):

```bash
python app.py
# then open http://127.0.0.1:5000
```

Production notes

- On Windows, use `waitress` to serve the app behind a real WSGI server:

```bash
waitress-serve --port=5000 app:app
```

- On Linux, `gunicorn` is a common choice (install separately).

Security & compatibility

- The model was saved with a different scikit-learn version; the app will warn if versions differ. Re-train or re-export the model with the target scikit-learn when possible.

Customization

- Replace text, styles, and logo in `index.html` and `styles.css` to match branding.
- Keep `FEATURE_ORDER` in `app.py` aligned with your model's expected input columns.

Support

If you want, I can produce a production-ready packaging (Dockerfile), CI steps, and a hosted demo deployment guide.
