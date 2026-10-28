# Description: Updated Simple Menu Application to test out game algorithms, applications and ideas
# Date: 01/22/2024, Cleaned up 10/28/2026

# Import tkinter to create GUI
from pathlib import Path
from tkinter import *
import sys
import time

# Import the menu and the games and applications
if __package__ in (None, ""):
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    from app.tools._Menu import Menu
    from app.games._MatrixMatch import MatrixMatch
    from app.games._Rps import RPS
    from app.tools._RpnCalc import RPNCalc
    from app.tools._ToDo import ToDo
else:
    from app.tools._Menu import Menu
    from app.games._MatrixMatch import MatrixMatch
    from app.games._Rps import RPS
    from app.tools._RpnCalc import RPNCalc
    from app.tools._ToDo import ToDo

# Global visualFrames
visualFrames = []


def clearVisualFrames():
    for x in visualFrames:
        x.destroy()


# Create functions for the menu to run
def playMatrixMatch():
    MatrixMatch.createGame()


def playRPS():
    RPS.createGame()


def runRPN():
    Calculator.createStack()
    Calculator.createCalc()


def runTODO():
    ToDoList.createToDo()


# Help page..
def helpMe():
    readmeFRAME = Frame(main, width=900, height=450, bg='#aaaaaa')
    readmeFRAME.place(x=0, y=0)
    visualFrames.append(readmeFRAME)
    info1 = Label(main,
                  text='1. MatrixMatch is a game where the rows and columns must be shaded according to the number\n'
                       + '2. Rock Paper Scissors is a random rng game\n'
                       + '3. RPN Calculator help using exists in its Menu\n'
                       + '4. Todo List is a circular list to add and remove items\n'
                       + 'More cases can easily be added'
                  , fg='#aaaaaa', bg='#2c2f33', font='arial 12 bold')
    info1.place(x=100, y=200)
    visualFrames.append(info1)


def readMe():
    readmeFRAME = Frame(main, width=900, height=450, bg='#aaaaaa')
    readmeFRAME.place(x=0, y=0)
    visualFrames.append(readmeFRAME)
    readThis1 = Label(main, text='Simple Menu Application GUI by Chris\n'
                                 + 'This was created with the purpose to easily add new items and test out game or '
                                   'application functionality\n '
                                 + 'Menu items can be added seamlessly with a singleton method menu\n'
                      , fg='#aaaaaa', bg='#2c2f33', font='arial 12 bold')
    readThis1.grid(row=0, column=0, pady=10, padx=10)
    visualFrames.append(readThis1)


# Create the GUI
def build_app():
    global main, MatrixMatch, RPS, Calculator, ToDoList, date

    main = Tk()
    icon_path = Path(__file__).resolve().parent / 'assets' / 'icon.ico'
    if icon_path.exists():
        main.iconbitmap(str(icon_path))

    MatrixMatch = MatrixMatch(main)
    RPS = RPS(main)
    Calculator = RPNCalc(main)
    ToDoList = ToDo(main)

    # Create the GUI to add games and applications to
    main.title('Simple Menu Application Gui')
    main.geometry('900x600')
    main.config(bg='#aaaaaa')

    # Create the array of items
    myMenu = Menu()
    myMenu.addMenu(playMatrixMatch, "Play MatrixMatch")
    myMenu.addMenu(playRPS, "Play RockPaperScissors")
    myMenu.addMenu(runRPN, "Run the RPN Calculator")
    myMenu.addMenu(runTODO, "ToDo List")
    myMenu.addMenu(helpMe, "Help Me")
    myMenu.addMenu(readMe, "Read me")

    # Now create them all under list number names
    for i, x in enumerate(myMenu.returnMenu()):
        Label(main, text=x.description, font='arial 24').grid(row=0 + i, column=0)
        Button(main, width=10, height=2, text='Click', bg='light blue', command=x.func).grid(row=0 + i, column=0 + 1,
                                                                                             padx=5)
    # Creating the reset button
    btnRestart = Button(main, text='Go to main',
                        command=lambda: [clearVisualFrames(), MatrixMatch.clearFrames(), RPS.clearFrames(),
                                         Calculator.clearFrames(), ToDoList.clearFrames()])
    btnRestart.config(width=30)
    btnRestart.place(x=350, y=500)
    # Hold time
    date = Label(main, text=time.asctime(time.localtime(time.time())))
    date.config(fg='#000000', font='verdana 12')
    date.place(x=0, y=500)

    def tick():
        time2 = time.strftime('%b %d %Y %H:%M:%S')
        date.config(text=time2)
        date.after(1000, tick)

    tick()
    return main


if __name__ == '__main__':
    main = build_app()
    main.mainloop()
