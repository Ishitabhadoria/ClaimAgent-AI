import faiss
import numpy as np

dimension = 128
index = faiss.IndexFlatL2(dimension)

memory = []

def store_vector(report):

    vec = np.random.rand(1,128).astype("float32")

    index.add(vec)

    memory.append(report)