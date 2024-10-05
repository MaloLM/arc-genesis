# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import numpy as np
from abstract_and_reason.graphics import Graphics
from abstract_and_reason.assets import load_json


class Solver:
    """
    Solver class for implementing solutions to ARC-AGI challenges.

    This class provides methods to load and display challenge data, predict puzzle outputs,
    and evaluate the performance of a model.
    """

    def __init__(self, prod=False) -> None:
        self.graphics = Graphics()

        if prod:
            self.base_path = '/kaggle/input/arc-prize-2024/'
        else:
            self.base_path = '../data/challenges/'

        self.training_challenges = load_json(
            self.base_path + 'arc-agi_training_challenges.json')
        self.training_solutions = load_json(
            self.base_path + 'arc-agi_training_solutions.json')
        self.evaluation_challenges = load_json(
            self.base_path + 'arc-agi_evaluation_challenges.json')
        self.evaluation_solutions = load_json(
            self.base_path + 'arc-agi_evaluation_solutions.json')
        self.test_challenges = load_json(
            self.base_path + 'arc-agi_test_challenges.json')
        self.sample_submission = load_json(
            self.base_path + 'sample_submission.json')

    def predict(self, puzzle_inps_train, puzzle_outs_train, puzzle_inps_test, puzzle_outs_test=None):
        """
        Predicts the outputs for test puzzles based on training inputs and outputs.

        Args:
            puzzle_inps_train (list): Training input puzzles.
            puzzle_outs_train (list): Training output puzzles.
            puzzle_inps_test (list): Test input puzzles.
            puzzle_outs_test (list, optional): Test output puzzles, used for validation purposes.

        Returns:
            list: Predicted outputs for the test puzzles.
        """
        try:
            # Your board prediction solution goes here !
            raise NotImplementedError
        except Exception:
            answers = self.random_prediction(
                puzzle_outs_train, puzzle_inps_test)

        return answers

    def random_prediction(self, puzzle_outs_train, puzzle_inps_test):
        """
        Generates random predictions for the test puzzles by averaging the shape of the training outputs.

        Args:
            puzzle_outs_train (list): Training output puzzles.
            puzzle_inps_test (list): Test input puzzles.

        Returns:
            list: Randomly generated predictions for the test puzzles.
        """
        answers = []
        avg_shape = np.ceil(np.array([np.array(p.shape) for p in puzzle_outs_train]).mean(
            0)).astype(int)  # I took average shape of output puzzles
        for _ in range(len(puzzle_inps_test)):
            # cause 0 to 9 options as mentioned in competition
            answers.append(np.random.randint(0, 10, size=avg_shape))

        return answers

    def train(self):
        """
        Placeholder for the training logic of the model.

        Raises:
            NotImplementedError: This function is not implemented.
        """
        raise NotImplementedError

    def validate(self):
        """
        Placeholder for the validation logic of the model.

        Raises:
            NotImplementedError: This function is not implemented.
        """
        # Have you trained a model? use this function to validate it.
        raise NotImplementedError

    def test(self):
        """
        Placeholder for the testing logic of the model on unseen test data.

        Raises:
            NotImplementedError: This function is not implemented.
        """
        # Have you trained a model? use this function to test it.
        raise NotImplementedError

    def display_train(self, task_id, puzzle_inps_train, puzzle_outs_train):
        """
        Displays the training input and output puzzles using the Graphics class.

        Args:
            task_id (int): ID of the task to be displayed.
            puzzle_inps_train (list): Training input puzzles.
            puzzle_outs_train (list): Training output puzzles.
        """
        self.graphics.plot_task(
            f"Train: #{task_id}", puzzle_inps_train, puzzle_outs_train,)

    def display_test(self, task_id, puzzle_inps_test, puzzle_outs_test):
        """
        Displays the test input and output puzzles using the Graphics class.

        Args:
            task_id (int): ID of the task to be displayed.
            puzzle_inps_test (list): Test input puzzles.
            puzzle_outs_test (list): Test output puzzles.
        """
        self.graphics.plot_task(
            f"Test: #{task_id}", puzzle_inps_test, puzzle_outs_test)

    def display_task(self, task_id, puzzle_inps_train, puzzle_outs_train, puzzle_inps_test, puzzle_outs_test=None):
        """
        Displays the full task, including training and test puzzles, using the Graphics class.

        Args:
            task_id (int): ID of the task to be displayed.
            puzzle_inps_train (list): Training input puzzles.
            puzzle_outs_train (list): Training output puzzles.
            puzzle_inps_test (list): Test input puzzles.
            puzzle_outs_test (list, optional): Test output puzzles. Default is None.
        """
        self.graphics.plot_full_task(f"Task #{task_id}", puzzle_inps_train,
                                     puzzle_outs_train, puzzle_inps_test, puzzle_outs_test)

    def display_board(self, task_id, board):
        """
        Displays a single puzzle board using the Graphics class.

        Args:
            task_id (int): ID of the task to be displayed.
            board (numpy.ndarray): The puzzle board to be displayed.
        """
        self.graphics.plot_board(f"Task #{task_id}", board)

    def display_side_to_side_boards(self, board_right, board_left, title, text_right, text_left, b1_cmap=None, b2_cmap=None):
        """
        Displays two boards side by side using the Graphics class.

        Args:
            board_right (numpy.ndarray): The board to display on the right.
            board_left (numpy.ndarray): The board to display on the left.
            title (str): The title for the figure.
            text_right (str): The label for the right board.
            text_left (str): The label for the left board.
            b1_cmap (matplotlib.colors.Colormap, optional): Colormap for the right board.
            b2_cmap (matplotlib.colors.Colormap, optional): Colormap for the left board.
        """
        self.graphics.plot_side_to_side_boards(
            board_right, board_left, title, text_right, text_left, b1_cmap, b2_cmap)

    def get_challenge_board(self, challenge_id, challenges, solutions, io: str, board_type: str, board_idx):
        """
        Retrieves a specific board from the challenge dataset.

        Args:
            challenge_id (int): ID of the challenge.
            challenges (dict): Challenge dataset.
            solutions (dict): Solution dataset.
            io (str): 'input' or 'output' to specify which board to retrieve.
            board_type (str): 'train' or 'test' to specify which dataset to retrieve the board from.
            board_idx (int): Index of the board to retrieve.

        Returns:
            numpy.ndarray: The requested board, or None if not found.
        """
        board = None
        if challenge_id in list(challenges):
            puzzle_inps_train, puzzle_outs_train, puzzle_inps_test, puzzle_outs_test = self.process_challenge(
                challenge_id, challenges, solutions)
            if io == 'input':
                if board_type == 'train':
                    if board_idx in range(0, len(puzzle_inps_train)):
                        board = puzzle_inps_train[board_idx]
                else:
                    if board_idx in range(0, len(puzzle_inps_test)):
                        board = puzzle_inps_test[board_idx]
            else:
                if board_type == 'train':
                    if board_idx in range(0, len(puzzle_outs_train)):
                        board = puzzle_outs_train[board_idx]
                else:
                    if board_idx in range(0, len(puzzle_outs_test)):
                        board = puzzle_outs_test[board_idx]
        return board

    def process_challenge(self, challenge_id, challenges, solutions=None):
        """
        Processes a single challenge by extracting its training and test inputs and outputs.

        Args:
            challenge_id (int): ID of the challenge to process.
            challenges (dict): Dictionary of challenges.
            solutions (dict, optional): Dictionary of solutions. If None, test solutions are not processed.

        Returns:
            tuple: Training inputs, training outputs, test inputs, and optionally test outputs if solutions are provided.
        """
        # solutions=None cause test_challenges doesn't have solutions
        # So we can use this function on test challenge as well (big brain move)
        one_challenge = challenges[challenge_id]

        puzzle_inps_train = []
        puzzle_outs_train = []
        for puzzles in one_challenge['train']:
            puzzle_inps_train.append(np.array(puzzles['input']))
            puzzle_outs_train.append(np.array(puzzles['output']))

        puzzle_inps_test = []
        for puzzles in one_challenge['test']:
            puzzle_inps_test.append(np.array(puzzles['input']))

        if solutions != None:
            one_solution = solutions[challenge_id]
            puzzle_outs_test = []
            for puzzles in one_solution:
                puzzle_outs_test.append(np.array(puzzles))

            return puzzle_inps_train, puzzle_outs_train, puzzle_inps_test, puzzle_outs_test

        else:
            return puzzle_inps_train, puzzle_outs_train, puzzle_inps_test, None
