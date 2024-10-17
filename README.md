```markdown
# Financial Data Analytics Microservices

## Overview

This project consists of two microservices designed to analyze financial data using machine learning models. The services are built with Flask and leverage libraries such as XGBoost and TensorFlow for predictions and trading strategies.

## Services

### 1. Service A: LSTM Prediction Service

- **Endpoint:** `/predict_lstm`
- **Method:** POST
- **Description:** This service receives financial features as input and returns predictions using an LSTM model.
- **Dependencies:** Flask, TensorFlow, NumPy

### 2. Service B: Trading Strategy Service

- **Endpoints:**
  - `/get_historical_data`
  - `/run_strategy`
- **Method:** POST
- **Description:** This service fetches historical data for specified tickers, processes it, and implements a trading strategy using XGBoost and LSTM predictions.
- **Dependencies:** Flask, XGBoost, Pandas, Scikit-learn, yFinance, Alpaca-Trade-API

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Final_Project_Financial_Data_Analytics/microservices
   ```

2. Build the Docker images:
   ```bash
   docker-compose build
   ```

3. Start the services:
   ```bash
   docker-compose up
   ```

### Stopping the Services

To stop the running services, use the following command:
```bash
docker-compose down
```

## Usage

- You can interact with the services using tools like Postman or cURL.
- To get historical data, send a POST request to `/get_historical_data` with a JSON payload containing the ticker symbol.
- To run the trading strategy, send a POST request to `/run_strategy` with a JSON payload containing the necessary data.

## Notes

- Ensure that your Alpaca API credentials are set correctly in the `service_b.py` file.
- The models will retrain automatically every hour based on the historical data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
