from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans

from data_utils import load_dataset

def preprocess(df):

    df["region"] = df["region"].astype("category").cat.codes
    df["hospital"] = df["hospital"].astype("category").cat.codes

    return df


def train_models():

    df = load_dataset()
    df = preprocess(df)

    X = df[["age","income","premium","region","hospital"]]
    y = df["claim_flag"]

    claim_model = RandomForestClassifier()
    claim_model.fit(X,y)

    fraud_model = IsolationForest(contamination=0.1)
    fraud_model.fit(X)

    risk_model = KMeans(n_clusters=3)
    risk_model.fit(X)

    Xp = df[["age","income","premium","claim_flag"]]
    yp = df["premium_adjustment"]

    pricing_model = RandomForestRegressor()
    pricing_model.fit(Xp,yp)

    return claim_model,fraud_model,risk_model,pricing_model