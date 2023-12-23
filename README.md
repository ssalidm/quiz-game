# Quiz Game

## Overview
Welcome to the Quiz Game! This simple console-based quiz application allows users to test their knowledge in different categories, including Geography, Computer Science, Music, and Sports.

## Getting Started
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/ssalidm/quiz-game.git

    cd quiz-game
    ```

2. Run the `main.py` script:
    ```bash
    python main.py
    ```

3. Follow the on-screen instructions to pick a category and answer the questions.

## Categories
- Geography
- Computer Science
- Music
- Sports

## How to Play
1. Launch the game by running the `main.py` script.
2. Choose a category by entering the corresponding category number:
    - 1- Geography
    - 2- Computer Science
    - 3- Music
    - 4- Sports
3. Answer the questions presented by typing your response.
4. Once all questions are answered, the game will display your results.

## Code Structure
The codebase is organized into several files:
- `question_model.py`: Defines the `Question` class.
- `data.py`: Contains question data for each category.
- `quiz_brain.py`: Implements the `QuizBrain` class, which manages the quiz logic.
- `main.py`: The main script to run the quiz game.

## Sample Execution
```bash
------------------------------
Welcome to the Quiz Game!
------------------------------

Pick a category number:
1- Geography, 2- Computer Science, 3- Music, 4- Sports: 2

You picked Computer Science

Quest
```

## License
This project is licensed under the [MIT License](https://github.com/ssalidm/quiz-game/blob/main/LICENSE).

## Acknowledgments
This quiz game was created as a simple project for learning and entertainment purposes.

Feel free to customize and extend the game as needed. Happy quizzing!
