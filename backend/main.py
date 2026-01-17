from fastapi import FastAPI
from backend.aws_services import get_services
from cost_estimator import estimate_cost

app = FastAPI(title="AWS Cost Guard API")

@app.get("/status")
def aws_status():
    services = get_services()
    costs, total = estimate_cost(services)
    return {
        "services": services,
        "costs": costs,
        "estimated_monthly_cost": total
    }
