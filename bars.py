import json
from math import hypot
from sys import argv


def load_data(filepath):
    with open(filepath, 'r') as json_file:
        return json.loads(json_file.read())


def get_distance(point1, point2):
    return hypot(point2[0] - point1[0], point2[1] - point1[1])


def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


def get_biggest_bar(bars):
    return max(bars, key=lambda bar: bar['properties']
                                        ['Attributes']
                                        ['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars, key=lambda bar: bar['properties']
                                        ['Attributes']
                                        ['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    return min(bars, key=lambda bar: get_distance(bar['geometry']
                                                     ['coordinates'],
                                                  [longitude, latitude]))


if __name__ == '__main__':
    bars = load_data(argv[1])['features']
    latitude = float(input('Please input your latitude: '))
    longitude = float(input('Please input your longitude: '))
    print('Biggest bar: ', get_bar_name(get_biggest_bar(bars)))
    print('Smallest bar: ', get_bar_name(get_smallest_bar(bars)))
    print('Closest bar: ', get_bar_name(get_closest_bar(bars,
                                                        longitude,
                                                        latitude)))
