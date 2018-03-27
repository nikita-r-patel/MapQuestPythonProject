import apimodule
import outputs

''' * User Input Example (First line = number of locations, 4th line = number of
    * desired information fields (possible ones listed in example below
3
4533 Campus Dr, Irvine, CA
1111 Figueroa St, Los Angeles, CA
3799 S Las Vegas Blvd, Las Vegas, NV
5
LATLONG
STEPS
TOTALTIME
TOTALDISTANCE
ELEVATION
'''


def make_locations_list()-> list:
    '''Gets input for number of locations and then the locations, then puts
    them into a list.'''
    locations_list = []
    number_of_locations = int(input())
    for iteration in range(number_of_locations):
        location = input()
        locations_list.append(location)
    return locations_list



def specified_outputs() -> list:
    '''Gets input for number of information parameters desired then gets them and stores
    into a list.'''
    outputs_list = []
    number_of_outputs = int(input())
    for iteration in range(number_of_outputs):
        output = input().upper()
        outputs_list.append(output)
    print()
    return outputs_list



def outputs_generated(outputs_list: list)-> str:
    '''From the outputs list generated, uses dictionary indexing to invoke class method for
    specified parameter.'''
    outputs_dictionary = {
        "STEPS": outputs.Steps(),
        "TOTALDISTANCE": outputs.Distance(),
        "TOTALTIME": outputs.Time(),
        "LATLONG":outputs.LatLong(),
        "ELEVATION": outputs.Elevation()
        }
    for output in outputs_list:
        outputs_dictionary[output].generate_output(json_response)
    print("Directions Courtesy of MapQuest; Map Data Copyright" +
          " OpenStreetMap Contributors")
            


if __name__ == '__main__':
    locations_list = make_locations_list()
    url = apimodule.make_search_url(locations_list)
    json_response = apimodule.return_JSON(url)
    apimodule.validate_JSON(json_response)
    outputs_list = specified_outputs()
    outputs_generated(outputs_list)
    


