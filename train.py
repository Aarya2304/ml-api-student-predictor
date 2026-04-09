import numpy
import pandas
from sklearn.linear_model import LinearRegression
import pickle

data = {
    "hours": [1,2,3,4,5,6,7,8],
    "attendance": [50,60,65,70,75,80,85,90],
    "score": [40,50,55,60,65,70,75,85]
}

df = pandas.DataFrame(data)

X = df[["hours", "attendance"]]
y = df[["score"]]

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)


with open("model.pkl", "rb") as f:
    model = pickle.load(f)


sample_input = [[5,80]]
prediction = model.predict(sample_input)

print("Predicted score:", prediction[0])