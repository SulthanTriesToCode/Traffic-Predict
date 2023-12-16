# Traffic Severity Prediction

This project uses a machine learning model to predict traffic severity based on various factors such as roadblock, time, weather, road infrastructure, types of roads, and traffic volume. The model is trained on a dataset containing these factors and their corresponding traffic severity.

## Dataset

The dataset used for this project is `traffic_data.csv`. It contains the following columns:

- Roadblock
- Time
- Weather
- Road Infrastructure
- Types of Roads
- Traffic Volume
- Severity of Traffic

## Model

The model used for this project is a Sequential model from Keras. It is trained for 300 epochs with early stopping. The model's performance is evaluated based on its loss and validation loss.

## Libraries

The following libraries are used in this project:

- pandas
- numpy
- keras
- sklearn
- matplotlib

## Usage

To use this project, run the `traffic_predict.ipynb` notebook. It loads the dataset, preprocesses it, trains the model, and finally, predicts the traffic severity.

## Results

The model's predictions are plotted against the actual traffic severity to visualize its performance.

