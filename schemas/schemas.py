from pydantic import BaseModel


class SchemaGetUserInfo(BaseModel):
    start_point: dict
    end_point: dict
    fuel: str
    consumption_per_100km: int
    total_passengers: int

