from utils import load_question
from question import Question
from quiz_maintenance import Quiz,clear_screen
import os


categories = {

    "General Knowledge": "general_knowledge.json",
    "Math": "math.json",
    "Physics": "physics.json",
    "Chemistry": "chemistry.json",
    "Biology": "biology.json",
    "Computer": "computer.json",
    "Islamic": "islamic.json",
    "Politics": "politics.json"
    
}

while True:
      
      print(f"\t---- Categories ----\n")
      for i,category in enumerate(categories.keys(),start=1):
            print(f"{i}. {category}")
      choice=(input("\nSelect a category (0 to exit): "))   
      if(choice==''):
            clear_screen()
            print("Invalid Selection!...")   
            input("\nPress enter to continue ==>> ")
            clear_screen()
            continue   
      else:
           choice=int(choice) 


      if choice==0:
            clear_screen()
            print("You are exiting the quiz app....")   
            input("\nPress enter to continue ==>> ")
            clear_screen()
            break

      elif choice not in range(1, len(categories) + 1):
            clear_screen()
            print("Invalid Selection!...")
            input("\nPress enter to continue ==>> ")
            clear_screen()
            continue

      

      clear_screen()

      filename=list(categories.values())[choice-1]
      data = load_question(filename)
      
      questions=[]
      for item in data:
            q=Question(item["question"],item["options"],item["answer"],item["difficulty"])
            questions.append(q) 
      
      
      quiz=Quiz(questions)
      quiz.run()



##'''Responsibilities:
##
##Import Quiz class and load_questions()
##
##Run the program
##
##Handle any top-level errors
##
##Optional: welcome message, instructions
##
##End result:
##Clean, readable, and minimal code in main.py.'''
