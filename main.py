# I create a directory
from os import makedirs
# Save the dictionary as json
from json import dump
# For UI
from tkinter import *

# Create question dictionary to give the question to user
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

    6: ["Does the school private you a good equipment for your study?", 'Yes', 'No', 'Not bad', ],

    7: ["Is this quiz  enough for you to give the school feedback?", 'Yes', 'Just a few things', 'No'],
}


# Create a class for user interface
class Quizstarter:
    def __init__(self, parent):
        self.quiz_frame = Frame()
        self.parent = parent
        self.name = None
        self.number = 0
        self.data = {}

        self.name_page()

    # Define a function for getting the user name
    def name_page(self, check=False, message=None):
        # The check val is for does user enter any thing if not it will be True
        # The message val is for giving the message to the user if needed

        self.quiz_frame.destroy()

        # Define the color in used.
        background_color = "#f4eee2"
        color_for_button = "#e3edf6"

        # Set up a frame for the name page
        self.quiz_frame = Frame(
            self.parent,
            bg=background_color,
            padx=100,
            pady=100
        )
        self.quiz_frame.grid()

        # Create a label for handing in frame
        Label(
            self.quiz_frame,
            text="Welcome to the Quiz",
            bg=background_color
        ).grid(row=0, padx=30)

        # If check is True show error message in frame
        if check:
            Label(
                self.quiz_frame,
                text="Please enter your name:",
                font=("Indie Flower", "17"), fg="Red",
                bg=background_color
            ).grid(row=2, padx=30, pady=20)
        # if check is not True show normal message in frame
        else:
            Label(
                self.quiz_frame,
                text="Enter your name:",
                font=("Indie Flower", "17"),
                bg=background_color
            ).grid(row=2, padx=30, pady=20)

        # Create an entry box for the user to input their name in frame
        self.entry_box = Entry(self.quiz_frame, textvariable=self.name)
        self.entry_box.grid(row=3, padx=30, pady=20)

        # Defind function for key press event
        def keypress(event):
            # if key press enter run self.name_collection
            if event.keycode == 13:
                self.name_collection()

        self.entry_box.bind('<Key>', keypress)

        # Create button for continue in frame
        Button(
            self.quiz_frame,
            text='Continue',
            font=("Indie Flower", "13", "bold"),
            bg=color_for_button,
            command=self.name_collection  # When press run self.name_collection
        ).grid(row=4, padx=20, pady=25)

        # if message is giveing show message
        if message is not None:
            Label(
                self.quiz_frame,
                text=message,
                font=("Indie Flower", "17"),
                fg='red',
                bg=background_color
            ).grid(row=5)

    # Define a function for the end page will show after user answer all the qanswers
    def end_page(self):
        background_color = "OldLace"
        color_for_button = "#e3edf6"

        # Set up a frame for the end page
        self.quiz_frame = Frame(
            self.parent,
            bg=background_color,
            padx=100,
            pady=100
        )
        self.quiz_frame.grid()

        # Create a label for handing in frame
        Label(
            self.quiz_frame,
            text="Thanks for your responses",
            bg=background_color
        ).grid(row=0, padx=20)

        # Create button for exit in frame
        Button(
            self.quiz_frame,
            text='Exit',
            font=("Helvetica", "13", "bold"),
            bg=color_for_button,
            command=exit  # When press exit the pargam
        ).grid(row=4, padx=20, pady=25)

    # Define a function for name check
    def name_collection(self):
        # Get val from entry box
        self.name = self.entry_box.get()
        # Check is it a blank if True show the name page with the error message
        if self.name.replace(' ', '') == '':
            self.name_page(True)
        # Check is it to long if True show the name page with the message
        elif len(self.name) > 10:
            self.name_page(message='Do not enter more than 10 characters.')
        # Check is it to long if True show the name page with the message
        else:
            # Start question
            self.question()

    # Define function for question page
    def question(self, check=False):
        if not check:
            self.number += 1

        self.quiz_frame.destroy()
        if self.number > len(qanswers):
            dump(self.data, open(f'data/{self.name}.json', 'w'))
            self.end_page()
            return
        background_color = "OldLace"
        color_for_button = "#e3edf6"

        # Set up a frame for the question page
        self.quiz_frame = Frame(root,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()

        # Create a label for question in frame
        Label(
            self.quiz_frame,
            text=qanswers[self.number][0],
            font=("Tw Cen MT", "16"),
            bg=background_color
        ).grid(row=1, padx=10, pady=10)

        i = 0
        # Create options for question in frame
        self.var = IntVar()
        for i in range(1, len(qanswers[self.number])):
            Radiobutton(
                self.quiz_frame,
                text=qanswers[self.number][i],
                font=("Helvetica", "12"),
                bg=background_color,
                value=i,
                padx=10,
                pady=10,
                variable=self.var,
                indicator=0,
                background=color_for_button
            ).grid(row=i + 1, sticky='w')

        # Create a button for confirm in frame
        Button(
            self.quiz_frame,
            text="Confirm",
            font=("Helvetica", "13", "bold"),
            bg=color_for_button,
            command=self.answer  # When press run self.answer
        ).grid(row=2 + i, padx=5, pady=5)

        # Defind a function for back
        def back():
            self.number -= 2
            self.question()

        if self.number > 1:
            Button(
                self.quiz_frame,
                text="Back",
                font=("Helvetica", "13", "bold"),
                                 bg=color_for_button,
                command=back # When press run back
            ).grid(row=8, padx=5, pady=5)

        if check:
            if self.number > 1:
                Label(
                    self.quiz_frame,
                    text="Place chose one",
                    font=("Tw Cen MT", "16"),
                    bg=background_color
                ).grid(row=10, padx=10, pady=10)
            else:
                Label(
                    self.quiz_frame,
                    text="Place choose one",
                    font=("Tw Cen MT", "16"),
                    bg=background_color
                ).grid(row=8, padx=10, pady=10)
    # Crate variable that can let the question page keep apprearing the questions.
    def answer(self):
        choice = self.var.get()
        self.data[qanswers[self.number][0]] = qanswers[self.number][choice]
        self.question(choice == 0)


root = Tk() # Make the window as a root.
root.title("Quiz") # Give the title of the root.
makedirs('data', exist_ok=True) #Create a data
quiz_instance = Quizstarter(root)
root.mainloop()  # Keep showing the window until we close it.