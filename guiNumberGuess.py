from logging import root
from string import whitespace
from tkinter import*
import time
import random

root = Tk()
root.title("Guess the number")
root.geometry("500x500")

num_label = Label(root, text = "3 Tries to guess a number\nBetween 1 and 10", font=("Brush Script MT", 24))
num_label.pack(pady=20)

def guesser():
    if guess_box.get().isdigit():
        global tries
        tries = tries -1

        if tries != 0:
            # label reset
            num_label.config(text="Pick a number\nBetween 1 and 10")
            diff = abs(num - int(guess_box.get()))

            if (int(guess_box.get())==num):
                bc = "SystemButtonFace"
                num_label.config(text="Correct!") 
            elif diff == 5:
                bc = "white"
            elif diff < 5:
                bc = f"#ff{diff}{diff}{diff}{diff}"
            else:
                bc = f"#{diff}{diff}{diff}{diff}ff"
            
            root.config(bg=bc)
            num_label.config(bg = bc)
        else:
            guess_box.delete(0,END)
            num_label.config(text="Out of tries!")
            time.sleep(2)
            rando()

    else:
        guess_box.delete(0,END)
        num_label.config(text="Please enter a number!")

def rando():
    global num
    global tries
    tries = 3
    num = random.randint(1,10)
    guess_box.delete(0,END)
    num_label.config(bg = "SystemButtonFace" , text = "3 Tries to guess a number\nBetween 1 and 10", font=("Brush Script MT", 24))
    root.config(bg = "SystemButtonFace")
    

guess_box = Entry(root, font = ("Helvetica", 100), width=2)
guess_box.pack(pady=20)

guess_button = Button(root, text = "Submit", command=guesser)
guess_button.pack(pady=20)

rand_button = Button(root, text = "New Number", command=rando)
rand_button.pack(pady=20)

rando()
root.mainloop()
