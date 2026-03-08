from agents.claims_agent import predict_claim
from agents.fraud_agent import detect_fraud
from agents.network_agent import detect_network_fraud
from agents.risk_agent import evaluate_risk
from agents.pricing_agent import predict_pricing
from agents.decision_agent import make_decision
from agents.report_agent import generate_report

from memory.vectorstore import store_vector

from models import train_models

claim_model,fraud_model,risk_model,pricing_model = train_models()

def run_system(data):

    claim_prob = predict_claim(claim_model,data)

    fraud_risk = detect_fraud(fraud_model,data)

    network_risk = detect_network_fraud(data)

    risk_score = evaluate_risk(risk_model,data)

    price = predict_pricing(pricing_model,data,claim_prob)

    decision = make_decision(
        claim_prob,
        fraud_risk,
        network_risk,
        risk_score
    )

    report = generate_report(
        data,
        claim_prob,
        fraud_risk,
        network_risk,
        risk_score,
        price,
        decision
    )

    store_case(report)

    return report