# CISC/CMPE 204 Modelling Project

Welcome to the major project for CISC/CMPE 204!

Change this README.md file to summarize your project, and provide pointers to the general structure of the repository. How you organize and build things (which files, how you structure things, etc) is entirely up to you! The only things you must keep in place are what is already listed in the **Structure** section below.

## Structure

* `documents`: Contains folders for both of your draft and final submissions. README.md files are included in both.
* `run.py`: General wrapper script that you can choose to use or not. Only requirement is that you implement the one function inside of there for the auto-checks.
* `test.py`: Run this file to confirm that your submission has everything required. This essentially just means it will check for the right files and sufficient theory size.

## Running With Docker

By far the most reliable way to get things running is with [Docker](https://www.docker.com). This section runs through the steps and extra tips to running with Docker. You can remove this section for your final submission, and replace it with a section on how to run your project.

1. First, download Docker https://www.docker.com/get-started

2. Navigate to your project folder on the command line.

3. We first have to build the course image. To do so use the command:
`docker build -t cisc204 .`

4. Now that we have the image we can run the image as a container by using the command: `docker run -it -v $(pwd):/PROJECT cisc204 /bin/bash`

    `$(pwd)` will be the current path to the folder and will link to the container

    `/PROJECT` is the folder in the container that will be tied to your local directory

5. From there the two folders should be connected, everything you do in one automatically updates in the other. For the project you will write the code in your local directory and then run it through the docker command line. A quick test to see if they're working is to create a file in the folder on your computer then use the terminal to see if it also shows up in the docker container.

### Mac Users w/ M1 Chips

If you happen to be building and running things on a Mac with an M1 chip, then you will likely need to add the following parameter to both the build and run scripts:

```
--platform linux/x86_64
```

For example, the build command would become:

```
docker build --platform linux/x86_64 -t cisc204 .
```

### Mount on Different OS'

In the run script above, the `-v $(pwd):/PROJECT` is used to mount the current directory to the container. If you are using a different OS, you may need to change this to the following:

- Windows PowerShell: `-v ${PWD}:/PROJECT`
- Windows CMD: `-v %cd%:/PROJECT`
- Mac: `-v $(pwd):/PROJECT`

Finally, if you are in a folder with a bunch of spaces in the absolute path, then it will break things unless you "quote" the current directory like this (e.g., on Windows CMD):

```
docker run -it -v "%cd%":/PROJECT cisc204
```




Sure! Here's a **README** template for the **"Treasure Land"** project. This document will provide an overview of the project, installation instructions, and how to use the provided scripts.

---

# Treasure Land

**Treasure Land** is an adventure-based logic puzzle game where players must navigate through various obstacles, solve puzzles, and find the hidden treasure. The game is built using logical propositions, constraints, and first-order logic to simulate player interactions with the environment and in-game elements like bridges, rivers, hazards, artifacts, and puzzles.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Game Description](#game-description)
3. [Getting Started](#getting-started)
4. [Game Logic and Constraints](#game-logic-and-constraints)
5. [Running the Project](#running-the-project)
6. [Testing](#testing)
7. [File Structure](#file-structure)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview

**Treasure Land** is a strategic game where the goal is to find the treasure by overcoming obstacles such as rivers, marshes, and hazards. The game logic is based on logical propositions, constraints, and interactions between various in-game elements, like clues, puzzles, and artifacts.

This project uses **first-order logic** to model player actions and interactions with the environment, requiring players to solve puzzles, avoid hazards, and find clues to reach the treasure.

---

## Game Description

In **Treasure Land**, players navigate through locations containing various elements:
- **Bridge**: Allows crossing of rivers.
- **River**: Blocks access to locations unless a bridge is present.
- **Puzzle**: Locations that contain puzzles that must be solved to progress.
- **Hazard**: Dangerous elements that prevent finding the treasure unless avoided with artifacts.
- **Artifact**: An item that helps the player avoid hazards.
- **Clue**: Points to locations containing puzzles or treasures.
- **Treasure**: The ultimate goal of the game.

The game is structured around **logical propositions**:
- **Bridge(x)**: A bridge exists at location `x`.
- **River(x)**: A river exists at location `x`.
- **Puzzle(x)**: A puzzle exists at location `x`.
- **Hazard(x)**: A hazard exists at location `x`.
- **Artifact(x)**: An artifact exists at location `x`.
- **Clue(x, y)**: A clue exists at location `x`, leading to location `y`.
- **Treasure(x)**: The treasure is located at `x`.

### Key Game Mechanics
- **Bridges** allow crossing **rivers**, which otherwise block access to locations.
- **Puzzles** need to be solved, and once solved, they provide access to the **treasure**.
- **Artifacts** help players avoid **hazards**.
- **Clues** help players navigate to the correct puzzle locations.

---

## Getting Started

### Prerequisites
To run the project, you'll need:
- **Python 3.x** (preferably 3.7+)
- **NNF (NextSAT) library**: For solving logical expressions.

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/treasure-land.git
    cd treasure-land
    ```

2. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure you have the necessary files**:
    - Make sure the `proofs.jp`, `modelling_report.docx`, and other related files are in place as described in the project's documentation.

---

## Game Logic and Constraints

The game utilizes **first-order logic** (FOL) to model constraints and propositions. Some key constraints in the game include:
- **River and Bridge**: If there is a river and no bridge, the player cannot access the clue at that location.
  - `River(x) ∧ ¬Bridge(x) → ¬Clue(x)`
  
- **Puzzle and Treasure**: Solving the puzzle (and avoiding hazards) leads to the treasure.
  - `Puzzle(x) ∧ ¬Hazard(x) → Treasure(x)`

- **Artifact Usage**: Artifacts allow players to avoid hazards, enabling them to proceed through the game.
  - `Artifact(x) → ¬Hazard(x)`

- **Cooperation**: Players must cooperate to defeat certain monsters (e.g., `Zephyr`) and earn respawns.

---

## Running the Project

### Main Game Script: `run.py`
You can run the game logic by calling the `optimal_treasure_strategy()` function, which will set up the logical propositions and constraints.

```bash
python run.py
```

### Testing the Theory: `test.py`
To ensure the logical consistency of the game and validate that all constraints are correctly set, you can run the `test.py` script. This script checks that the number of variables and constraints meet the expected levels and verifies that the logical theory is consistent.

To run the tests:
```bash
python3 test.py draft   # For draft version
python3 test.py final   # For final version
```

---

## Testing

### Testing the Theory

The `test.py` script performs a series of tests on the game theory to ensure that:
- The game has enough variables and constraints.
- The theory is logically inconsistent (no solutions should exist).
- The theory is negated correctly (ensuring no solutions exist when negated).

### File Checks

The `test.py` script also verifies the existence of the following files:
- `proofs.jp`
- `modelling_report.docx` or `modelling_report.pptx`
- `report.txt` and `report.pdf`

These files should be located in the `documents/{draft|final}` folder.

---

## File Structure

```
treasure-land/
│
├── documents/
│   ├── draft/
│   │   ├── proofs.jp
│   │   ├── modelling_report.docx
│   │   └── report.pdf
│   └── final/
│       ├── proofs.jp
│       ├── modelling_report.pptx
│       └── report.txt
│
├── run.py              # Main game logic
├── test.py             # Testing script for game theory
├── requirements.txt    # Python dependencies
├── README.md           # This file
```

---

## Contributing

We welcome contributions to improve the project. If you want to contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/branch-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/branch-name`).
5. Create a new pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust this **README** based on your project requirements, especially if there are any specific installation or usage instructions relevant to your environment. Let me know if you need further modifications!