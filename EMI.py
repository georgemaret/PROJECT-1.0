from guietta import _, Gui, Quit

gui = Gui (
    ["Product Cost: ", '__p__'],
    ["Rate of Interest: ", '__r__'],
    ["Number of Months: ", '__n__'],
    [   ['EMI'], _ ],
    ["EMI = ",'result']
)

def emi(gui):
    p= int(gui.p)
    n= int(gui.n)
    r= int(gui.r)/100
    gui.result= p*r*((1+r)**n)/(((1+r)**n)-1)


gui.EMI= emi


gui.run()
