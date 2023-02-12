import random

##
# Program that given questions will ask the user questions to help them study
##

# Loads questions from text file
def loadQuestions(file_name):
  try:
    # Opens files and reads lines
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()

    # Splits questions and anwsers then returns the list of questions and anwsers
    questions = [i.strip().split(" A: ") for i in lines]
    return questions

  except FileNotFoundError:
    print("Error: File not found.")
    return []

def main():
  # Gets name of file with questions
  file_name = input("Enter name of file containing practice questions: ")
  
  correct = 0
  totalQuestionsAsked = 0

  # Loads all questions
  questions = loadQuestions(file_name)
  
  if not questions:
    print("No practice questions found.")
    return

  while len(questions) > 0:

    totalQuestionsAsked += 1

    # Gets random question from list of questions
    random_question_index = random.randint(0, len(questions)-1)
    random_question = questions[random_question_index]
    
    print(random_question[0])
    ans = input("Enter your answer to the question: ")

    # Checks if answer is correct if so deletes question
    if ans == random_question[1]:
      print("Correct!")
      correct += 1
      del questions[random_question_index]
    else:
      print("Incorrect.")
    
    if len(questions) <= 0:
      print("You have completed all of the practice questions.")
      break

    continueQuestions = input("Do you want to continue? (yes/no): ").lower()
    
    if continueQuestions == "no":
      break
  
    
  correct_percent = "%.2f" % ((correct/totalQuestionsAsked)*100)
  print(f"The percentage of correct answers is: {correct_percent}%")
  
    
if __name__ == "__main__":
  main()