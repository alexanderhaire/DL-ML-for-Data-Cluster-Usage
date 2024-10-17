# File: service_a.py
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import threading
import time

app = Flask(__name__)

lstm_model = None  # Global variable to hold the LSTM model
input_shape = (6, 1)  # Input shape for the LSTM model

# LSTM model creation function
def create_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(100, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(25))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Function to retrain the LSTM model periodically
def retrain_lstm_model():
    global lstm_model
    while True:
        print("Retraining LSTM model...")
        # Simulated dummy retraining data
        X_train = np.random.random((100, input_shape[0], input_shape[1]))
        y_train = np.random.randint(0, 2, 100)

        # Retrain the model
        lstm_model.fit(X_train, y_train, epochs=10, batch_size=64, verbose=0)
        print("LSTM model retrained!")

        time.sleep(3600)  # Retrain every hour

# Endpoint to make predictions with the LSTM model
@app.route('/predict_lstm', methods=['POST'])
def predict_lstm():
    global lstm_model
    data = request.json.get('data')
    input_data = np.array(data).reshape((1, len(data), 1))  # Reshape data for LSTM

    # Ensure the LSTM model exists
    if lstm_model is None:
        return jsonify({'error': 'LSTM model not available'}), 500

    prediction = lstm_model.predict(input_data)
    return jsonify({'prediction': prediction[0][0]})

# Main application logic to start the Flask app and LSTM retraining
if __name__ == '__main__':
    # Initialize the LSTM model
    lstm_model = create_lstm_model(input_shape)

    # Start background thread to retrain the LSTM model periodically
    threading.Thread(target=retrain_lstm_model).start()

    # Run the Flask application
    app.run(host='0.0.0.0', port=5001)
