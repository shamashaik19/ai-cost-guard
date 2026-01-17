def estimate_cost(services):
    cost = {}
    total = 0

    pricing = {
        "EC2": 20,
        "S3": 2,
        "RDS": 30,
        "Lambda": 5
    }

    for service, price in pricing.items():
        value = services.get(service)

        if isinstance(value, int):
            cost[service] = value * price
            total += cost[service]
        else:
            cost[service] = "Not available"

    return cost, total
