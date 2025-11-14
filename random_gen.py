import tkinter as tk
import random


class RandomGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Number Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Title Label
        self.title_label = tk.Label(
            root, 
            text="Random Number Generator",
            font=("Arial", 18, "bold"),
            pady=20
        )
        self.title_label.pack()
        
        # Display label for random number
        self.number_label = tk.Label(
            root,
            text="Press the button to generate",
            font=("Arial", 24),
            fg="blue",
            pady=30
        )
        self.number_label.pack()
        
        # Generate button
        self.generate_button = tk.Button(
            root,
            text="Generate Random Number",
            font=("Arial", 14),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            command=self.generate_random_number
        )
        self.generate_button.pack(pady=20)
        
        # Range info label
        self.info_label = tk.Label(
            root,
            text="Range: 1 - 100",
            font=("Arial", 10),
            fg="gray"
        )
        self.info_label.pack()
    
    def generate_random_number(self):
        """Generate and display a random number"""
        random_num = random.randint(1, 100)
        self.number_label.config(text=str(random_num))


def main():
    root = tk.Tk()
    app = RandomGeneratorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
