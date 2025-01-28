from tkinter import *
from tkinter import ttk

from bubbleSort import bubble_sort
from insertionSort import insertion_sort
from selectionSort import selection_sort
from mergeSort import merge_sort
from quickSort import quick_sort


root = Tk()
root.title('Sorting Algorithm Visualizer')
root.geometry("850x600")
root.config(bg='#2b2b2b') 
select_algorithm = StringVar()
arr = []

def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 850
    bar_width = canvas_width / (len(arr) + 1)
    border_offset = 30
    spacing = 5
    normalized_array = [i / max(arr) for i in arr]
    for i, height in enumerate(normalized_array):
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height * 340
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="#2b2b2b")
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(arr[i]), fill="#ffffff") 

    root.update_idletasks()

def sorting():
    global arr
    algorithm = select_algorithm.get()
    if algorithm == "Bubble Sort":
        bubble_sort(arr, drawrectangle, sortingspeed.get())
    elif algorithm == "Insertion Sort":
        insertion_sort(arr, drawrectangle, sortingspeed.get())
    elif algorithm == "Selection Sort":
        selection_sort(arr, drawrectangle, sortingspeed.get())
    elif algorithm == "Merge Sort":
        merge_sort(arr, drawrectangle, sortingspeed.get())
    elif algorithm == "Quick Sort":
        quick_sort(arr, drawrectangle, sortingspeed.get())

def set_user_array(input_str):
    global arr
    try:
        arr = list(map(int, input_str.split(',')))
        drawrectangle(arr, ['#ff6f61' for _ in range(len(arr))])
    except ValueError:
        print("Please enter comma-separated array elements.")


options_frame = Frame(root, width=850, height=200, bg='#3c3f41')
options_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=850, height=380, bg='#1e1e1e', highlightbackground='#3c3f41')
canvas.grid(row=1, column=0, padx=10, pady=5)


Label(options_frame, text="Algorithm Choice:", bg='#3c3f41', fg='white', font=('Helvetica', 12)).grid(row=0, column=0, padx=10, pady=10)

algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm, values=['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort'], width=15, font=('Helvetica', 10))
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

# Sorting Speed Slider
sortingspeed = Scale(options_frame, from_=0.1, to=2.0, length=150, digits=2, resolution=0.1, orient=HORIZONTAL, label="Control Speed", bg='#3c3f41', fg='white', troughcolor='#ff6f61', font=('Helvetica', 10))
sortingspeed.grid(row=0, column=2, padx=10, pady=10)

# Start Sorting Button
Button(options_frame, text="Start Sorting", command=sorting, bg='#ff6f61', fg='white', font=('Helvetica', 12), height=2, width=15, relief=RAISED).grid(row=0, column=3, padx=5, pady=5)

# User Input for Array
Label(options_frame, text="Enter Array Elements:", bg='#3c3f41', fg='white', font=('Helvetica', 12)).grid(row=1, column=0, padx=10, pady=10)
user_input = Entry(options_frame, width=40, font=('Helvetica', 10))
user_input.grid(row=1, column=1, padx=5, pady=5)
Button(options_frame, text="Set Array Elements", command=lambda: set_user_array(user_input.get()), bg='#5cb85c', fg='white', font=('Helvetica', 12), height=2, width=15, relief=RAISED).grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
