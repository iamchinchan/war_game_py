---

# War Card Game (Python Edition)

A fully automated simulation of the classic "War" card game built with Python. This project focuses on **Object-Oriented Programming (OOP)** and clean logic to handle complex card game rules.

## 🚀 What I Built

I created a modular game engine where two players (Jatin and Shiv) battle until one runs out of cards. The project is split into different files to keep the code organized and easy to manage.

### Key Technical Features:

- **Object-Oriented Design**: Used classes for `Card`, `Deck`, `Player`, and `Table` to represent real-world objects.
- **FIFO Logic**: Implemented a "First-In-First-Out" system for the player's hand—cards are drawn from the top and won cards are added to the bottom.
- **Infinite Loop Prevention**: Added a shuffle feature to the "won cards" pile to prevent the game from getting stuck in a repeating cycle.
- **Clean Terminal UI**: The game provides clear, round-by-round updates on card counts and winners.

## 🧠 Game Logic

The game follows a unique **"Carry-over" War rule**:

1.  **Normal Round**: Each player draws one card. The highest card value wins the round and takes both cards.
2.  **The Tie (War)**: If the cards are equal, a "War" starts. Both players must place 3 additional cards face-down on the table.
3.  **The Decider**: The very next normal round determines who wins the entire pile. This "carry-over" makes the stakes much higher.
4.  **Shortage Rule**: If a player does not have enough cards to "pay" the 3-card War fee, they lose the game immediately.
5.  **Sudden Death**: If both players are low on cards during a tie, they draw single cards until someone wins or both run out.

## 📂 Project Structure

- `main.py`: The main game engine and loop.
- `player.py`: Manages player names and their card hands.
- `table.py`: Acts as the referee, handles comparisons and the cards on the field.
- `deck.py` & `card.py`: Handles the creation and shuffling of the 52-card deck.
- `globals.py`: Stores card ranks, suits, and values (Ace is high!).

## 🎮 How to Play

1.  Ensure you have Python installed.
2.  Download all project files into one folder.
3.  Run the game via terminal:
    ```bash
    python main.py
    ```
4.  Follow the on-screen prompts to watch the battle and choose if you want to play again.

---

_Created as part of my Python learning journey, focusing on clean code and logical problem-solving._
