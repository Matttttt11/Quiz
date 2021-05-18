from tkinter import *
import random

global qanswers
name_list = []
score=0
asked = [1,2,3]

qanswers = {
    1: [
        "What is the best way to protect yourself at home if the earthquake happens?",
        'stay under the tables', 'run away from home',
        'just wait for someone to help', 'stay under the tables', 1],
    2: [
        "What is the best way to do if someone gets a heart attack on the street?",
        'Get away from him', 'Immediately call the ambulance',
        'Call the police', 'Immediately call the ambulance', 2
    ],
    3: ["The best way to remind someone who is being noisy in the library:" 'Tell him to shut up.', 'Give an eye contact with him', 'Use body structure to remind him', 'Use body structure to remind him', 3],

    4: ["What is one of the most popular languages in the world?:", '1' ,'2', '3','2',2],

    5: ["Something i like in this world:", '123', '123456','abc','abc',3],

    6: ["wo shi bu shi ni baba", 'shi', 'en', 'mei cuo', 'shi', 1],

    7: ["Is joel gay?",'Absolutely','Definitely','Obivously','Absolutely',1],

    8: ["123456",'4','5','6','4',1],

    9: ["q",'a','w','f','f',1],

    10: ["kk",'yrrt','sswvw','saerest','yrrt',1]


    
}


def randomiser():
    global qnum
    qnum = random.randint(1, 10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()







class Quizstarter:
    def __init__(self, parent):

        background_color = "OldLace"
          #frame setup
        self.quiz_frame = Frame(parent,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()
        self.handing_label = Label(self.quiz_frame,
                                     text="Welcome to the Quiz",
                                     bg=background_color)
        self.handing_label.grid(row=0, padx=20)

        self.user_label = Label(self.quiz_frame,
                                  text="Enter your name:",
                                  font=("Tw Cen MT", "16"),
                                  bg=background_color)
        self.user_label.grid(row=2, padx=30, pady=20)
        
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=3, padx=20, pady=20)
        
        self.continue_button = Button(self.quiz_frame,
                                        text='Continue',
                                        font=("Helvetica", "13", "bold"),
                                        bg="pink",
                                        command=self.name_collection)
        self.continue_button.grid(row=4, padx=20, pady=25)

    def name_collection(self):
        name = self.entry_box.get()
        name_list.append(name)
        self.quiz_frame.destroy()
        Quiz(root)


class Quiz:
  def __init__(self, parent):
          
    background_color = "OldLace"
                  #frame setup
    self.quiz_frame = Frame(parent,
                                        bg=background_color,
                                        padx=100,
                                        pady=100)
    self.quiz_frame.grid()  
                
    self.question_label=Label(self.quiz_frame, text=qanswers[qnum][0], font=("Tw Cen MT","16"),bg=background_color)
    self.question_label.grid(row=1,padx=10,pady=10)
        
    self.var1=IntVar()
        
    self.rb1= Radiobutton(self.quiz_frame, text=qanswers[qnum][1], font=("Helvetica","12"), bg=background_color,value=1, padx=10,pady=10,variable=self.var1, indicator = 0, background = "light blue")
    self.rb1.grid(row=2, sticky=W)
        
    self.rb2= Radiobutton(self.quiz_frame, text=qanswers[qnum][2], font=("Helvetica","12"), bg=background_color,value=2, padx=10,pady=10,variable=self.var1, indicator = 0, background = "light blue")
    self.rb2.grid(row=3, sticky=W)
        
    self.rb3= Radiobutton(self.quiz_frame, text=qanswers[qnum][3], font=("Helvetica","12"), bg=background_color,value=3, padx=10,pady=10,variable=self.var1, indicator = 0, background = "light blue")
    self.rb3.grid(row=4, sticky=W)
                
                
            
          
    self.quiz_instance=Button(self.quiz_frame, text="Confirm", font=("Helvetica","13","bold"), bg="SpringGreen3",command=self.test_progress)
    self.quiz_instance.grid(row=7,padx=5,pady=5)
          
    self.score_label=Label(self.quiz_frame, text="Score", font=("Tw Cen MT","16"), bg=background_color)
    self.score_label.grid(row=8,padx=10,pady=1)
        
  def qsetup(self):
    randomiser()
    self.var1.set(0)
    self.question_label.config(text=qanswers[qnum][0])
    self.rb1.config(text=qanswers[qnum][1])
    self.rb2.config(text=qanswers[qnum][2])
    self.rb3.config(text=qanswers[qnum][3])
                 
  def test_progress(self):
    global score
    scr_label=self.score_label
    choice=self.var1.get()
                      
    if len(asked)>9:
      if choice == qanswers[qnum][5]:
        score+=1
        scr_label.configure(text=score)
        self.quiz_instance.config(text="Confirm")
      else:
        score == score
        scr_label.configure(text="The correcr answer was :"+ qanswers[qnum][4])
        self.quiz_instance.config(text="Confirm")
    else:
      if choice == 0:
        self.quiz_instance.config(text="Try again, you did not selevt an option then sumbit again")
        choice=self.var1.get()
      else:
        if choice == qanswers[qnum][5]:
                            
          score += 1
          scr_label.configure(text=score)
          self.quiz_instance.config(text="Confirm")
          self.qsetup()
                              
        else:
          score == score
          scr_label.configure(text="The correcr answer was :"+ qanswers[qnum][4])
          self.quiz_instance.config(text="Confirm")
          self.qsetup()

randomiser()

if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    quiz_instance = Quizstarter(root)
    root.mainloop()  #Keep showing the window until we close it.