import json
import random


def shuffle_list(input_list):
    """
    Shuffles the elements of the given list in place and returns it.

    Args:
        input_list (list): The list to be shuffled.

    Returns:
        list: The shuffled list.
    """
    random.shuffle(input_list)
    return input_list


def load_json(file_path):
    """
    Loads and returns the contents of a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The data loaded from the JSON file.
    """
    with open(file_path) as f:
        data = json.load(f)
    return data


arc_agi_colormap = {
    0: '#404040',
    1: '#2e67c0',
    2: '#af3827',
    3: '#4f942e',
    4: '#e0c231',
    5: '#6d6d6d',
    6: '#9f3674',
    7: '#b76424',
    8: '#6d9fb6',
    9: '#5f1a23'
}
"""
A colormap for the ARC-AGI benchmark, mapping integers to hex color codes.
"""


def manhattan_distance(xa, ya, xb, yb):
    """
    Calculates the Manhattan distance between two points in a grid.

    Args:
        xa (int): x-coordinate of the first point.
        ya (int): y-coordinate of the first point.
        xb (int): x-coordinate of the second point.
        yb (int): y-coordinate of the second point.

    Returns:
        int: The Manhattan distance between the two points.
    """
    return abs(xa - xb) + abs(ya - yb)


def calculate_center(points):
    """
    Calculates the geometric center (centroid) of a list of 2D points.

    Args:
        points (list of tuples): A list of (x, y) tuples representing the coordinates of points.

    Returns:
        tuple: The (x, y) coordinates of the center point.
    """
    x_coordinates = [point[0] for point in points]
    y_coordinates = [point[1] for point in points]

    center_x = sum(x_coordinates) / len(x_coordinates)
    center_y = sum(y_coordinates) / len(y_coordinates)

    return (center_x, center_y)
