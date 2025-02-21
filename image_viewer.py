import os
import tkinter as tk
from tkinter import filedialog, Label, Button, Frame
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")  # Light gray background

        self.image_list = []
        self.image_index = 0

        # Title
        self.title_label = Label(root, text="Image Viewer", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Image Frame
        self.image_frame = Frame(root, bg="white", width=600, height=400, relief="solid", borderwidth=2)
        self.image_frame.pack(pady=10)

        self.image_label = Label(self.image_frame, bg="white")
        self.image_label.pack(expand=True)

        # Buttons Frame
        self.button_frame = Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.prev_button = Button(self.button_frame, text="⏪ Previous", command=self.prev_image, font=("Arial", 12), bg="#3498db", fg="white", padx=10, pady=5)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.load_button = Button(self.button_frame, text="📂 Load Images", command=self.load_images, font=("Arial", 12, "bold"), bg="#2ecc71", fg="white", padx=10, pady=5)
        self.load_button.grid(row=0, column=1, padx=10)

        self.next_button = Button(self.button_frame, text="Next ⏩", command=self.next_image, font=("Arial", 12), bg="#3498db", fg="white", padx=10, pady=5)
        self.next_button.grid(row=0, column=2, padx=10)

        self.exit_button = Button(root, text="❌ Exit", command=root.quit, font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", padx=10, pady=5)
        self.exit_button.pack(pady=10)

    def load_images(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.image_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))]
            if self.image_list:
                self.image_index = 0
                self.display_image()
            else:
                self.image_label.config(text="No images found", font=("Arial", 14, "bold"), fg="red")

    def display_image(self):
        if self.image_list:
            image_path = self.image_list[self.image_index]
            image = Image.open(image_path)
            image = image.resize((600, 400), Image.LANCZOS)
            self.tk_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.tk_image)
            self.image_label.image = self.tk_image

    def next_image(self):
        if self.image_list and self.image_index < len(self.image_list) - 1:
            self.image_index += 1
            self.display_image()

    def prev_image(self):
        if self.image_list and self.image_index > 0:
            self.image_index -= 1
            self.display_image()

# Run the application
root = tk.Tk()
app = ImageViewer(root)
root.mainloop()
