from tkinter import *
from random import *
def selected(player_chose):
    choices=['ROCK','PAPER','SCISSORS']
    computer_chose=choice(choices)
    frame1=Frame(win,bg="pink")
    frame1.grid(pady=5)
    player_choice=Label(frame1,text="player has choosen:",fg="#1E90FF",bg="pink",font=("Times New Roman",15,"bold"))
    player_choice.grid(pady=5)
    play1=Label(frame1,text=player_chose,fg="red",bg="pink",font=("Times New Roman",20,"bold"))
    play1.grid(pady=5)
    res=Label(frame1,text="computer has choosen:",fg="#1E90FF",bg="pink",font=("Times New Roman",15,"bold"))
    res.grid(pady=5)
    result_text1=Label(frame1,text=computer_chose,fg="red",bg="pink",font=("Times New Roman",20,"bold"))
    result_text1.grid(pady=5)
    

    if player_chose==computer_chose:
        
        result_text=Label(win,text="This is tie!",font=("Times New Roman",15,"bold"),fg="white",bg="pink")
        result_text.grid(pady=5)
    elif(player_chose =="ROCK" and computer_chose=="SCISSORS") or\
        (player_chose == "PAPER" and computer_chose == "ROCK") or \
        (player_chose == "SCISSORS" and computer_chose == "PAPER"):
          
            result_text=Label(frame1,text="you won!",font=("Times New Roman",15,"italic"),bg="pink")
            result_text.grid(pady=5)

    else:
        
        result_text=Label(frame1,text="computer won!",font=("Times New Roman",15,"italic"),bg="pink")
        result_text.grid(pady=5)

    play_Again=Button(frame1,text="PlayAgain",bg="green",fg="yellow",font=("Arial",13,"bold"),relief=RAISED,command=lambda:selected1())
    play_Again.grid(row=15,column=2,sticky=S)
    

def selected1():
     win.destroy()
     create_game()

def create_game():
    global win
    win=Tk()
    win.title("Rock Paper Scissors game")
    win.configure(background="pink")
    win.geometry("350x500")
    frame=Frame(win,bg="pink")
    frame.grid(pady=5)
    l1=Label(frame,text="Select your choice:",bg="pink",fg="red",font=("Arial",20,"bold"))
    l1.grid(pady=5)
    result_text=StringVar()
    rock=Button(frame,text="ROCK",bg="yellow",fg="red",command=lambda: selected("ROCK"),)
    rock.grid(pady=5)
    paper=Button(frame,text="PAPER",bg="yellow",fg="red",command=lambda: selected("PAPER"))
    paper.grid(pady=5)
    scissors=Button(frame,text="SCISSORS",bg="yellow",fg="red",command=lambda: selected("SCISSORS"))
    scissors.grid(pady=5)
    win.mainloop()

create_game()
