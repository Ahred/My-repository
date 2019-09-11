from tkinter import *       ###interface
from random import shuffle        ###for shuffle deck

deck = [2,3,4,5,6,7,8,9,10, 'Jack', 'Queen', 'King', 'Ace'] * 4

shuffle(deck)

count = 0

def take():
    global count, deck
    card = deck.pop() ### pop - take the first card

    if card == 'Jack' or card == 'Queen' or card == 'King':
        card = 10
    if card == 'Ace':
        card = 11

    count += card

    if count > 21:
        text3['text'] = 'Ooops, you lose :( ,your score is '+ str(count)
        text2['text'] = 'You lose'
    else:
        text2['text'] = 'Your score is '+ str(count)
        
     

def enough():
    global count

    if count == 21:
        text3['text'] = 'Congratulation, your score is 21'
        
       

    if count < 21:
        text3['text'] = 'Your score is '+ str(count)



        
###Create a window for the game
root = Tk()
root.geometry('300x140')
###Label
text1 = Label(root, text = 'The Black Jack game', fg = 'red')
text1.place(x=100, y=0)  ###location of inscription; x-width, y-height
###Score 
text2 = Label(root, text = 'Your score is 0', fg = 'blue')
text2.place(x = 110, y = 30)
###Button 1 (Take a card)
but1 = Button(root, width = '15', text = 'Take a card', command = take)
but1.place(x=20, y=60)
###Button 2 (Enough)
but2 = Button(root, width = '15', text = 'Enough', command = enough)
but2.place(x = 160, y = 60)
###Text in the end
text3 = Label (root, text = 'The result of the game', fg = 'red')
text3.place(x = 90, y = 100)

root.mainloop()
