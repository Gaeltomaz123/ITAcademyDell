import customtkinter

# Setting themes
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green") 

# Creating window
app = customtkinter.CTk()
app.title("TheLuckyGame")
app.geometry("1000x600")
app.iconbitmap("images/clover.ico")

count = 0

def test():
    global count
    count += 1
    label.configure(text=f"Clicks: {count}")

label = customtkinter.CTkLabel(app, text="Clicks: 0")
button = customtkinter.CTkButton(app, corner_radius=32, command=test)
#button.place(relx=0.5, rely=0.5, anchor="center")
label.pack(anchor="s", expand=True, pady=10)
button.pack(anchor="n", expand=True)

app.mainloop()