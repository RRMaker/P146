from tkinter import *
root = Tk()
root.title("Fibonacci")
root.geometry("400x400")

enter_num = Entry(root)
label_series = Label(root, text = "Fibonacci Series: ")
label_sum = Label(root, text = "Fibbonacci Sum: ")

def Fibonacci():
    num = int(enter_num.get())
    first_num = 0
    second_num = 1
    sum = 0
    counter = 1
    while(counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_num = second_num
        second_num = sum
        sum = first_num + second_num
        sum2 = 0
        sum2 = sum2 + sum
        label_sum['text'] = "Fibbonaci Sum: " + str(sum2)

button = Button(root, text = "Show Fibonacci Series", command = Fibonacci)

enter_num.pack()
button.pack()
label_series.pack()
label_sum.pack()


root.mainloop()

