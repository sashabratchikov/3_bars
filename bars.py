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
    biggest_bar = bars[0]
    for bar in bars[1:]:
        seats_count = bar['properties']['Attributes']['SeatsCount']
        if seats_count > biggest_bar['properties']['Attributes']['SeatsCount']:
            biggest_bar = bar
    return biggest_bar


def get_smallest_bar(bars):
    smallest_bar = bars[0]
    for bar in bars[1:]:
        seats_count = bar['properties']['Attributes']['SeatsCount']
        if seats_count < smallest_bar['properties']['Attributes']['SeatsCount']:
            smallest_bar = bar
    return smallest_bar


# we ignore Earth radius as all points are very close
def get_distance(coords1, coords2):
    return hypot(coords2[0] - coords1[0], coords2[1] - coords1[1])


def get_closest_bar(bars, longitude, latitude):
    closest_bar = bars[0]
    shortest_distance = get_distance(closest_bar['geometry']['coordinates'], [longitude, latitude])
    for bar in bars[1:]:
        distance = get_distance(bar['geometry']['coordinates'], [longitude, latitude])
        if distance < shortest_distance:
            closest_bar = bar
            shortest_distance = distance
    return closest_bar


if __name__ == '__main__':
    bars = load_data(argv[1])['features']
    latitude = float(input('Please input your latitude: '))
    longitude = float(input('Please input your longitude: '))
    print(get_biggest_bar(bars))
    print(get_smallest_bar(bars))
    print(get_closest_bar(bars, longitude, latitude))
