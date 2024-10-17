# ARC Genesis 🚀

## What is ARC-AGI?

ARC-AGI (Abstraction and Reasoning Corpus for Artificial General Intelligence) is a benchmark that evaluates AI's ability to solve novel, abstract problems—key aspects of general intelligence according to ARC creators.

Unlike traditional benchmarks, ARC-AGI tests how well AI can generalize to new tasks, focusing on abstraction, reasoning, and pattern recognition through grid-based puzzles.

![A basic task example from the Abstract and Reason Corpus](https://arcprize.org/media/images/arc-example-task.jpg)

> Source: [arc-agi website](https://arcprize.org)

## What is ARC Genesis?

🌟 **ARC Genesis** is a Python framework built to help you working in the ARC-AGI contest by providing essential tools and resources. It enables you to:

- Visualize problems effectively.
- Deploy and evaluate solutions via Kaggle (2 methods).
- Optimize task execution order for better performance.
- Start small before scaling to complex challenges (like 30x30 grids).

## What is JupyterGenesis?

[JupyterGenesis](https://github.com/MaloLM/JupyterGenesis) simplifies setting up a Jupyter environment across platforms (Linux, macOS, Windows). It automates virtual environment creation and Python package installation.

### How to Use JupyterGenesis?

Simply run the script for your OS to install dependencies and launch a local JupyterLab server for your development needs.

> For more details, check the [documentation](./jupyter-genesis/README.md).

## Requirements

You only need `Python 3` and `pip`, under Linux, macOS, or Windows.

## Project Structure and Setup

After cloning the repository, you’ll access:

- **`challenges_plotting.ipynb`**: Visualizes ARC challenges with various graphical methods.
- **`challenges_sorting.ipynb`**: Optimizes task execution order during evaluations.
- **`tiny_arc.ipynb`**: Focuses on solving smaller, simpler tasks before scaling to larger ones.
- **`kaggle_submission.ipynb`**: Prepares solutions for submission using external package imports.
- **`self_sufficient_kaggle_submission.ipynb`**: Offers a self-contained submission method.
- **`local_benchmark.ipynb`**: Benchmarks your solutions locally.

## Kaggle Submission

Kaggle requires notebook submissions for evaluation. You can submit in two ways:

### 1. By Importing an External Package

This approach separates the solution and evaluation for cleaner development. Refer to `/source/kaggle_submission.ipynb`.

### 2. Using a Self-Sufficient Notebook

A quicker, all-in-one solution without external imports but with some limitations... Refer to `self_sufficient_kaggle_submission.ipynb`.

## Contribute! 🙌

Contributions are welcome from anyone! Whether it's code, documentation, translations, or bug reporting, every contribution helps us move closer to AGI.
