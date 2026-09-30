import os
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

app = Flask(__name__)

# Load the trained model
MODEL_PATH = 'fashion_mnist_cnn.keras'
model = tf.keras.models.load_model(MODEL_PATH)

# Class names as per the notebook (corrected typo)
CLASS_NAMES = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']

def process_image(image):
    # Convert to grayscale
    image = image.convert('L')
    # Resize to 28x28
    image = image.resize((28, 28))
    # Invert colors if necessary? Usually Fashion MNIST has dark background and light clothes.
    # We can assume users upload images with white background, so we might need to invert it.
    # Let's invert it since standard drawings are dark on white, while MNIST is light on dark.
    # But real photos might be different. Let's just do a basic ImageOps.invert if most pixels are light, or just keep it simple.
    
    img_array = np.array(image)
    
    # Invert image if background is light (assuming corners are background)
    if np.mean(img_array[0:5, 0:5]) > 127:
        image = ImageOps.invert(image)
        img_array = np.array(image)
        
    # Normalize
    img_array = img_array / 255.0
    # Reshape to (1, 28, 28, 1) for the CNN
    img_array = img_array.reshape(1, 28, 28, 1)
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
        
    if file:
        try:
            image = Image.open(file.stream)
            processed_image = process_image(image)
            prediction = model.predict(processed_image)
            
            class_idx = np.argmax(prediction[0])
            class_name = CLASS_NAMES[class_idx]
            confidence = float(prediction[0][class_idx])
            
            return jsonify({
                'class': class_name,
                'confidence': confidence,
                'all_probs': prediction[0].tolist()
            })
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
