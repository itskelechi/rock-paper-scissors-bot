# ✊🖐✌ Rock Paper Scissors AI

A computer vision-based Rock, Paper, Scissors game that lets you battle an AI!
Your moves are detected using a pre-trained Keras model on images of your hand gestures.
## 📸 Gameplay Concept

    You provide an image (Rock.jpeg, Paper.jpeg, or Scissors.jpeg) of your hand.

    The AI loads a trained Keras model to recognize your gesture.

    The computer randomly picks its move.

    The winner is decided based on classic Rock Paper Scissors logic.

    First to reach a higher score? Bragging rights are yours.

## 🔧 Setup Instructions
#### 🐍 Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

####  🧠 Dependencies

Install required Python packages by running:

pip install tensorflow pillow numpy opencv-python

    ⚠️ This script uses Keras (bundled with TensorFlow), so installing tensorflow covers it.

## 📁 Project Structure

rock-paper-scissors-ai/
├── keras_model.h5       # Your trained model file
├── labels.txt           # Labels that match model outputs
├── Rock.jpeg            # Example input image
├── Paper.jpeg
├── Scissors.jpeg
├── game.py              # Main Python script (the one in this README)
└── README.md            # You're reading it!

## ▶️ How to Run the Game

    Prepare your input images:

        Take pictures of your hand in "Rock", "Paper", and "Scissors" poses.

        Save them in .jpeg format with exact filenames:

    Rock.jpeg
    Paper.jpeg
    Scissors.jpeg

## Run the script:

python RPS.py

Play the game:

    When prompted:

        Enter your play (Rock, Paper, Scissors):

        Type your move exactly (e.g., Rock), and make sure the corresponding .jpeg file is in the same folder.

    Watch the AI respond and scores tally up!

🤖 Example Interaction

Lets Play Rock Paper Scissors!
Computer score: 1
Player score: 2

Enter your play (Rock, Paper, Scissors): Scissors
Computer plays...Paper
Your play...Scissors
Player Wins!

## 💡 Model Notes

    keras_model.h5 must be trained using hand gesture images and saved using Teachable Machine or a custom CNN.

    labels.txt should contain output class names like:

    0 Rock
    1 Paper
    2 Scissors

## 🛠️ Future Enhancements (Ideas!)

    Add a webcam-based live detection instead of static .jpeg files

    Build a GUI using tkinter or pygame

    Add sounds, animations, or real-time scoring graphs

    Multiplayer mode?

## 🧠 Credits

Project by Kelechi with help from Keras, TensorFlow, and your glorious hands.
📜 License

MIT License — use it, remix it, just don’t let the AI win all the time 😉