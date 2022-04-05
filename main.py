# import the library
from appJar import gui
from datetime import date




today = date.today()





# create a GUI variable called app





# app = gui ( "Gary Pawn", "1280x720" ) #Adds a text area with a vertical scroll bar
# app.addScrolledTextArea ( "Daily Report ----- Gary's Pawn Shop", 123 ) 

# # add & configure widgets - widgets get a name, to help referencing them later
# # app.addLabel("title", "Daily Report")
# # app.setLabelBg("title", "red")

# #begginning cash on hand total
# app.addLabel("fn","Beginning Cash on Hand",0,0)


# # start the GUI
# app.go()


def press(btn):
    if btn == "Exit":
        win.stop()
    else:
        try:








            firstNum = float(win.getEntry("first"))
            secondNum = float(win.getEntry("second"))
            registercount = float(win.getEntry("third"))

            # thirnum=float(win.getEntry("third"))

            message =  "The results are as follows:\n\n"
            message += "Addition: " + str (firstNum + secondNum) + "\n"
            message += "Subtraction: " + str (firstNum - secondNum) + "\n"
            message += "Multiplication: " + str (firstNum * secondNum) + "\n"


            result=result+fistnum+secondNum
            
            message += "Over Or Short " + str (result+result1) + "\n"







            if btn == "Result":
                win.setLabel("Result", message)

                    
        except ValueError as e:
            win.errorBox("Error", "Invalid number")
            win.setFocus ( "first" )

win = gui("Calculator", "1280x720")
win.setBg("grey")
win.setFont(18)
# add 2 labels & buttons - this time specify row & column



win.addLabel ( "fn", "Beginning Cash On Hand", 0, 0 )
win.addEntry ( "first", 0, 1 )
win.addLabel ( "sn", "Purchase", 0, 2 )
win.addEntry ( "second", 0, 3 )
win.setFocus ( "first" )
win.addLabel ( "tn", "Total Cash in Register", 4, 0 )
win.addEntry ( "third", 4, 1 )

# add the result label - specify row/column/colspan
win.addEmptyLabel("Result", 1, 0, 1)

# format the label
win.setLabelRelief("Result", win.GROOVE)
win.setLabelAlign("Result", win.NW)
win.setLabelHeight("Result", 1)

# add the buttons
win.addButtons(["Result", "Exit"], press, 2, 5, 2)
# start the GUI
win.go()
