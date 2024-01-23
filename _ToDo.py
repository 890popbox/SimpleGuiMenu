# Basic ToDo list class
from tkinter import *
from _Menu import *


class ToDo(object):
    def __init__(self, root):
        self.root = root
        self.ToDoList = []
        self.visualFrames = []
        self.ToDoFrames = []
        self.extraFrames = []
        self.currentPos = 0
        self.currentDisplay = Label()

    # Show to do
    def createLabel(self):
        main = self.root
        self.currentDisplay = Label(main, text='NAN', width=55, height=15, fg='#000000', bg='#ffffff')
        self.currentDisplay.place(x=255, y=75)
        self.ToDoFrames.append(self.currentDisplay)

    # Display change
    def showToDo(self, pos):
        self.currentDisplay.config(text=('index[' + str(pos) + ']. ' + self.ToDoList[pos]))

    # Create this class
    def createToDo(self):
        main = self.root
        todoFRAME = Frame(main, width=600, height=450, bg='#aaaaaa')
        todoFRAME.place(x=0, y=0)
        self.visualFrames.append(todoFRAME)
        # The first label
        self.createLabel()

        # Add
        add_ = Button(main, text="Add an item to the list", width=20, height=2, command=lambda: self.showAddingFrames())
        add_.place(x=475, y=320)
        self.ToDoFrames.append(add_)

        # Add
        del_ = Button(main, text="Delete an item to the list", width=20, height=2,
                      command=lambda: self.showDeletingFrames())
        del_.place(x=275, y=320)
        self.ToDoFrames.append(del_)

        # Clean
        clean_ = Button(main, text="Clear all of the list", width=20, height=2, command=lambda: self.showClearFrames())
        clean_.place(x=650, y=500)
        self.ToDoFrames.append(clean_)

        # Go left and right..
        left_ = Button(main, text="<-", width=15, height=5, command=lambda: self.goBACK())
        left_.place(x=100, y=150)
        self.ToDoFrames.append(left_)
        right_ = Button(main, text="->", width=15, height=5, command=lambda: self.goFORWARD())
        right_.place(x=700, y=150)
        self.ToDoFrames.append(right_)

    # BACK AND FORTH
    def goBACK(self):
        # If list is empty can't run this
        if (len(self.ToDoList) == 0):
            return

        # If above 0 we can go back, else have to go to end of list, else rarely happens]
        if (self.currentPos > 0):
            self.currentPos -= 1
            self.showToDo(self.currentPos)
        else:
            self.currentPos = len(self.ToDoList) - 1
            self.showToDo(self.currentPos)

    def goFORWARD(self):
        # If list is empty can't run this
        if (len(self.ToDoList) == 0):
            return

        # If we go beyond bounds, go back to 0
        if (self.currentPos < len(self.ToDoList) - 1):
            self.currentPos += 1
            self.showToDo(self.currentPos)
        else:
            self.currentPos = 0
            self.showToDo(self.currentPos)

    # Adding stuff
    def showAddingFrames(self):
        main = self.root
        addingFrame = Frame(main, width=900, height=500, bg='#bbbbbb')
        addingFrame.place(x=0, y=0)
        self.extraFrames.append(addingFrame)
        entryLine = Entry(main, width=30, fg='#000000', bg='#ffffff')
        entryLine.place(x=370, y=250)
        self.extraFrames.append(entryLine)
        # Add and cancel
        addit_ = Button(main, text="Add", width=10, height=2, command=lambda: self.addToDo(entryLine.get()))
        addit_.place(x=475, y=300)
        self.extraFrames.append(addit_)
        cancel_ = Button(main, text="Cancel", width=10, height=2, command=lambda: self.cancelFrame())
        cancel_.place(x=375, y=300)
        self.extraFrames.append(cancel_)

    # Deleting item
    def showDeletingFrames(self):
        main = self.root
        deletingFrame = Frame(main, width=900, height=500, bg='#bbbbbb')
        deletingFrame.place(x=0, y=0)
        self.extraFrames.append(deletingFrame)
        entryLine = Entry(main, width=30, fg='#000000', bg='#ffffff')
        entryLine.place(x=370, y=250)
        self.extraFrames.append(entryLine)
        # Add and cancel
        delit_ = Button(main, text="Delete", width=10, height=2, command=lambda: self.delToDo(entryLine.get()))
        delit_.place(x=475, y=300)
        self.extraFrames.append(delit_)
        cancel_ = Button(main, text="Cancel", width=10, height=2, command=lambda: self.cancelFrame())
        cancel_.place(x=375, y=300)
        self.extraFrames.append(cancel_)

    # Delete the whole list
    def showClearFrames(self):
        main = self.root
        cleaningFrame = Frame(main, width=900, height=500, bg='#bbbbbb')
        cleaningFrame.place(x=0, y=0)
        self.extraFrames.append(cleaningFrame)
        # Add and cancel
        clearit_ = Button(main, text="Confirm clear", width=10, height=2, command=lambda: self.cleanToDo())
        clearit_.place(x=475, y=300)
        self.extraFrames.append(clearit_)
        cancel_ = Button(main, text="Cancel clear", width=10, height=2, command=lambda: self.cancelFrame())
        cancel_.place(x=375, y=300)
        self.extraFrames.append(cancel_)

    # Finish adding
    def cancelFrame(self):
        for c in self.extraFrames:
            c.destroy()
        self.extraFrames.clear()

    # Add whats in entry and cancel.
    def addToDo(self, item):
        self.ToDoList.append(item)
        self.cancelFrame()
        self.showToDo(self.currentPos)

    # Delete whats in entry and cancel.
    def delToDo(self, item):
        if len(self.ToDoList):
            self.ToDoList.remove(item)
            self.currentPos -= 1
        self.cancelFrame()
        self.showToDo(self.currentPos)

    # Confirm clear, you can do a few in in lambda but need to set pos also
    def cleanToDo(self):
        self.ToDoList.clear()
        self.cancelFrame()
        self.createLabel()
        self.currentPos = 0

    # Clean frames
    def clearFrames(self):
        for a in self.visualFrames:
            a.destroy()
        for b in self.ToDoFrames:
            b.destroy()
        self.visualFrames.clear()
        self.ToDoFrames.clear()
        self.cancelFrame()
