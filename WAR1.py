from tkinter import *
from random import *
from PIL import Image, ImageTk

window = Tk()
window.title('WAR')
window.geometry("1920x1280")
window.configure(background="black")
f1 = Frame(window, bg="black")
f1.pack(pady=20)


p1_frame = LabelFrame(f1, text="Player 1", bd=0)
p1_frame.grid(row=0, column=0, padx=20, pady=20, ipadx=20)

p2_frame = LabelFrame(f1, text="Player 2", bd=0)
p2_frame.grid(row=1, column=0,pady=20, ipadx=20)



def resize(card):
    cardpic = Image.open(card)

    new_cardpic = cardpic.resize((150, 218))

    global card_img
    card_img = ImageTk.PhotoImage(new_cardpic)

    return card_img


def shuffle():
    s = ["dice", "clubs", "hearts", "spade"]
    val = range(1, 14)
    global deck
    deck = []
    for x in s:
        for y in val:
            deck.append(f'{y}_{x}')
    global p1,p2
    p1 = []
    p2 = []
    global pts_1, pts_2
    pts_1=0
    pts_2=0


    p1_card = choice(deck)
    deck.remove(p1_card)
    p1.append(p1_card)
    global p1_pic
    p1_pic = resize(f"C:/Users/Welcome/Desktop/card/{p1_card}.png")
    p1_lab.config(image=p1_pic)

    p2_card = choice(deck)
    deck.remove(p2_card)
    p2.append(p2_card)
    global p2_pic
    p2_pic = resize(f"C:/Users/Welcome/Desktop/card/{p2_card}.png")
    p2_lab.config(image=p2_pic)

    # player_label.config(text=card)
    score(p1_card,p2_card)


def deal():
    try:
        p1_card = choice(deck)
        deck.remove(p1_card)
        p1.append(p1_card)
        global p1_pic
        p1_pic = resize(f"C:/Users/Welcome/Desktop/card/{p1_card}.png")
        p1_lab.config(image=p1_pic)
        # dealer_label.config(text=card)

        p2_card = choice(deck)
        deck.remove(p2_card)
        p2.append(p2_card)
        global p2_pic
        p2_pic = resize(f"C:/Users/Welcome/Desktop/card/{p2_card}.png")
        p2_lab.config(image=p2_pic)
        # player_label.config(text=card)
        score(p1_card,p2_card)


    except:
        if pts_1>pts_2:
            victor.config(text=f"Player 1 has won the game with {pts_1} points!!")
        elif pts_2>pts_1:
            victor.config(text=f"Player 2 has won the game with {pts_2} points!!")
        else:
            victor.config(text="There is no winner, It's a draw.")






p1_lab = Label(p1_frame, text='')
p1_lab.pack(pady=20)

p2_lab = Label(p2_frame, text='')
p2_lab.pack(pady=20)
winner=Label(window, text="", fg="gold", bg="black")
winner.place(x=600, y=330)
victor=Label(window,text="", font=("Times","18","bold"), fg="gold", bg="black")
victor.place(x=750,y=100)
p1_count=Label(window, text="", font=("verdana","20", "bold"), fg="gold", bg="black")
p1_count.place(x=200, y=100)
p2_count=Label(window, text="", font=("verdana","20", "bold"), fg="gold", bg="black")
p2_count.place(x=200, y=150)

def score(p1_card,p2_card):
    global pts_1,pts_2
    x=p1_card.split("_", 1)[0]
    p1_card=int(x)
    y = p2_card.split("_", 1)[0]
    p2_card=int(y)
    if p1_card>p2_card:
        winner.config(text="Player 1 wins the round!")
        pts_1+=1
        p1_count.config(text=f"PLAYER 1:{pts_1}")
    elif p2_card>p1_card:
        winner.config(text="Player 2 wins the round!")
        pts_2+=1
        p2_count.config(text=f"PLAYER 2: {pts_2}")
    else:
        winner.config(text="It's a Tie!")





shuf_button = Button(window, text="Start Game", command=shuffle)
shuf_button.place(x=900,y=320)
draw_button = Button(window, text="Draw Card", command=deal)
draw_button.place(x=300, y=320)
window.mainloop()