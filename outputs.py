import apimodule


class Steps:
    '''Takes the JSON object and indexes it to obtain the directions.'''
    def generate_output(self, json):
        print("DIRECTIONS")
        dictionary_list = json['route']['legs']
        for dictionary in dictionary_list:
            for item in dictionary['maneuvers']:
                print(item['narrative'])
        print()



class Time:
    '''Takes the JSON object and indexes it to obtain the time of trip.'''
    def generate_output(self, json):
        print("TOTAL TIME: ",(int(round(json['route']['time']/60))), "minutes")
        print()



class Distance:
    '''Takes the JSON object and indexes it to obtain the distance of trip.'''
    def generate_output(self, json):
        print("TOTAL DISTANCE: ",(int(json['route']['distance'])),"miles")
        print()



class LatLong:
    '''Takes the JSON object and indexes it to obtain the
    latitudes and longitudes of each location.'''
    def generate_output(self, json):
        print("LATLONGS")
        dictionary_list = json['route']['locations']
        for dictionary in dictionary_list:
            latLng_dictionary = dictionary['latLng']
            latitude = round(latLng_dictionary['lat'], 2)
            longitude = round(latLng_dictionary['lng'], 2)
            if latitude < 0:
                latitude = str(abs(latitude)) + "S"
            else:
                latitude = str(latitude) + "N"
            if longitude < 0:
                longitude = str(abs(longitude)) + "W"
            else:
                longitude = str(longitude) + "E"
            print(latitude, longitude)
        print()



class Elevation:
    '''Takes the JSON object and indexes it to obtain the
    latitudes and longitudes of each location to make a new URL which is parsed
    and indexed to obtain the elevations of each location.'''
    def generate_output(self, json):
        print("ELEVATIONS")
        dictionary_list = json['route']['locations']
        for dictionary in dictionary_list:
            latLng_dictionary = dictionary['latLng']
            latitude = latLng_dictionary['lat']
            longitude = latLng_dictionary['lng']
            elevation_url = apimodule.make_elevation_url(latitude, longitude)
            json_elevation_response = apimodule.return_JSON(elevation_url)
            elevation_from_JSON = json_elevation_response['elevationProfile'][0]['height']
            elevation = int(round(elevation_from_JSON))
            print(elevation)
        print()



