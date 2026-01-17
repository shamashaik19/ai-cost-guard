def estimate_cost(services):
    pricing = {
        "EC2": 20,
        "S3": 5,
        "RDS": 30,
        "Lambda": 5
    }

    costs = {}
    total = 0

    for svc, count in services.items():
        cost = count * pricing.get(svc, 0)
        costs[svc] = cost
        total += cost

    return costs, total
