
import sys
import tkinter

root = tkinter.Tk()
root.title(u"title")
root.geometry("400x300")

frame = tkinter.Frame(root, height = 100, width = 200, 
                      relief = "sunken", borderwidth = "1",
                      cursor = "cross")
frame.pack()


root.mainloop()




if __name__ == "__main__":
    print("pythonですわぁ")