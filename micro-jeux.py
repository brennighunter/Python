#Mega collection de micro-jeux

from Tkinter import *

import scissors
import hangman
import pokerdice

root = Tk()
root.title("Mega collection de micro-jeux")

mainframe = Frame(root, height = 200, width = 500)
mainframe.pack_propagate(0)
mainframe.pack(padx = 5, pady = 5)

intro = Label(mainframe, text = "Bienvenue a la Mega collection de micro-jeux. Selectionnez l un des jeux suivants pour jouer:")
intro.pack(side=TOP)

rps_button = Button(mainframe, text = "Caillou, Papier, Ciseaux", command =
scissors.start)
rps_button.pack()

hm_button = Button(mainframe, text = "Pendu", command = hangman.start)
hm_button.pack()

pd_button = Button(mainframe, text = "Poker aux des", command = pokerdice.start)
pd_button.pack()

exit_button = Button(mainframe, text = "Quit", command = root.destroy)

exit_button.pack(side = BOTTOM)
root.mainloop()
