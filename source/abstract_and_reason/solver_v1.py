import numpy as np
from abstract_and_reason.graphics import Graphics
from abstract_and_reason.assets import load_json


class Solver:
    """
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
        try:
            raise NotImplementedError
        except Exception:
            answers = self.random_prediction(
                puzzle_outs_train, puzzle_inps_test)

        return answers

    def random_prediction(self, puzzle_outs_train, puzzle_inps_test):
        answers = []
        avg_shape = np.ceil(np.array([np.array(p.shape) for p in puzzle_outs_train]).mean(
            0)).astype(int)  # I took average shape of output puzzles
        for _ in range(len(puzzle_inps_test)):
            # cause 0 to 9 options as mentioned in competition
            answers.append(np.random.randint(0, 10, size=avg_shape))

        return answers

    def train(self):
        pass

    def validate(self):
        pass

    def test(self):
        pass

    def display_train(self, task_id, puzzle_inps_train, puzzle_outs_train):
        self.graphics.plot_task(
            f"Train: #{task_id}", puzzle_inps_train, puzzle_outs_train,)

    def display_test(self, task_id, puzzle_inps_test, puzzle_outs_test):
        self.graphics.plot_task(
            f"Test: #{task_id}", puzzle_inps_test, puzzle_outs_test)

    def display_task(self, task_id, puzzle_inps_train, puzzle_outs_train, puzzle_inps_test, puzzle_outs_test=None):
        self.graphics.plot_full_task(f"Task #{task_id}", puzzle_inps_train,
                                     puzzle_outs_train, puzzle_inps_test, puzzle_outs_test)

    def display_board(self, task_id, board):
        self.graphics.plot_board(f"Task #{task_id}", board)

    def display_side_to_side_boards(self, board_right, board_left, title, text_right, text_left, b1_cmap=None, b2_cmap=None):
        self.graphics.plot_side_to_side_boards(
            board_right, board_left, title, text_right, text_left, b1_cmap, b2_cmap)

    def get_challenge_board(self, challenge_id, challenges, solutions, io: str, board_type: str, board_idx):
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
        # solutions=None cause test_challenges doesn't have solutions,
        # So we can use this function on test challenge as well (big brain move)
        one_challenge = challenges[challenge_id]

        puzzle_inps_train = []
        puzzle_outs_train = []
        for puzzles in one_challenge['train']:
            # convert to numpy array before you append so we can see it as a matrix
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
