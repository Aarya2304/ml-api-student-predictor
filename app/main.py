import pickle
import fastapi
import pandas as pd
app = fastapi.FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/predict")
def predict(data: dict):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

        hours = data["hours"]
        attendance = data["attendance"]

        input_data = pd.DataFrame([[hours, attendance]],
                                  columns = ["hours", "attendance"])

        result = model.predict(input_data)

        print(f"Predicted score: {result[0]}")
        return {"predicted_score": float(result[0])}
