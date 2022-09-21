import requests


class DistanceMatrix(object):
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def get_distance(self):
        result = requests.get(
            url=f"https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins={self.start_point['latitude']},{self.start_point['longitude']}&destinations={self.end_point['latitude']},{self.end_point['longitude']}&travelMode=driving&key=AucdCDVThRBldZKDIt7c-xyAY-_tMg1KA6EdlpHmsB4WHuNHKSdaGKJN2I_CkPwp")

        distance = result.json()['resourceSets'][0]['resources'][0]['results'][0]['travelDistance']
        duration = result.json()['resourceSets'][0]['resources'][0]['results'][0]['travelDuration']

        return {'distance': distance, 'duration': duration}


# start_point = {'latitude': 42.287304, 'longitude': 22.694212}
# end_point = {"latitude": 42.366879, "longitude": 23.005037}
# print(DistanceMatrix(start_point, end_point).get_distance())

