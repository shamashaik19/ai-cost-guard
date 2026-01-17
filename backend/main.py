from fastapi import FastAPI
from backend.aws_services import get_running_services
from backend.cost_estimator import estimate_cost

app = FastAPI()

@app.get("/status")
def aws_status():
    services = get_running_services()
    costs, total = estimate_cost(services)

    return {
        "services": services,
        "costs": costs,
        "estimated_monthly_cost": total
    }
