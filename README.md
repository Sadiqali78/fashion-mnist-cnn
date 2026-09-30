# 👕 Fashion MNIST Classification App

Welcome to the **Fashion MNIST Classification App**! This is a lightweight web application built with **Flask** that uses a trained Convolutional Neural Network (CNN) to intelligently identify and classify images of clothing items.

---

## 🚀 Quick Start

Follow these simple steps to get the project up and running on your local machine.

### 1️⃣ Prerequisites
Make sure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)

### 2️⃣ Installation

First, open your terminal or command prompt and navigate to the project folder:
```bash
cd "d:/Hope AI/Learn/Deep Learning/CNN/fashion"
```

Next, install all the necessary dependencies. We use a specific version of NumPy to ensure everything runs smoothly:
```bash
pip install -r requirements.txt
```
> 💡 *Note: `numpy` is capped at `<1.28.0` in the requirements to prevent compatibility issues with TensorFlow packages.*

### 3️⃣ How to Run

Once everything is installed, starting the app is incredibly easy. Run this command in your terminal:

```bash
python app.py
```

### 4️⃣ Use the App

1. Wait for the terminal to display `* Running on http://127.0.0.1:5000`
2. Open your favorite web browser and navigate to: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**
3. Upload an image of a clothing item (e.g., *T-shirt, Trouser, Sneaker, Bag, Ankle Boot*) and let the AI predict what it is!

---

## 📁 Project Structure

Here's a quick overview of what's inside this repository:

| File / Folder | Description |
| :--- | :--- |
| 🖥️ **`app.py`** | The main Flask web server script handling the interface and AI predictions. |
| 🧠 **`fashion_mnist_cnn.keras`** | The pre-trained TensorFlow/Keras neural network model. |
| 🎨 **`templates/`** | Contains the frontend HTML interface (`index.html`). |
| 📦 **`requirements.txt`** | The list of Python dependencies required to run the app. |
| 📓 **`Fashion_MNIST_CNN_Workshop.ipynb`**| The Jupyter Notebook where the CNN model was originally trained. |

---
*Built with ❤️ using Flask, TensorFlow, and Python.*
