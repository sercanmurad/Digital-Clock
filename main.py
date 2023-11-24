import tkinter as tk
import time

#Function for uptade the label text with the current time
def time_uptade():
    current_time=time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, time_uptade)#uptade every 1 second

#Crete the main screen
root = tk.Tk()
root.title("Digital Clock")
#Crete a label to display a time
clock_label=tk.Label(root,text="",font=("Caribi",48))
clock_label.pack(padx=20, pady=20)
#Call the function
time_uptade()

#start the root
root.mainloop()
