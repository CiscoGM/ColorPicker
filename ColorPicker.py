import tkinter as tk
import math

class ColorPickerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Color Picker")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.color_label = tk.Label(self.root, text="Selecciona un color", font=("Arial", 16))
        self.color_label.pack(pady=10)
        self.color_display = tk.Label(self.root, width=30, height=10, relief=tk.SOLID)
        self.color_display.pack(pady=10)
        self.copy_button = tk.Button(self.root, text="Copiar", command=self.copy_color)
        self.copy_button.pack(pady=5)
        self.draw_color_circle()
        self.canvas.bind("<Button-1>", self.pick_color)
        self.root.mainloop()

    def draw_color_circle(self):
        radius = 150
        center_x = 200
        center_y = 200
        for angle in range(0, 360):
            color = self.get_hex_color(angle)
            start_x = center_x - radius
            start_y = center_y - radius
            end_x = center_x + radius
            end_y = center_y + radius
            self.canvas.create_arc(start_x, start_y, end_x, end_y, fill=color, outline="", start=angle, extent=1)
        self.canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="black")

    def get_hex_color(self, angle):
        color = "#"
        angle = angle % 360
        red = int((1 + math.cos(math.radians(angle))) / 2 * 255)
        green = int((1 + math.cos(math.radians(angle + 120))) / 2 * 255)
        blue = int((1 + math.cos(math.radians(angle + 240))) / 2 * 255)
        color += f"{red:02x}{green:02x}{blue:02x}"
        return color

    def pick_color(self, event):
        x = event.x
        y = event.y
        center_x = 200
        center_y = 200
        distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
        if distance <= 150:
            angle = math.degrees(math.atan2(y - center_y, x - center_x))
            if angle < 0:
                angle += 360
            color = self.get_hex_color(int(angle))
            self.color_label.config(text=color)
            self.color_display.config(bg=color)

    def copy_color(self):
        if hasattr(self, "color_to_copy"):
            self.root.clipboard_clear()
            self.root.clipboard_append(self.color_to_copy)
            self.root.update()

if __name__ == "__main__":
    app = ColorPickerApp()
