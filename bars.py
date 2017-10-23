import json
from functools import reduce
from math import hypot
from sys import argv


def load_data(filepath):
    json_file = open(filepath, 'r')
    json_content = json_file.read()
    json_file.close()
    return json.loads(json_content)


def get_biggest_bar(bars):
    biggest_bar = max(bars, key = lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return biggest_bar['properties']['Attributes']['Name']

def get_smallest_bar(bars):
    smallest_bar = min(bars, key = lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return smallest_bar['properties']['Attributes']['Name']


# we ignore Earth radius as all points are very close
def get_distance(coords1, coords2):
    return hypot(coords2[0] - coords1[0], coords2[1] - coords1[1])


def get_closest_bar(bars, longitude, latitude):
    closest_bar_name = bars[0]['properties']['Attributes']['Name']
    shortest_distance = get_distance(bars[0]['geometry']['coordinates'], [longitude, latitude])
    for bar in bars[1:]:
        distance = get_distance(bar['geometry']['coordinates'], [longitude, latitude])
        if distance < shortest_distance:
            closest_bar_name = bar['properties']['Attributes']['Name']
            shortest_distance = distance
    return closest_bar_name


if __name__ == '__main__':
    bars = load_data(argv[1])['features']
    latitude = float(input('Please input your latitude: '))
    longitude = float(input('Please input your longitude: '))
    print('Biggest bar: ', get_biggest_bar(bars))
    print('Smallest bar: ', get_smallest_bar(bars))
    print('Closest bar: ', get_closest_bar(bars, longitude, latitude))
