# Word Prediction

A Python project for implementing word prediction algorithms.

## Algorithms

- **Naive word prediction**: A simple approach that predicts the next word based on frequency counts of word sequences in the training corpus.

## Installation

### Prerequisites

- Python 3.13+
- Redis server

### Setup

1. Install dependencies:
```bash
pip install -e .
```

2. Start Redis server:
```bash
redis-server
```

## Usage

Before running, update the `FILE_NAME` variable in `src/config.py` to point to your corpus text file.

Run the prediction script:

```bash
python run.py
```

## Project Structure

```
word-prediction/
├── src/
│   ├── __init__.py
│   └── naive_word_prediction.py
├── pyproject.toml
├── README.md
├── LICENSE
└── .pre-commit-config.yaml
```
