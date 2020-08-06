import random
from tkinter import *
from tkinter import scrolledtext


#LISTS
dice_list=['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

card_list=[]


def main():
    #ROOT
    root=Tk()
    root.title('Draw Roll Dice')
    root.geometry('500x400+300+100')
    root.minsize(500,350)

    #FUNCION ROLL

    def roll():
        dices=int(number_entry.get())+1
        box.delete(1.0,END)

        for i in range(1,dices):
            dice=random.choice(dice_list)
            box.insert(END,dice)


    def draw():
        cards=int(number_entry.get())+1
        box.delete(1.0,END)

        for i in range(1,cards):
            card=random.choice(card_list)
            box.insert(END,card)



    #FRAME
    frame=Frame(root)
    frame.pack(padx=2,pady=2,side='top',expand=True, fill='both')

    #BOX
    box=Text(frame, height=2, width=2)
    box.config(font=('arial',60,'bold'))
    box.pack(side='left',expand=True,fill='both')

    xframe=Frame(root)
    xframe.pack(fill="x")

    scrollx=Scrollbar(xframe, command=box.xview,width=13,orient="horizontal") 
    scrollx.pack(side="bottom",fill="x")

    scrolly=Scrollbar(frame, command=box.yview, width=13)
    scrolly.pack(side="left",fill="y")

    box.config(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

    #BUTTONS
    bframe=Frame(root)
    bframe.pack(side='bottom')
    
    roll_button=Button(bframe,text='Roll Dices!', bd=3, command=lambda:roll())
    roll_button.grid(row='0',column='2',padx=10, pady=10)

    '''
    draw_button=Button(bframe,text='Draw Cards!', bd=3, command=lambda:draw())
    draw_button.grid(row='0',column='3',padx=10, pady=10)
    '''
    
    dicetxt=Label(bframe,text='Set the number:')
    dicetxt.grid(row='0',column='0',padx=10, pady=10)

    number=StringVar()
    number_entry=Entry(bframe, width=4, textvariable=number)
    number_entry.grid(row='0',column='1',padx=10, pady=10)



    

    root.mainloop()

main()