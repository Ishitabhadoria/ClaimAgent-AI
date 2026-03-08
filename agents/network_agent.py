import networkx as nx

def detect_network_fraud(data):

    G = nx.Graph()

    G.add_edge(data["hospital"],data["region"])

    centrality = nx.degree_centrality(G)

    score = list(centrality.values())[0]

    if score > 0.5:
        return "High Network Fraud Risk"

    return "Low Network Fraud Risk"