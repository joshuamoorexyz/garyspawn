# import the library
from appJar import gui
from datetime import datetime

#global variables
totalcash=0.00
totaltax=0.00
totalregister=0.00
oos = 0.00
totalsale=0
totalpawn=0.00
pawns=0



#set date and time

now = datetime.now() # current date and time
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
date_today = now.strftime("%m/%d/%Y")


#functions needed for the program



    

def gettax(price):
    
    state_sales_tax = .07
    return price * state_sales_tax




def press(name):
    print(name,"Button pressed")
    if name == "Calculate":
        cash=win.getEntry("Beginning Cash On Hand:")
        print(cash)
        global totalregister
        global totalcash
        global totaltax
        global oos
        global totalsale
        global totalpawn

        if(totalregister ==0.00):
            totalregister=totalregister+float(cash)
            win.setLabel("totalbcash","Beginning Cash in Register:"+str('%.2f' % totalregister))
            totalcash=totalcash+totalregister
            win.setLabel("totalcash","Total Cash in Register:"+str('%.2f' % totalcash))
        else:    
            #sell an item

            #need to make beginning cash field non interactive after inital value is set
            sale=win.getEntry("New Sale:")
            totalcash=totalcash+float(sale)
            totalsale=totalsale+1
            win.setLabel("totalcash","Total Cash in Register:"+str('%.2f' % totalcash))
            win.setLabel("totalsales", "Total Sales:"+str(totalsale))

            #pawn
            pawn=win.getEntry("New Pawn:")
            
            totalpawn=totalpawn+float(pawn)
            totalcash=totalcash-float(pawn)
            pawns=pawns+1
            win.setLabel("totalcash","Total Cash in Register:"+str('%.2f' % totalcash))
            win.setLabel("totalpawns", "Total Pawns:"+str(pawns))
            win.setLabel("totalpawn","Total pawned:"+str('%.2f' %totalpawn))

            #get tax
            tax=gettax(float(sale))
            totaltax=totaltax+tax
            win.setLabel("totaltax", "Total Tax Collected:"+str('%.2f' % totaltax))
            #calc over/under
            oos=totalcash-totalregister
            win.setLabel("oos", "Over or Short:"+str('%.2f' % oos))


            #clear text input areas
            win.clearEntry("New Sale:", callFunction=True)

    if name == "Report":
        pass








        




win = gui("DAILY REPORT----------Gary's Pawn and Gun "+"----------Date of Report:"+date_today , "1280x720")
win.setBg("grey")
win.setFont(18)


win.addLabelEntry ("Beginning Cash On Hand:")
#win.addButton("Calculate",press)
win.addLabelEntry ("New Sale:")
win.addLabelEntry ("New Pawn:")
win.addLabel ( "totalbcash", "Beginning Cash in Register:"+str(totalregister), 4, 0 )
win.addLabel ( "totalcash", "Total Cash in Register:"+str(totalcash), 4, 1 )
win.addLabel ( "totaltax", "Total Tax Collected:"+str(totaltax), 5, 0 )
win.addLabel ( "oos", "Over or Short:"+str(oos), 5,1 )
win.addLabel ( "totalsales", "Total Sales:"+str(totalsale), 5,2 )
win.addLabel("totalpawns", "Total Pawns:"+str(pawns),6,0)
win.addLabel("totalpawn","Total pawned:"+str(totalpawn),6,1)


win.addButtons(["Calculate","Report"],press)





# start the GUI
win.go()
