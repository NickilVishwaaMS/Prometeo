from flask import Flask, render_template, request, jsonify
import inference

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' in request.files:
        image = request.files['image']
        prediction = inference.predict(image)
        return jsonify({'prediction': str(prediction)})
    return jsonify({'error': 'No image provided'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
