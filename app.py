from flask import Flask, jsonify, request, send_from_directory
import joblib
import os
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'decision_tree_regressor.pkl')
FEATURE_ORDER = ['Fresh', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']

app = Flask(__name__, static_folder='.', static_url_path='')
model = joblib.load(MODEL_PATH)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(silent=True)
    if not data:
        return jsonify(error='Invalid JSON payload'), 400

    try:
        inputs = [float(data[name]) for name in FEATURE_ORDER]
    except KeyError:
        return jsonify(error=f'Missing one or more inputs: {FEATURE_ORDER}'), 400
    except ValueError:
        return jsonify(error='All input values must be numeric'), 400

    prediction = model.predict([inputs])[0]
    return jsonify(prediction=float(prediction))

@app.route('/predict_csv', methods=['POST'])
def predict_csv():
    if 'file' not in request.files:
        return jsonify(error='No file uploaded'), 400
    f = request.files['file']
    try:
        df = pd.read_csv(f)
    except Exception as e:
        return jsonify(error='Failed to read CSV: ' + str(e)), 400
    missing = [c for c in FEATURE_ORDER if c not in df.columns]
    if missing:
        return jsonify(error='Missing required columns: ' + ','.join(missing)), 400
    X = df[FEATURE_ORDER].astype(float)
    preds = model.predict(X).tolist()
    # attach predictions to rows for frontend convenience
    rows = df[FEATURE_ORDER].fillna('').values.tolist()
    # return limited preview
    return jsonify(predictions=[float(p) for p in preds], columns=FEATURE_ORDER, rows=[list(r)+[float(preds[i])] for i,r in enumerate(rows)])

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
