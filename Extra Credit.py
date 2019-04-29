#Madubuke Ekpecham
#Extra Credit

from graphics import*
from button import*
import math

#Conversions for Kilos, Grams, and Ounces
def Kils(weight):
    kilos = weight * .4535
    return kilos
def Ounc(weight):
    onces = weight * 16
    return onces
def Gra(weight):
    grams = weight* 453.592
    return grams
#Inputs an error if value isnt correct
def notValid (inputbox2, inputbox3, inputbox4):
    inputbox2.setText("Enter a correct value")
    inputbox3.setText("Enter a correct value")
    inputbox4.setText("Enter a correct value")
    
def main():
#Creates the Window
    win = GraphWin("Weight Converter", 500, 500)
    win.setBackground('grey92')

    #Create title of program and show textbox
    text1 = Text(Point(250,50), "Weight Converter")
    text2 = Text(Point(365,90), "lbs")
    inputbox = Entry(Point(250,90),26)
    #Create Gram category and show textbox
    text3 = Text(Point(185,150), "Grams")
    inputbox2 = Entry(Point(250,175),26)
    #Create Kilograms category and show textbox
    text4 = Text(Point(200,230), "Kilograms")
    inputbox3 = Entry(Point(250,255),26)
    #Create Ounces category and show textbox
    text5 = Text(Point(190,300), "Ounces")
    inputbox4 = Entry(Point(250,325),26)
    #Makes the objects show on the program and edits fill, text style, and size
    inputbox.draw(win)
    inputbox.setFill('white')
    inputbox.setText(" ")
    inputbox2.draw(win)
    inputbox2.setFill('white')
    inputbox2.setText("0")
    inputbox3.draw(win)
    inputbox3.setFill('white')
    inputbox3.setText("0")
    inputbox4.draw(win)
    inputbox4.setFill('white')
    inputbox4.setText("0")
    text1.draw(win)
    text1.setSize(30)
    text1.setStyle('bold')
    text2.draw(win)
    text2.setStyle('bold')
    text3.draw(win)
    text3.setStyle('bold')
    text3.setSize(20)
    text4.draw(win)
    text4.setStyle('bold')
    text4.setSize(20)
    text5.draw(win)
    text5.setStyle('bold')
    text5.setSize(20)

    #Makes button and converts values
    button = Button(win,Point(230,430),130,90, "Convert")
    button.activate()
    butClick = win.getMouse()

    #Initiate While loop to get values and display an error if the value is wrong
    while button.clicked(butClick):
        try:
            weight = eval(inputbox.getText())
            inputbox2.setText(Kils(weight))
            inputbox3.setText(Ounc(weight))
            inputbox4.setText(Gra(weight))
        except:
            notValid (inputbox2, inputbox3, inputbox4)
                          

        butClick=win.getMouse()
    win.getMouse()


main()
