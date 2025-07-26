from random import choice
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import cv2


def computerShoots( ):
  hands = ["Rock", "Paper", "Scissors"]
  return (choice(hands))

#get player's data
def determineHand(filename):
   # recognize player's data
  np.set_printoptions(suppress=True)

  model = load_model("keras_model.h5", compile=False)

  class_names = open("labels.txt", "r").readlines()
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  image = Image.open(filename).convert("RGB")
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  image_array = np.asarray(image)

  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  data[0] = normalized_image_array

  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]
  return class_name[2:]

def playerShoots():
 hand = input("Enter your play (Rock, Paper, Scissors): ")
 return determineHand(hand + ".jpeg")

def determineWhoWins(x, y):
 #Compare scissors play
  if x == "Scissors":
    if y == "Scissors":
     return "It's a draw!"
    elif y == "Rock":
      return "Player Wins!"
    else:
      return "Computer Wins!"

    # Compare rock play
  if x == "Rock":
    if y == "Rock":
     return "It's a draw!"
    elif y == "Paper":
      return "Player Wins!"
    else:
      return "Computer Wins!"

    # Compare paper play
  if x == "Paper":
    if y == "Paper":
     return "It's a draw!"
    elif y == "Scissors":
      return "Player Wins!"
    else:
      return "Computer Wins!"


computerScore = 0
playerScore = 0
while True:
  print()
  print("Lets Play Rock Paper Scissors!")

  print("Computer score: " + str(computerScore))
  print("Player score: " + str(playerScore))
  x = computerShoots( )
  y = playerShoots( )
  print("Computer plays..." + x)
  print("Your play..." + y)
  winner = determineWhoWins(x, y)
  print(winner)

  #tally score
  if winner ==  "Computer Wins!":
    #print("Computer Wins!")
    computerScore += 1
  elif winner == "Player Wins!":
    #print("Player Wins!")
    playerScore += 1
  else:
    #print("Its a Draw!")
    computerScore += 1
    playerScore += 1

