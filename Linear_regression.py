import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# load the dataset

df = pd.read_csv("data.csv")

# Encode 'location' to numeric using labelEncoder
le = LabelEncoder()
df["LocationIndex"] = le.fit_transform(df["Location"])


# define features and target
X = df[['Size', 'Bedroom', 'LocationIndex']]
Y = df['Rent']

# split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

#Train the Linear Model
model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

# Compare
#compare = pd.DataFrame({'Actual': Y_test, 'Prediction': Y_pred.astype(int)})
#print("\nActual vs Prediction:\n", compare.head())

new_location = 'Mumbai'
new_location_index = le.transform([new_location])[0]

new_data = [[1200, 3, new_location_index]]

predict = model.predict(new_data)
print(f"Predicted rent based on this data is {predict}")

