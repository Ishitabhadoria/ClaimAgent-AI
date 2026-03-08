import pandas as pd

def evaluate_risk(model,data):

    df = pd.DataFrame([data])

    cluster = model.predict(df)[0]

    risk_score = cluster/2

    return risk_score