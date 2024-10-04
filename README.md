# ARC-AGI Genesis

## What is ARC-AGI ?

ARC-AGI (Abstraction and Reasoning Corpus for Artificial General Intelligence) is a benchmark designed to measure an AI's ability to acquire new skills and solve novel, abstract problems—key traits of general intelligence. Unlike typical AI benchmarks that focus on task-specific performance, ARC-AGI challenges AI systems to generalize knowledge to entirely new tasks without relying on extensive training data. It tests for abstraction, reasoning, and pattern recognition through a series of grid-based puzzles that are easy for humans but very difficult for machines.

> source: [arc-agi website](https://arcprize.org)

## What is ARC-AGI Genesis?

Are you new to ARC-AGI contest ?

ARC-AGI Genesis is a python framework that saves you significant time and effort by gathering a set of resources to help you tackle the competition.

In summary, ARC-AGI Genesis enables you to:

- Visually display problems in various ways.
- Easily deploy and evaluate your solutions with Kaggle (2 ways).
- Optimize task execution order during Kaggle evaluations for better performance.
- Work on small challenges before scalling to large challenges (such as 30x30 grids).

## Project Structure and Setup

After cloning this repository, you will have access to the following resources:

- **`challenges_plotting.ipynb`**: A demonstration of various ways to visually display the challenges. This notebook will help you explore the different graphical representations available to tackle the ARC tasks.

- **`challenges_sorting.ipynb`**: A notebook presenting an approach to optimize the task execution order during the evaluation process. It focuses on improving performance by reordering the challenges efficiently.

- **`tiny_arc.ipynb`**: A notebook designed for handling smaller challenges. It presents a working method for efficiently addressing compact and simpler problems before processing expansive tasks such as large grid tasks.

- **`kaggle_submission.ipynb`**: The notebook used for submitting your solutions via the [first approach](#by-importing-an-external-package). It walks through the process of preparing and submitting solutions using external package imports.

- **`self_sufficient_kaggle_submission.ipynb`**: The notebook used for submissions via the [second approach](#using-a-self-sufficient-notebook). This method ensures your notebook is entirely self-sufficient, without relying on external imports.

- **`local_bench.ipynb`**: A notebook for evaluating your solutions locally using the provided evaluation set (not the Kaggle one). This allows you to benchmark your performance in a controlled environment before submission.

## Kaggle publication

There are two main ways to submit your solution for the dedicated Kaggle evaluation. Both approaches have been tested and work seamlessly for the ARC-AGI competition on Kaggle.

In both cases, Kaggle expects a notebook for evaluation.

### By importing an external package

Separating the solution from the evaluation notebook seems like a cleaner approach in terms of software development. In this approach, the evaluation notebook imports a package containing the solution to be evaluated. However, Kaggle makes this method a bit tricky to implement. Here's how to proceed:

EXPLAIN

---

### Using a Self-Sufficient Notebook

If you're looking for a less clean but quicker approach to evaluate your solution, I've also prepared a version entirely contained within a single self-sufficient notebook — though it's quite loaded! This method bypasses some of the complexities of external package management, offering a more straightforward solution.

## Contribute!

Help make this framework even more powerful and help others drive significant advancements towards AGI.

We welcome contributions from everyone, regardless of their background.

Every contribution—whether it's code, documentation, translations, or even bug reporting—is valuable to us. Together, we can make this project even better!
