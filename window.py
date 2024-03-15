from customtkinter import *

# Setting themes
set_appearance_mode("white")
set_default_color_theme("green") 

# Creating window
app = CTk()
app.title("TheLuckyGame")
app.geometry("1000x600")
app.iconbitmap("images/clover.ico")
app.resizable(width=False, height=False)

count = 0

def test():
    global count
    count += 1
    label.configure(text=f"Clicks: {count}")

# Objects inside app
label = CTkLabel(app, text="Clicks: 0")
button = CTkButton(app, corner_radius=32, command=test)
label.pack(anchor="s", expand=True, pady=10)
button.pack(anchor="n", expand=True)

app.mainloop()