from fastapi import APIRouter
from schemas.schemas import SchemaGetUserInfo
from classes.fuel_price import FuelPrice
from classes.distance_matrix import DistanceMatrix

router = APIRouter()


@router.post('/distance')
def get_distance(schema: SchemaGetUserInfo):

    fuel_price = FuelPrice(schema.fuel).get_price()['Fuel price']
    distance = DistanceMatrix(schema.start_point, schema.end_point).get_distance()['distance'] / 100
    total_price = fuel_price * schema.consumption_per_100km * distance
    price_per_person = total_price / schema.total_passengers
    fuel_required = schema.consumption_per_100km * distance

    return {'price per person': round(price_per_person, 2),
            'total price': round(total_price, 2),
            'fuel required': round(fuel_required, 2),
            'distance/km': round(distance * 100, 1)}
