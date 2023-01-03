from tkinter import *
from random import *
from PIL import Image, ImageTk
import mysql.connector as mc
c=mc.connect(host="localhost",user="root",passwd="boredum2808",database="csproject")
cr=c.cursor()
window = Tk()
window.title('WAR')
window.geometry("1920x1280")
window.configure(background="black")
f1=Frame(window, bg="green")
f2=Frame(window, bg="green")
f3=Frame(window, bg="green")
f1.place(x=0, y=350)
f2.place(x=670, y=350)
f3.place(x=450, y=50)


p1_frame = LabelFrame(f1, text="Player 1", bd=0)
p1_frame.grid(row=1, column=0, ipadx=10)

p2_frame = LabelFrame(f2, text="Player 2", bd=0)
p2_frame.grid(row=1, column=0, ipadx=10)

dealer_frame= LabelFrame(f3,text="Dealer", bd=0)
dealer_frame.grid(row=1, column=0, ipadx=10)



def resize(card):
    cardpic = Image.open(card)

    new_cardpic = cardpic.resize((75, 109))

    global card_img
    card_img = ImageTk.PhotoImage(new_cardpic)

    return card_img


def shuffle():
    win_1.config(text="")
    win_2.config(text="")
    s = ["dice", "clubs", "hearts", "spade"]
    val = range(1, 14)
    global deck
    deck = []
    for x in s:
        for y in val:
            deck.append(f'{y}_{x}')
    hit_1["state"]=NORMAL
    hit_2["state"]=NORMAL
    stand_1["state"]=NORMAL
    stand_2["state"]=NORMAL
    p1_lab.config(image="")
    p1_lab_1.config(image="")
    p1_lab_2.config(image="")
    p1_lab_3.config(image="")
    p1_lab_4.config(image="")

    p2_lab.config(image="")
    p2_lab_1.config(image="")
    p2_lab_2.config(image="")
    p2_lab_3.config(image="")
    p2_lab_4.config(image="")

    p3_lab.config(image="")
    p3_lab_1.config(image="")
    p3_lab_2.config(image="")
    p3_lab_3.config(image="")
    p3_lab_4.config(image="")



    global p1,p2,p3,p1_place,p2_place,p3_place,bj_1,bj_2,bj_3
    p1 = []
    p2 = []
    p3 = []
    p1_place=0
    p2_place=0
    p3_place=0
    bj_1=0
    bj_2=0
    bj_3=0

    p1_hit()
    p1_hit()
    p2_hit()
    p2_hit()
    p3_hit()
    p3_hit()
    global IsClicked_1,IsClicked_2
    IsClicked_1=False
    IsClicked_2=False
    #start.destroy()
def p1_hit():
    global p1_place
    if p1_place<=4:
        try:
            p1_card = choice(deck)
            deck.remove(p1_card)

            cd=p1_card.split("_",1)[0]
            cd1=int(cd)
            p1.append(order[cd1])
            global p1_pic1,p1_pic2,p1_pic3,p1_pic4,p1_pic5
            if p1_place==0:
                p1_pic1 = resize(f"C:/Users/Welcome/Desktop/card/{p1_card}.png")
                p1_lab.config(image=p1_pic1)
                p1_place += 1
            elif p1_place==1:
                p1_pic2 = resize(f"C:/Users/Welcome/Desktop/card/{p1_card}.png")
                p1_lab_1.config(image=p1_pic2)
                p1_place += 1
            elif p1_place==2:
                p1_pic3 = resize(f"C:/Users/Welcome/Desktop/card/{p1_card}.png")
                p1_lab_2.config(image=p1_pic3)
                p1_place += 1
            elif p1_place==3:
                p1_pic4 = resize(f"C:/Users/Welcome/Desktop/card/{p1_card}.png")
                p1_lab_3.config(image=p1_pic4)
                p1_place += 1
            elif p1_place==4:
                p1_pic5 = resize(f"C:/Users/Welcome/Desktop/card/{p1_card}.png")
                p1_lab_4.config(image=p1_pic5)
                p1_place+=1


        except:
            return " "
        bj("p1")


def p2_hit():
    global p2_place
    if p2_place<=4:
        try:
            p2_card = choice(deck)
            deck.remove(p2_card)
            cd = p2_card.split("_", 1)[0]
            cd1 = int(cd)
            p2.append(order[cd1])
            global p2_pic1,p2_pic2,p2_pic3,p2_pic4,p2_pic5
            if p2_place==0:
                p2_pic1 = resize(f"C:/Users/Welcome/Desktop/card/{p2_card}.png")
                p2_lab.config(image=p2_pic1)
                p2_place += 1
            elif p2_place==1:
                p2_pic2 = resize(f"C:/Users/Welcome/Desktop/card/{p2_card}.png")
                p2_lab_1.config(image=p2_pic2)
                p2_place += 1
            elif p2_place==2:
                p2_pic3 = resize(f"C:/Users/Welcome/Desktop/card/{p2_card}.png")
                p2_lab_2.config(image=p2_pic3)
                p2_place += 1
            elif p2_place==3:
                p2_pic4 = resize(f"C:/Users/Welcome/Desktop/card/{p2_card}.png")
                p2_lab_3.config(image=p2_pic4)
                p2_place += 1
            elif p2_place==4:
                p2_pic5 = resize(f"C:/Users/Welcome/Desktop/card/{p2_card}.png")
                p2_lab_4.config(image=p2_pic5)
                p2_place+=1


        except:
            return " "
        bj("p2")
def p3_hit():
    global p3_place
    if p3_place<=4:
        try:
            p3_card = choice(deck)
            deck.remove(p3_card)
            cd = p3_card.split("_", 1)[0]
            cd1 = int(cd)
            p3.append(order[cd1])
            global p3_pic1,p3_pic2,p3_pic3,p3_pic4,p3_pic5
            if p3_place==0:
                p3_pic1 = resize(f"C:/Users/Welcome/Desktop/card/{p3_card}.png")
                p3_lab.config(image=p3_pic1)
                p3_place += 1
            elif p3_place==1:
                p3_pic2 = resize(f"C:/Users/Welcome/Desktop/card/{p3_card}.png")
                p3_lab_1.config(image=p3_pic2)
                p3_place += 1
            elif p3_place==2:
                p3_pic3 = resize(f"C:/Users/Welcome/Desktop/card/{p3_card}.png")
                p3_lab_2.config(image=p3_pic3)
                p3_place += 1
            elif p3_place==3:
                p3_pic4 = resize(f"C:/Users/Welcome/Desktop/card/{p3_card}.png")
                p3_lab_3.config(image=p3_pic4)
                p3_place += 1
            elif p3_place==4:
                p3_pic5 = resize(f"C:/Users/Welcome/Desktop/card/{p3_card}.png")
                p3_lab_4.config(image=p3_pic5)
                p3_place+=1


        except:
            return " "
        bj("p3")
def bj(x):
    global bj_1,bj_2,bj_3,IsClicked_1,IsClicked_2
    if x=="p1":
        print(p1)
        if len(p1)==2:
            if sum(p1)==21:
                bj_1=1
        else:
            if sum(p1)==21:
                bj_1=1
            elif sum(p1)>21:
                for y in p1:
                    if y==11:
                        p1[p1.index(y)]=1
                if sum(p1)>21:
                    bj_1=2
            else:
                if sum(p1) == 21:
                    bj_1 = 1
                if sum(p1) > 21:
                    bj_1 = 2

    if x=="p2":
        print(p2)
        if len(p2)==2:
            if sum(p2)==21:
                bj_2=1
        else:
            if sum(p2)==21:
                bj_2=1
            elif sum(p2)>21:
                for z in p2:
                    if z==11:
                        p2[p2.index(z)]=1
                if sum(p2)>21:
                    bj_2=2
                else:
                    if sum(p2)==21:
                        bj_2=1
                    if sum(p2)>21:
                        bj_2=2

    if x=="p3":
        print(p3)
        if len(p3)==2:
            if sum(p3)==21:
                bj_3=1
            elif sum(p3)>21:
                for e in p3:
                    if e==11:
                        p3[p3.index(e)]=1
                if sum(p3)>21:
                    bj_3=2
            else:
                if sum(p3) == 21:
                    bj_3 = 1
                if sum(p3) > 21:
                    bj_3 = 2
    if len(p1)==2 and len(p2)==2 and len(p3)==2:
        if bj_1==1 and bj_3==1 and bj_2==1:
            win_1.config(text="It's a Tie")
            win_2.config(text="It's a Tie")
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==1 and bj_3==0 and bj_2==1:
            win_1.config(text="Player 1 Wins!")
            win_2.config(text="Player 2 Wins!")
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==0 and bj_3==1 and bj_2==0:
            win_1.config(text="Dealer Wins")
            win_2.config(text="Dealer Wins")
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==1 and bj_3==1 and bj_2==0:
            win_1.config(text="It's a Tie")
            win_2.config(text="Dealer Wins")
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==0 and bj_3==1 and bj_2==1:
            win_1.config(text="Dealer Wins")
            win_2.config(text="It's a Tie")
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==0 and bj_3==0 and bj_2==1:
            win_2.config(text="Player 2 Wins!")
            IsClicked_2=True
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==1 and bj_3==0 and bj_2==0:
            win_1.config(text="Player 1 Wins!")
            IsClicked_1=True
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED

    else:
        if bj_1==1 and bj_3==1 and bj_2==1:
            win_1.config(text="It's a Tie")
            win_2.config(text="It's a Tie")
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==1 and bj_3==0 and bj_2==1:
            win_1.config(text="Player 1 Wins!")
            win_2.config(text="Player 2 Wins!")
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==0 and bj_3==1 and bj_2==0:
            win_1.config(text="Dealer Wins")
            win_2.config(text="Dealer Wins")
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==1 and bj_3==1 and bj_2==0:
            win_1.config(text="It's a Tie")
            win_2.config(text="Dealer Wins")
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==0 and bj_3==1 and bj_2==1:
            win_1.config(text="Dealer Wins")
            win_2.config(text="It's a Tie")
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==0 and bj_3==0 and bj_2==1:
            win_2.config(text="Player 2 Wins")
            IsClicked_2=True
            hit_2["state"] = DISABLED
            stand_2["state"] = DISABLED
        elif bj_1==1 and bj_3==0 and bj_2==0:
            win_1.config(text="Player 1 Wins")
            IsClicked_1=True
            hit_1["state"] = DISABLED
            stand_1["state"] = DISABLED
    if bj_1==2:
        win_1.config(text="Player 1 Loses")
        IsClicked_1=True
        hit_1["state"]=DISABLED
        stand_1["state"]=DISABLED
    if bj_2==2:
        win_2.config(text="Player 2 Loses")
        IsClicked_2=True
        hit_2["state"]=DISABLED
        stand_2["state"]=DISABLED

def stand1():
    global IsClicked_1,IsClicked_2
    IsClicked_1=True
    stand()
def stand2():
    global IsClicked_2,IsClicked_1
    IsClicked_2= True
    stand()

def stand():
    global p1,p2,p3,IsClicked_1,IsClicked_2
    if IsClicked_1==True and IsClicked_2==True:
        hit_1['state']=DISABLED
        stand_1['state']=DISABLED
        hit_2['state']=DISABLED
        stand_2['state']=DISABLED
        if sum(p3)>=16 :
            if sum(p3)>sum(p1):
                win_1.config(text="Dealer Wins")
            elif sum(p3)<sum(p1):
                win_1.config(text="Player 1 Wins")
            if sum(p3)<sum(p2):
                win_2.config(text="Player 2 Wins!")
            elif sum(p3)>sum(p2):
                win_2.config(text="Dealer Wins")
            if sum(p3)==sum(p1):
                win_1.config(text="It's a Tie")
            if sum(p3)==sum(p2):
                win_2.config(text="It's a Tie")
            if sum(p3)>21 and sum(p2)<21:
                win_2.config(text="Player 2 Wins")
            if sum(p3)>21 and sum(p1)<21:
                win_1.config(text="Player 1 Wins")
            if sum(p2)>21:
                win_2.config(text="Player 2 Loses")
            if sum(p1)>21:
                win_1.config(text="Player 1 Loses")
            if sum(p1)==21:
                win_1.config(text="Player 1 Wins!")
            if sum(p2)==21:
                win_2.config(text="Player 2 Wins!")
            if sum(p3)>21 and sum(p1)<21:
                win_1.config(text="Player 1 Wins")
            if sum(p3)>21 and sum(p2)<21:
                win_2.config(text="Player 2 Wins")
            '''if sum(p3)>21 and sum(p1)<21 and sum(p2)<21:
                win_1.config(text="Player 1 Wins (Dealer busts)")
                win_2.config(text="Player 2 Wins (Dealer busts)")
            elif sum(p3)>21 and sum(p1)<21:
                win_1.config(text="Player 1 Wins!")
            elif sum(p3)>21 and sum(p2)<21:
                win_2.config(text="Player 2 Wins!")
            elif sum(p3)>sum(p2) and sum(p3)>sum(p1) and sum(p1)<=21 and sum(p2)<=21:
                win_1.config(text="Dealer Wins")
                win_2.config(text="Dealer Wins")
            elif sum(p3)>sum(p2) and sum(p3)<sum(p1) and sum(p1)<=21 and sum(p2)<=21:
                win_2.config(text="Dealer Wins")
                win_1.config(text="Player 1 Wins!")
            elif sum(p3)<sum(p2) and sum(p3)>sum(p1) and sum(p1)<=21 and sum(p2)<=21:
                win_1.config(text="Dealer Wins")
                win_2.config(text="Player 2 Wins!")
            elif sum(p3)<sum(p2) and sum(p3)<sum(p1) and sum(p1)<=21 and sum(p2)<=21:
                win_1.config(text="Player 1 Wins!")
                win_2.config(text="Player 2 Wins!")
            elif sum(p1)==21 and sum(p3)>sum(p2):
                win_1.config(text="Player 1 Wins!")
                win_2.config(text="Dealer Wins")
            elif sum(p1)==21 and sum(p3)<sum(p2):
                win_1.config(text="Player 1 Wins!")
                win_2.config(text="Player 2 Wins!")
            elif sum(p1)==21 and sum(p3)==sum(p2):
                win_1.config(text="Player 1 Wins")
                win_2.config(text="It's a Tie")
            elif sum(p2)==21 and sum(p3)<sum(p1):
                win_1.config(text="Player 1 Wins!")
                win_2.config(text="Player 2 Wins!")
            elif sum(p2)==21 and sum(p3)>sum(p1):
                win_2.config(text="Player 2 Wins!")
                win_1.config(text="Dealer Wins")
            elif sum(p2)==21 and sum(p3)==sum(p1):
                win_2.config(text="Player 2 Wins")
                win_1.config(text="It's a Tie")'''




        else:
            p3_hit()
            stand()





def add():
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

        p3_card = choice(deck)
        deck.remove(p3_card)
        p3.append(p3_card)
        global p3_pic
        p3_pic = resize(f"C:/Users/Welcome/Desktop/card/{p3_card}.png")
        p3_lab.config(image=p3_pic)


    except:
        return ""





order={1:11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:10, 12:10, 13:10}
p1_lab = Label(p1_frame, text='')
p1_lab.grid(row=0, column=0, pady=20, padx=20)
p1_lab_1 = Label(p1_frame, text='')
p1_lab_1.grid(row=0, column=1, pady=20, padx=20)
p1_lab_2 = Label(p1_frame, text='')
p1_lab_2.grid(row=0, column=2, pady=20, padx=20)
p1_lab_3 = Label(p1_frame, text='')
p1_lab_3.grid(row=0, column=3, pady=20, padx=20)
p1_lab_4 = Label(p1_frame, text='')
p1_lab_4.grid(row=0, column=4, pady=20, padx=20)


p2_lab = Label(p2_frame, text='')
p2_lab.grid(row=0, column=0, pady=20, padx=20)
p2_lab_1 = Label(p2_frame, text='')
p2_lab_1.grid(row=0, column=1,pady=20, padx=20)
p2_lab_2 = Label(p2_frame, text='')
p2_lab_2.grid(row=0, column=2, pady=20, padx=20)
p2_lab_3 = Label(p2_frame, text='')
p2_lab_3.grid(row=0, column=3, pady=20, padx=20)
p2_lab_4 = Label(p2_frame, text='')
p2_lab_4.grid(row=0, column=4, pady=20, padx=20)


p3_lab = Label(dealer_frame, text='')
p3_lab.grid(row=0, column=0, pady=20, padx=20)
p3_lab_1 = Label(dealer_frame, text='')
p3_lab_1.grid(row=0, column=1, pady=20, padx=20)
p3_lab_2 = Label(dealer_frame, text='')
p3_lab_2.grid(row=0, column=2, pady=20, padx=20)
p3_lab_3 = Label(dealer_frame, text='')
p3_lab_3.grid(row=0, column=3, pady=20, padx=20)
p3_lab_4 = Label(dealer_frame, text='')
p3_lab_4.grid(row=0, column=4, pady=20, padx=20)

win_1=Label(window, text="",font="verdana",bg="black",fg="yellow")
win_1.place(x=200,y=280)
win_2=Label(window,text="",font="verdana",bg="black",fg="yellow")
win_2.place(x=800,y=280)

stand_1 = Button(window, text="STAND", command=stand1)
stand_1.place(x=320,y=570)
hit_1 = Button(window, text="HIT", command=p1_hit)
hit_1.place(x=270, y=570)
stand_2 = Button(window, text="STAND", command=stand2)
stand_2.place(x=970,y=570)
hit_2 = Button(window, text="HIT", command=p2_hit)
hit_2.place(x=920, y=570)
start=Button(window,text="New Round",command=shuffle)
start.place(x=570, y=280)
window.mainloop()