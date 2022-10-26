import tkinter as tk
import random
import time


minPos=0
maxPos=800
number_of_squares = 50
squareMaxSize=200
number_of_circles = 10
circleMaxSize=200

app = tk.Tk()

def on_KeyRelease(KeyRelease):
    createRandomArt()


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle


def _create_square(self, x, y, r, **kwargs):
    return self.create_rectangle(x, y, x+r, y+r, **kwargs)
tk.Canvas.create_square = _create_square


def createRandomArt():
    for i in range(number_of_squares):
        x=random.randint(minPos, maxPos)
        y=random.randint(minPos, maxPos)
        size=random.randint(minPos, squareMaxSize)
        color="#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        canvas.create_square(x, y, size, fill=color, width=0)

    for i in range(number_of_circles):
        x=random.randint(minPos, maxPos)
        y=random.randint(minPos, maxPos)
        size=random.randint(minPos, circleMaxSize)
        color="#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        canvas.create_circle(x, y, size, fill=color, width=0)


app.bind("<KeyRelease>", on_KeyRelease)
canvas = tk.Canvas(app, width=maxPos, height=maxPos, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()
createRandomArt()
app.wm_title("Random art")
app.mainloop()
