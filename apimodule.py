import urllib.request
import urllib.parse
import json
import sys


MAP_QUEST_API_KEY = 'Fmjtd%7Cluu8216znd%2C2n%3Do5-9425uy'

DECODED_API_KEY = 'Fmjtd|luu8216znd,2n=o5-9425uy'

MAP_QUEST_BASE_URL = 'http://open.mapquestapi.com/directions/v2'

ELEVATION_BASE_URL = "http://open.mapquestapi.com/elevation/v1/profile?"



def list_of_locations_tuples(locations_list)-> list:
    '''Generates a list of tuples from the list of locations to append to the
    query parameters when building the URL.'''
    locations_tuples_list = []
    first_location = ('from', locations_list[0])
    locations_tuples_list.append(first_location)
    for location in locations_list[1: ]:
        locations_tuples_list.append(('to',location))
    return(locations_tuples_list)
    
    
    
def make_search_url(locations_list: list)-> str:
    '''Returns URL with necessary parameters (API key, ambiguities, 'from'
    tuple, 'to' tuples).'''
    query_parameters = [('key', DECODED_API_KEY),('ambiguities', 'ignore')]\
                       + list_of_locations_tuples(locations_list)
    return MAP_QUEST_BASE_URL + '/route?' + \
           urllib.parse.urlencode(query_parameters)



def return_JSON(url: str)-> 'json':
    '''Returns parsed JSON response when opening generated URL.  If opening or
    processing the url fails, MAPQUEST ERROR is printed and the program stops
    running.'''
    open_url_response = None
    try:
        open_url_response = urllib.request.urlopen(url)
        json_script = open_url_response.read().decode(encoding='utf-8')
        json_response = json.loads(json_script)
        return json_response
    except:
        print()
        print("MAPQUEST ERROR")
        sys.exit(0)
    finally:
        if open_url_response != None:
            open_url_response.close()



def validate_JSON(json_response: 'json')-> 'json' or str:
    '''Checks to see if the JSON can be used to obtain the outputs.  If it does,
    the JSON response is returned.  If it is not usable, an error message is
    displayed and the program stops running.'''
    if json_response['info']['statuscode'] == 0:
        return json_response
    elif json_response['info']['statuscode'] in [400,500,601,602,603,609,610]:
        print()
        print("NO ROUTE FOUND")
        sys.exit(0)
    else:
        print()
        print("MAPQUEST ERROR")
        sys.exit(0)



def make_elevation_url(latitude: int, longitude: int)-> str:
    '''Makes an elevation url with latitude and longitude parameters to be used
    in the Elevation class.'''
    elevation_url = ELEVATION_BASE_URL + "&key=" + MAP_QUEST_API_KEY + \
                        "&shapeFormat=raw&unit=f&latLngCollection=" + \
                        (str(latitude)+"%2C") + str(longitude)
    return elevation_url   



    
