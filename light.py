# 写的时候没写注释
import tkinter as tk
import time

class TrafficLightSimulator:
    def __init__(self, master):
        self.master = master
        self.manual_mode = False
        master.title("Traffic Light Simulator")

        self.canvas = tk.Canvas(master, width=200, height=400)
        self.canvas.pack()

        self.red_light = self.canvas.create_oval(50, 50, 150, 150, fill="grey")
        self.yellow_light = self.canvas.create_oval(50, 150, 150, 250, fill="grey")
        self.green_light = self.canvas.create_oval(50, 250, 150, 350, fill="grey")

        self.manual_mode_button = tk.Button(master, text="Enter Manual Mode", command=self.toggle_manual_mode)
        self.manual_mode_button.pack()

        self.red_button = tk.Button(master, text="Red", command=lambda: self.toggle_light("red"))
        self.yellow_button = tk.Button(master, text="Yellow", command=lambda: self.toggle_light("yellow"))
        self.green_button = tk.Button(master, text="Green", command=lambda: self.toggle_light("green"))

        self.change_light()

    def toggle_manual_mode(self):
        self.manual_mode = not self.manual_mode
        if self.manual_mode:
            self.manual_mode_button.config(text="Exit Manual Mode")
            self.red_button.pack()
            self.yellow_button.pack()
            self.green_button.pack()
            self.stop_all_lights()
        else:
            self.manual_mode_button.config(text="Enter Manual Mode")
            self.red_button.pack_forget()
            self.yellow_button.pack_forget()
            self.green_button.pack_forget()
            self.stop_all_lights()
            self.change_light()

    def toggle_light(self, color):
        current_color = self.canvas.itemcget(getattr(self, color + "_light"), "fill")
        new_color = "grey" if current_color != "grey" else color
        self.canvas.itemconfig(getattr(self, color + "_light"), fill=new_color)

    def change_light(self):
        if not self.manual_mode:
            self.turn_on_green()
            self.master.after(17000, self.blink_green)

    def blink_green(self):
        if not self.manual_mode:
            for _ in range(3):
                self.canvas.itemconfig(self.green_light, fill="green")
                self.master.update()
                time.sleep(1)
                self.canvas.itemconfig(self.green_light, fill="grey")
                self.master.update()
                time.sleep(1)
            self.blink_yellow()

    def blink_yellow(self):
        if not self.manual_mode:
            for _ in range(3):
                self.canvas.itemconfig(self.yellow_light, fill="yellow")
                self.master.update()
                time.sleep(1)
                self.canvas.itemconfig(self.yellow_light, fill="grey")
                self.master.update()
                time.sleep(1)
            self.turn_on_red()

    def turn_on_green(self):
        self.canvas.itemconfig(self.red_light, fill="grey")
        self.canvas.itemconfig(self.green_light, fill="green")

    def turn_on_red(self):
        self.canvas.itemconfig(self.green_light, fill="grey")
        self.canvas.itemconfig(self.yellow_light, fill="grey")
        self.canvas.itemconfig(self.red_light, fill="red")
        self.master.after(30000, self.change_light)

    def stop_all_lights(self):
        self.canvas.itemconfig(self.red_light, fill="grey")
        self.canvas.itemconfig(self.yellow_light, fill="grey")
        self.canvas.itemconfig(self.green_light, fill="grey")

root = tk.Tk()
traffic_light = TrafficLightSimulator(root)
root.mainloop()

