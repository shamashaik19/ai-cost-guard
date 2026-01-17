def estimate_cost(services):
    cost = {
        "EC2": services["EC2"] * 20,      # approx $20/month per instance
        "S3": services["S3"] * 2,
        "RDS": services["RDS"] * 30,
        "Lambda": services["Lambda"] * 5
    }
    total = sum(cost.values())
    return cost, total
