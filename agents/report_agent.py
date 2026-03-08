def generate_report(
        data,
        claim_prob,
        fraud_risk,
        network_risk,
        risk_score,
        price,
        decision
):

    report = f"""
INSURANCE INVESTIGATION REPORT

Customer Age: {data['age']}
Income: {data['income']}
Premium: {data['premium']}

Claim Probability: {claim_prob:.2f}

Fraud Risk: {fraud_risk}
Network Fraud Risk: {network_risk}

Risk Score: {risk_score:.2f}

Recommended Premium Adjustment: {price:.2f}

FINAL DECISION:
{decision}
"""

    return report