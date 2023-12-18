import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

# Load the dataset
data = pd.read_csv('traffic_data.csv')

# Separate the target variable 'severity' from other categories
X = data.drop('severity', axis=1)
y = data['severity']

# Preprocess the target variable into numerical data
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
y = to_categorical(y)

# Preprocess the categories using one-hot encoding
one_hot_encoder = OneHotEncoder()
X = one_hot_encoder.fit_transform(X).toarray()

# Split the dataset into training and testing sets with an 80/20 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = Sequential()
model.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))  # Input layer
model.add(Dense(16, activation='relu'))  # Hidden layer
model.add(Dense(5, activation='softmax'))  # Output layer

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Define the early stopping criteria
early_stopping = EarlyStopping(monitor='val_loss', patience=3, mode='min')

# Train the model
model.fit(X_train, y_train, epochs=1000, batch_size=32, callbacks=[early_stopping], validation_split=0.2)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy * 100}%')

# User input
roadblock = input("Enter roadblock: ")
time = input("Enter time: ")
weather = input("Enter weather: ")
infrastructure = input("Enter infrastructure: ")
type = input("Enter type: ")
volume = input("Enter volume: ")

user_input = [[roadblock, time, weather, infrastructure, type, volume]]
user_input = one_hot_encoder.transform(user_input).toarray()

# Make a prediction
prediction = model.predict(user_input)

# Convert prediction to label
severity = label_encoder.inverse_transform([prediction.argmax()])[0]

print(f'The predicted severity is: {severity}')
