import pandas as pd
import os
import random

DATA_FILE = "insuranceclaims.csv"


def create_dummy_data():

    data = []

    regions = ["Mumbai","Delhi","Bangalore","Chennai"]
    hospitals = ["Apollo","Fortis","Max","Manipal"]

    for i in range(200):

        age = random.randint(20,70)
        income = random.randint(20000,100000)
        premium = random.randint(5000,40000)

        region = random.choice(regions)
        hospital = random.choice(hospitals)

        claim_flag = random.choice([0,1])
        premium_adjustment = random.randint(0,20)

        data.append([
            age,income,premium,region,hospital,
            claim_flag,premium_adjustment
        ])

    df = pd.DataFrame(data,columns=[
        "age","income","premium","region","hospital",
        "claim_flag","premium_adjustment"
    ])

    df.to_csv(DATA_FILE,index=False)

    return df


def load_dataset():

    if not os.path.exists(DATA_FILE):
        print("Dataset not found. Creating dummy dataset...")
        return create_dummy_data()

    return pd.read_csv(DATA_FILE)