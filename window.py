import customtkinter

# Setting themes
customtkinter.set_appearance_mode("white")
customtkinter.set_default_color_theme("green") 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.count = 0

        # Creating window
        self.title("TheLuckyGame")
        self.geometry("1000x600")
        self.iconbitmap("images/clover.ico")
        self.resizable(width=False, height=False)

        # Objects inside app
        self.label = customtkinter.CTkLabel(self, text="Clicks: 0")
        self.button = customtkinter.CTkButton(self, corner_radius=32, command=self.test)
        self.label.pack(anchor="s", expand=True, pady=10)
        self.button.pack(anchor="n", expand=True)

    def test(self):
        self.count += 1
        self.label.configure(text=f"Clicks: {self.count}")


