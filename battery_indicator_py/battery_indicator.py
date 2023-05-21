import tkinter as tk
import psutil


def update_battery_percentage():
    battery = psutil.sensors_battery()
    percent = battery.percent
    battery_label.config(text=f"Battery: {percent}%")
    root.after(1000, update_battery_percentage)


root = tk.Tk()
root.title("Battery Percentage")
root.geometry("150x50")
root.attributes('-topmost', True)
root.attributes('-alpha', 1)  # Set transparency level (0.0 to 1.0)
root.configure(bg='black')  # Set the background color to black

battery_label = tk.Label(root, text="", bg='black', fg='white')  # Set text color to white
battery_label.pack()

update_battery_percentage()
root.mainloop()
