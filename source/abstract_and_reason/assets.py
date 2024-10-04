# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

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


def sort_challenges_by_size(challenges, ascending=True):
    """
    Sorts the challenges by the number of cells in their training examples (input+output).

    This function sorts a dictionary of challenges ID based on the total number 
    of cells (elements) in the 'input' and 'output' grids of the 'train' examples.

    Parameters:
    -----------
    challenges : dict
        A dictionary where keys are challenge IDs and values are challenge details.
        Each challenge contains a 'train' key, which is a list of examples, and each 
        example has 'input' and 'output' lists of lists.

    ascending : bool, optional (default=True)
        If True, the challenges are sorted in ascending order by the number of cells.
        If False, they are sorted in descending order.

    Returns:
    --------
    list
        A list of challenge IDs sorted by the number of cells in the 'train' examples.


    Example:
    --------
    res = sort_challenges_by_size(training_challenges)
    """
    def count_challenge_cells(challenge):
        return sum(
            extract_numbers(example['input']) + extract_numbers(example['output']) 
            for example in challenge['train']
        )

    def extract_numbers(list_of_lists):
        return sum(len(sublist) for sublist in list_of_lists)
    
    def check_ids(list1, list2):
        return sorted(list1) == sorted(list2)
    
    def sort_ids_by_numbers(ids, numbers, ascending=True):
        return [id for _, id in sorted(zip(numbers, ids), reverse=not ascending)]
        
    challenge_ids = list(challenges)
    numbers = [count_challenge_cells(challenges[_id]) for _id in challenge_ids]

    return sort_ids_by_numbers(challenge_ids, numbers, ascending=ascending)
