import pandas as pd

def predict_pricing(model,data,claim_prob):

    df = pd.DataFrame([[

        data["age"],
        data["income"],
        data["premium"],
        claim_prob

    ]],columns=["age","income","premium","claim_flag"])

    price = model.predict(df)[0]

    return price