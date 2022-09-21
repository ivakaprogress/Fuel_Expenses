from fastapi import FastAPI
from routers import fuel_distance_budget_info

app = FastAPI()
app.include_router(fuel_distance_budget_info.router)
