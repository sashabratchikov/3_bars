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
    biggest_bar_name = bars[0]['properties']['Attributes']['Name']
    biggest_bar_seats = bars[0]['properties']['Attributes']['SeatsCount']
    for bar in bars[1:]:
        bar_attributes = bar['properties']['Attributes']
        seats_count = bar_attributes['SeatsCount']
        if seats_count > biggest_bar_seats:
            biggest_bar_name = bar_attributes['Name']
            biggest_bar_seats = seats_count
    return biggest_bar_name


def get_smallest_bar(bars):
    smallest_bar_name = bars[0]['properties']['Attributes']['Name']
    smallest_bar_seats = bars[0]['properties']['Attributes']['SeatsCount']
    for bar in bars[1:]:
        bar_attributes = bar['properties']['Attributes']
        seats_count = bar_attributes['SeatsCount']
        if seats_count < smallest_bar_seats:
            smallest_bar_name = bar_attributes['Name']
            smallest_bar_seats = seats_count
    return smallest_bar_name


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
