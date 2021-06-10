from tkinter import *
from numpy.random import shuffle
from os import makedirs
from json import dump

name_list = []
score = 0

qanswers = {
    1: [
        "How is your school learning so far?",
        'Fantastic', 'Good',
        'Bad'],
    2: [
        "What do you think of your subject teachers?",
        'Awesome', 'It is fine',
        'The teacher needs to support more students', 'Others',
    ],
    3: ["What thing does the school need to improve?" ,
        'School facilities and equipment', 'School environment', 'Others', ],

    4: ["How is your friend or your classmate at school?:", 'Great', 'Not bad',
        'I do not have friends at school', 'Other', ],

    5: ["Do you think is hard for you to learn the subject you choose this year?:", 'No', 'A' ' bit', 'Yes', 'Other', ],


    6: ["Does the school private you a good equipment for your study?", 'Yes', 'No', 'Not bad', ],

    7: ["Is this quiz  enough for you to give the school feedback?", 'Yes', 'Just a few things', 'No'],
}


class Quizstarter:
    def __init__(self, parent):
        self.data={}
        self.parent = parent
        self.name = None
        self.number = 0

        self.name_page()

    def name_page(self):
        background_color = "OldLace"
        color_for_button = "#e3edf6"
        # frame setup
        self.quiz_frame = Frame(self.parent,
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
                                font=("Indie Flower", "17"),
                                bg=background_color)
        self.user_label.grid(row=2, padx=30, pady=20)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=3, padx=20, pady=20)

        self.continue_button = Button(self.quiz_frame,
                                      text='Continue',
                                      font=("Indie Flower", "13", "bold"),
                                      bg=color_for_button,
                                      command=self.name_collection)
        self.continue_button.grid(row=4, padx=20, pady=25)

    def end_page(self):
        background_color = "OldLace"
        # frame setup
        self.quiz_frame = Frame(self.parent,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()
        self.handing_label = Label(self.quiz_frame,
                                   text="Thanks for your responses",
                                   bg=background_color)
        self.handing_label.grid(row=0, padx=20)

        self.continue_button = Button(self.quiz_frame,
                                      text='Exit',
                                      font=("Helvetica", "13", "bold"),
                                      bg=color_for_button,
                                      command=exit)
        self.continue_button.grid(row=4, padx=20, pady=25)

    def name_collection(self):
        self.name = self.entry_box.get()
        if self.name.replace(' ','') == '':
            self.quiz_frame.destroy()
            self.name_page()
            background_color = "OldLace"
            self.warning_label = Label(self.quiz_frame,
                                text="Please enter your name:",
                                font=("Indie Flower", "15"), fg="Red",
                                bg=background_color)
            self.warning_label.grid(row=2, padx=20, pady=20)

          
        else:
            self.new_question()

    def new_question(self):
        self.quiz_frame.destroy()
        self.number += 1
        if self.number > len(qanswers):
            dump(self.data, open(f'data/{self.name}.json','w'))
            self.end_page()
        background_color = "OldLace"
        color_for_button = "#e3edf6"
        # frame setup
        self.quiz_frame = Frame(root,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()

        self.question_label = Label(self.quiz_frame, text=qanswers[self.number][0], font=("Tw Cen MT", "16"),
                                    bg=background_color)
        self.question_label.grid(row=1, padx=10, pady=10)

        self.var1 = IntVar()

        self.rb1 = Radiobutton(self.quiz_frame, text=qanswers[self.number][1], font=("Helvetica", "12"),
                               bg=background_color,
                               value=1, padx=10, pady=10, variable=self.var1, indicator=0, background=color_for_button)
        self.rb1.grid(row=2, sticky=W)

        self.rb2 = Radiobutton(self.quiz_frame, text=qanswers[self.number][2], font=("Helvetica", "12"),
                               bg=background_color,
                               value=2, padx=10, pady=10, variable=self.var1, indicator=0, background=color_for_button)
        self.rb2.grid(row=3, sticky=W)

        self.rb3 = Radiobutton(self.quiz_frame, text=qanswers[self.number][3], font=("Helvetica", "12"),
                               bg=background_color,
                               value=3, padx=10, pady=10, variable=self.var1, indicator=0, background=color_for_button)
        self.rb3.grid(row=4, sticky=W)

        self.quiz_instance = Button(self.quiz_frame, text="Confirm", font=("Helvetica", "13", "bold"),
                                    bg=color_for_button, command=self.test_progress)
        self.quiz_instance.grid(row=7, padx=5, pady=5)

    def qsetup(self):
        self.var1.set(0)
        self.question_label.config(text=qanswers[self.number][0])
        self.rb1.config(text=qanswers[self.number][1])
        self.rb2.config(text=qanswers[self.number][2])
        self.rb3.config(text=qanswers[self.number][3])

    def test_progress(self):
        choice = self.var1.get()
        self.quiz_instance.config(text="Confirm")
        self.data[qanswers[self.number][0]]=qanswers[self.number][choice]
        self.new_question()


root = Tk()
root.title("Quiz")
makedirs('data',exist_ok=True)
quiz_instance = Quizstarter(root)
root.mainloop()  # Keep showing the window until we close it.
