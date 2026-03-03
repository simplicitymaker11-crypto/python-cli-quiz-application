# Questions displaying
'''Responsibilities:

1. Store question, options, answer, difficulty

2. Assign points dynamically based on difficulty

3. Provide method is_correct(user_answer) to check answers

End result:
You can create a Question object and it knows everything about itself, including points.'''

class Question:
    def __init__(self,question,options,answer,difficulty):

        self.question=question
        self.options=options
        self.answer=answer
        self.difficulty=difficulty
        self.points=self.assign_points()
        


    def display_question(self,index):
        
        print(f"-----------------------------------------")
        print(f"{index}. {self.question}")
        print(f"-----------------------------------------\n")
        for i,option in enumerate  (self.options,start=1):
             print(f"{i}. {option}")
        print(f"\n-----------------------------------------")

       


    def assign_points(self):

        if self.difficulty.lower() == "easy":
            return 1
        elif self.difficulty.lower() == "medium":
            return 3
        elif self.difficulty.lower() == "hard":
            return 5


    def is_correct(self,user_answer):
       
        
        return user_answer == self.answer
        
    
    


  