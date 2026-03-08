import pandas as pd

def detect_fraud(model,data):

    df = pd.DataFrame([data])

    pred = model.predict(df)[0]

    if pred == -1:
        return "High Fraud Risk"

    return "Low Fraud Risk"