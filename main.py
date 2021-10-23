import random

#default diffilculty global var
EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
  level = input("Choose diffilculty: Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL


#check if the given number is accurate
def check_answer(guess, answer, attempts):
  """checks answer against guess. returns the number of turns/attempts remaining"""
  if guess > answer:
    print("Too high.")
    return attempts - 1
  elif guess < answer:
    print("Too low.")
    return attempts - 1
  else:
    print(f"You've done it! It's {answer}.")

def game():
  #choose number between 1-100
  print("Guess a number!")
  print("What is the number between 1 and 100?")
  answer = random.randint(1, 100)
  print(f"TEST: Correct answer: {answer}")

  #choosing the diffilculty
  attempts = set_difficulty()
  

  guess = 0
  while guess != answer:
    print(f"You have {attempts} attempts remaining to guess the number.")

    #let make a choice 
    guess = int(input("Guess a number: "))

    #follow the number of turns/attempts and reduce it by 1 if guess went wrong
    attempts = check_answer(guess, answer, attempts)
    if attempts == 0:
      print("You lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()
