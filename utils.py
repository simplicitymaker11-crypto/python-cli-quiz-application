import json
from quiz_maintenance import clear_screen


def load_question(file_path):
    try:
        with open(file_path , "r") as file:
       
          data=json.load(file)
          if not data:
              print("File is empty! ... ")
              input("Press enter to continue ==>> ")
              clear_screen()
          else:
             return data["questions"]
             

    except FileNotFoundError:
       print("File Not Found! ... ") 
       input("Press enter to continue ==>> ")
       clear_screen()  
       return [] 
      
    except json.JSONDecodeError:
       print("Invalid JSON format! ... ")   
       input("Press enter to continue ==>> ")
       clear_screen()
       return []   
