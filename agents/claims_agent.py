import pandas as pd

def predict_claim(model,data):

    df = pd.DataFrame([data])

    prob = model.predict_proba(df)[0][1]

    return prob