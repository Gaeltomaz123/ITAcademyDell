import customtkinter
from PIL import Image

# Setting themes
customtkinter.set_appearance_mode("white")

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
        
        # Fonts
        self.font_left = customtkinter.CTkFont(family="Arial", size=15, weight="bold")
        self.font_titles = customtkinter.CTkFont(family="Arial", size=50, weight="bold")
        
        # Left Frame
        self.left_frame = customtkinter.CTkFrame(self, fg_color="#2A8C55",  width=300, height=600, corner_radius=0)
        self.left_frame.pack_propagate(0)
        self.left_frame.pack(fill="y", anchor="w", side="left")

        # Logo
        self.logo_img_data = Image.open("images/pngegg.png")
        self.logo_img = customtkinter.CTkImage(dark_image=self.logo_img_data, light_image=self.logo_img_data, size=(77.68, 85.42))
        self.logo = customtkinter.CTkLabel(self.left_frame, text="", image=self.logo_img)
        self.logo.pack(pady=(38, 0), anchor="center")

        # Iniciar
        self.start_img_data = Image.open("images/botao-play.png")
        self.start_img = customtkinter.CTkImage(dark_image=self.start_img_data, light_image=self.start_img_data)
        self.start = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.start, self.start_page), image=self.start_img, text="Iniciar", fg_color="#207244", font=self.font_left, hover_color="#207244", anchor="w")
        self.start.pack(anchor="sw", ipady=5, pady=(60, 0), padx=(15, 0))

        # Registrar nova aposta
        self.bet_img_data = Image.open("images/dinheiro.png")
        self.bet_img = customtkinter.CTkImage(dark_image=self.bet_img_data, light_image=self.bet_img_data)
        self.register = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.register, self.register_page), image=self.bet_img, text="Registar nova aposta", fg_color="transparent", font=self.font_left, hover_color="#207244", anchor="w")
        self.register.pack(anchor="sw", ipady=5, pady=(10, 0), padx=(15, 0))

        # Listas apostas
        self.list_img_data = Image.open("images/lista-de-itens.png")
        self.list_img = customtkinter.CTkImage(dark_image=self.list_img_data, light_image=self.list_img_data)
        self.list = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.list), image=self.list_img, text="Listas apostas", fg_color="transparent", font=self.font_left, hover_color="#207244", anchor="w")
        self.list.pack(anchor="sw", ipady=5, pady=(10, 0), padx=(15, 0))

        # Finalizar apostas e executar sorteio
        self.draw_prize_img_data = Image.open("images/loteria.png")
        self.draw_prize_img = customtkinter.CTkImage(dark_image=self.draw_prize_img_data, light_image=self.draw_prize_img_data)
        self.draw_prize = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.draw_prize), image=self.draw_prize_img, text="Finalizar apostas", fg_color="transparent", font=self.font_left, hover_color="#207244", anchor="w")
        self.draw_prize.pack(anchor="sw", ipady=5, pady=(10, 0), padx=(15, 0))

        # Fim da apuração
        self.end_img_data = Image.open("images/fim.png")
        self.end_img = customtkinter.CTkImage(dark_image=self.end_img_data, light_image=self.end_img_data)
        self.end = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.end), image=self.end_img, text="Fim da apuração", fg_color="transparent", font=self.font_left, hover_color="#207244", anchor="w")
        self.end.pack(anchor="sw", ipady=5, pady=(10, 0), padx=(15, 0))

        # Premiação
        self.prize_img_data = Image.open("images/distintivo.png")
        self.prize_img = customtkinter.CTkImage(dark_image=self.prize_img_data, light_image=self.prize_img_data)
        self.prize = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.prize), image=self.prize_img, text="Premiação", fg_color="transparent", font=self.font_left, hover_color="#207244", anchor="w")
        self.prize.pack(anchor="sw", ipady=5, pady=(10, 0), padx=(15, 0))

        # Frames
        # Frame - Iniciar
        

        # Frame - Registrar nova aposta
        
        # Frame - Listas apostas
        frame_iniciar = customtkinter.CTkFrame(self, fg_color="#fff",  width=700, height=600, corner_radius=0)
        frame_iniciar.pack_propagate(0)
        frame_iniciar.pack(side="left")

        title_frame = customtkinter.CTkFrame(master=frame_iniciar, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

        customtkinter.CTkLabel(master=title_frame, text="Listas apostas", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")

        # Frame - Finalizar apostas e executar sorteio
        frame_iniciar = customtkinter.CTkFrame(self, fg_color="#fff",  width=700, height=600, corner_radius=0)
        frame_iniciar.pack_propagate(0)
        frame_iniciar.pack(side="left")

        title_frame = customtkinter.CTkFrame(master=frame_iniciar, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

        customtkinter.CTkLabel(master=title_frame, text="Finalizar apostas e executar sorteio", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")

        # Frame - Fim da apuração
        frame_iniciar = customtkinter.CTkFrame(self, fg_color="#fff",  width=700, height=600, corner_radius=0)
        frame_iniciar.pack_propagate(0)
        frame_iniciar.pack(side="left")

        title_frame = customtkinter.CTkFrame(master=frame_iniciar, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

        customtkinter.CTkLabel(master=title_frame, text="Fim da apuração", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")

        # Frame - Premiação
        frame_iniciar = customtkinter.CTkFrame(self, fg_color="#fff",  width=700, height=600, corner_radius=0)
        frame_iniciar.pack_propagate(0)
        frame_iniciar.pack(side="left")

        title_frame = customtkinter.CTkFrame(master=frame_iniciar, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

        customtkinter.CTkLabel(master=title_frame, text="Premiação", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")


    def diselected(self):
        self.start.configure(fg_color="transparent")
        self.register.configure(fg_color="transparent")
        self.list.configure(fg_color="transparent")
        self.draw_prize.configure(fg_color="transparent")
        self.end.configure(fg_color="transparent")
        self.prize.configure(fg_color="transparent")

    def selected(self, but):
        self.diselected()
        but.configure(fg_color="#207244")

    def start_page(self):
        self.frame_iniciar = customtkinter.CTkFrame(self, fg_color="#fff",  width=700, height=600, corner_radius=0)
        self.frame_iniciar.pack_propagate(0)
        self.frame_iniciar.pack(side="left")

        title_frame = customtkinter.CTkFrame(master=self.frame_iniciar, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

        customtkinter.CTkLabel(master=title_frame, text="Iniciar", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")

    def register_page(self):
        self.frame_iniciar = customtkinter.CTkFrame(self, fg_color="#fff",  width=700, height=600, corner_radius=0)
        self.frame_iniciar.pack_propagate(0)
        self.frame_iniciar.pack(side="left")

        title_frame = customtkinter.CTkFrame(master=self.frame_iniciar, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

        customtkinter.CTkLabel(master=title_frame, text="Registrar nova aposta", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")



        ''' Label
        self.label = customtkinter.CTkLabel(self.left_frame, text="Clicks: 0")
        self.label.pack(anchor="s", expand=True, pady=10)

        # Button
        self.button = customtkinter.CTkButton(self.left_frame, corner_radius=32, command=self.test)
        self.button.pack(anchor="n", expand=True)

    def test(self):
        self.count += 1
        self.label.configure(text=f"Clicks: {self.count}") '''


