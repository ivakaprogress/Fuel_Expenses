import requests


class FuelPrice(object):
    def __init__(self, fuel):
        self.fuel = fuel

    def get_price(self):
        result = requests.get(url=f'https://fuelo.net/api/price?key=0e77009a7bc05c6&fuel={self.fuel}')

        fuel_type = result.json()['fuel']
        price = result.json()['price']
        currency = result.json()['dimension']
        return {'Fuel type': fuel_type, 'Fuel price': price, 'Currency': currency}


# fuel = 'gasoline'
# print(FuelPrice(fuel).get_price())
