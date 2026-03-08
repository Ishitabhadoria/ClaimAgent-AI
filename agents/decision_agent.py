def make_decision(
        claim_prob,
        fraud_risk,
        network_risk,
        risk_score
):

    if fraud_risk=="High Fraud Risk" or network_risk=="High Network Fraud Risk":
        return "Full Investigation Required"

    if claim_prob > 0.6:
        return "Approve with Caution"

    return "Approve Claim"