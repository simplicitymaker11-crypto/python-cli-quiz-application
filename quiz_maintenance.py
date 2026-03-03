from question import Question
import os



def clear_screen():
    if os.name == "nt":     
        os.system("cls")


class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.total_question=len(self.questions)
        
    def run(self):
        for index,question in enumerate(self.questions,start=1):
            

            while True:

                try:
                 question.display_question(index)
                 user_input=int(input("\nSelect your answer (0 to exit): "))
                 if user_input==0:
                     clear_screen()
                     print("You are exitting quiz ... ")
                     input("\nPress enter to continue ==>> ")
                     clear_screen()
                     return                   

                 if user_input < 1 or user_input > len(question.options):
                     clear_screen()
                     print("Invalid selection!...\n")
                     input("Press enter to continue ==>> ")
                     clear_screen()
                     continue
                 
                 clear_screen()
                 break

                except ValueError:

                    clear_screen()
                    print("Enter the correct type! ...\n")
                    input("Press enter to continue ==>> ")
                    clear_screen()


            
            if question.is_correct(user_input):
                
                self.score+=question.points
                if(index==self.total_question):
                    print(f"-----------------------------")
                    print(f"correct Anwswer\n\nScore: {self.score}\n\nQuiz Finished .......") 
                    print(f"-----------------------------")
                    input("\n\nPress enter to continue ==>> ")  
                    clear_screen()


                    while True:
                      repeat=int(input("1. Repeat\n2. Exit\n\nEnter you Choice: "))
                      clear_screen()

                      try: 
                        if repeat==1: 
                          self.run()
    
                        elif repeat==2: 
                          input("Press enter to continue ==>> ") 
                          clear_screen()
                          return
                        
                      except ValueError:  
                          print("Invalid Choice! ")
                          input("\n\nPress enter to continue ==>> ") 
                          clear_screen()

                else:    
                    print(f"-----------------------------") 
                    print(f"correct Anwswer\n\nScore: {self.score}")
                    print(f"-----------------------------")    
                    input("\n\nPress enter to continue ==>> ") 
                    clear_screen()

            else:

                if(index==self.total_question):
                    print(f"-----------------------------") 
                    print(f"Incorrect Anwswer\n\nScore: {self.score}\n\nQuiz Finished .......")  
                    print(f"-----------------------------")  

                    
                    input("\n\nPress enter to continue ==>> ") 
                    clear_screen()
                    
                    while True:
                      repeat=int(input("1. Repeat\n2. Exit\n\nEnter you Choice: "))
                      clear_screen()

                      try: 
                        if repeat==1: 
                          self.run()
    
                        elif repeat==2 : 
                          input("Press enter to continue ==>> ") 
                          clear_screen()
                          return
                        
                      except ValueError:  
                          print("Invalid Choice! ")
                          input("\n\nPress enter to continue ==>> ") 
                          clear_screen()

                else: 
                    print(f"-----------------------------")    
                    print(f"Incorrect Anwswer!\n\nCorrect answer : {question.options[question.answer-1]}\n\nScore:  {self.score} ")
                    print(f"-----------------------------") 
                    input("\n\nPress enter to exit ==>> ") 
                    clear_screen()


            clear_screen()
            
            