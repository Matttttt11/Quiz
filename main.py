from tkinter import *
from os import makedirs
from json import dump

name_list = []

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
    3: ["What thing does the school need to improve?",
        'School facilities and equipment', 'School environment', 'Others', ],

    4: ["How is your friend or your classmate at school?:", 'Great', 'Not bad',
        'I do not have friends at school', 'Other', ],

    5: ["Do you think is hard for you to learn the subject you choose this year?:", 'No', 'A' ' bit', 'Yes', 'Other', ],

    6: ["Does the school provide you a good equipment for your study?", 'Yes', 'No', 'Not bad', ],

    7: ["Is this quiz  enough for you to give the school feedback?", 'Yes', 'Just a few things', 'No'],
}


class Quizstarter:
    def __init__(self, parent):
        self.data = {}
        self.parent = parent
        self.name = None
        self.number = 0

        self.name_page()

    def name_page(self, check=False,message=''):
        background_color = "#f4eee2"
        color_for_button = "#e3edf6"
        # frame setup
        self.quiz_frame = Frame(self.parent,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()
        handing_label = Label(self.quiz_frame,
                              text="Welcome to the Quiz",
                              bg=background_color)
        handing_label.grid(row=0, padx=30)

        if check:
            user_label = Label(self.quiz_frame,
                               text="Please enter your name:",
                               font=("Indie Flower", "17"), fg="Red",
                               bg=background_color)
        else:
            user_label = Label(self.quiz_frame,
                               text="Enter your name:",
                               font=("Indie Flower", "17"),
                               bg=background_color)
        user_label.grid(row=2, padx=30, pady=20)

        self.entry_box = Entry(self.quiz_frame,textvariable=self.name)
        self.entry_box.grid(row=3, padx=30, pady=20)

        def keypass(event):
            if event.keycode == 13:
                self.name_collection()

        self.entry_box.bind('<Key>', keypass)

        continue_button = Button(self.quiz_frame,
                                 text='Continue',
                                 font=("Indie Flower", "13", "bold"),
                                 bg=color_for_button,
                                 command=self.name_collection)
        continue_button.grid(row=4, padx=20, pady=25)
        if message!='':
            message=Label(self.quiz_frame,
                  text=message,
                  font=("Indie Flower", "17"),
                  fg='red',
                  bg=background_color)
            message.grid(row=5)


    def end_page(self):
        background_color = "OldLace"
        color_for_button = "#e3edf6"
        # frame setup
        self.quiz_frame = Frame(self.parent,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()
        handing_label = Label(self.quiz_frame,
                              text="Thanks for your responses",
                              bg=background_color)
        handing_label.grid(row=0, padx=20)

        continue_button = Button(self.quiz_frame,
                                 text='Exit',
                                 font=("Helvetica", "13", "bold"),
                                 bg=color_for_button,
                                 command=exit)
        continue_button.grid(row=4, padx=20, pady=25)

    def name_collection(self):
        self.name = self.entry_box.get()
        if self.name.replace(' ', '') == '':
            self.quiz_frame.destroy()
            self.name_page(True)
        elif len(self.name)>10:
            self.quiz_frame.destroy()
            self.name_page(message='Do not enter more than 10 characters.')
        else:
            self.new_question()

    def new_question(self, check=False):
        if not check:
            self.number += 1

        self.quiz_frame.destroy()
        if self.number > len(qanswers):
            dump(self.data, open(f'data/{self.name}.json', 'w'))
            self.end_page()
            return
        background_color = "OldLace"
        color_for_button = "#e3edf6"
        # frame setup
        self.quiz_frame = Frame(root,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()

        question_label = Label(self.quiz_frame, text=qanswers[self.number][0], font=("Tw Cen MT", "16"),
                               bg=background_color)
        question_label.grid(row=1, padx=10, pady=10)

        self.var1 = IntVar()
        for i in range(1, len(qanswers[self.number])):
            rb = Radiobutton(self.quiz_frame, text=qanswers[self.number][i], font=("Helvetica", "12"),
                             bg=background_color,
                             value=i, padx=10, pady=10, variable=self.var1, indicator=0, background=color_for_button)
            rb.grid(row=i + 1, sticky=W)

        quiz_instance = Button(self.quiz_frame, text="Confirm", font=("Helvetica", "13", "bold"),
                               bg=color_for_button, command=self.test_progress)
        quiz_instance.grid(row=7, padx=5, pady=5)

        def back():
            self.number -= 2
            self.new_question()

        if self.number > 1:
            back_button = Button(self.quiz_frame, text="Back", font=("Helvetica", "13", "bold"),
                                 bg=color_for_button, command=back)
            back_button.grid(row=8, padx=5, pady=5)

        if check:
            label = Label(
                self.quiz_frame,
                text="Please choose one",
                font=("Tw Cen MT", "16"),
                bg=background_color
            )
            label.grid(row=10, padx=10, pady=10)

    def test_progress(self):
        choice = self.var1.get()
        self.data[qanswers[self.number][0]] = qanswers[self.number][choice]
        self.new_question(choice == 0)



root = Tk()
root.title("Quiz")
makedirs('data', exist_ok=True)
quiz_instance = Quizstarter(root)
root.mainloop()  # Keep showing the window until we close it.