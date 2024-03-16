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
        self.left_frame = customtkinter.CTkFrame(self, fg_color="#2dc83f",  width=300, height=600, corner_radius=0)
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
        self.start = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.start, frame_start), image=self.start_img, text="Iniciar", fg_color="#26a635", font=self.font_left, hover_color="#26a635", anchor="w")
        self.start.pack(anchor="sw", ipady=5, pady=(60, 0), padx=(15, 0))

        # Registrar nova aposta
        self.bet_img_data = Image.open("images/dinheiro.png")
        self.bet_img = customtkinter.CTkImage(dark_image=self.bet_img_data, light_image=self.bet_img_data)
        self.register = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.register, frame_register), image=self.bet_img, text="Registar nova aposta", fg_color="transparent", font=self.font_left, hover_color="#26a635", anchor="w")
        self.register.pack(anchor="sw", ipady=5, pady=(10, 0), padx=(15, 0))

        # Listas apostas
        self.list_img_data = Image.open("images/lista-de-itens.png")
        self.list_img = customtkinter.CTkImage(dark_image=self.list_img_data, light_image=self.list_img_data)
        self.list = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.list, frame_list), image=self.list_img, text="Listas apostas", fg_color="transparent", font=self.font_left, hover_color="#26a635", anchor="w")
        self.list.pack(anchor="sw", ipady=5, pady=(10, 0), padx=(15, 0))

        # Finalizar apostas e executar sorteio
        self.draw_prize_img_data = Image.open("images/loteria.png")
        self.draw_prize_img = customtkinter.CTkImage(dark_image=self.draw_prize_img_data, light_image=self.draw_prize_img_data)
        self.draw_prize = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.draw_prize, frame_draw_prize), image=self.draw_prize_img, text="Finalizar apostas", fg_color="transparent", font=self.font_left, hover_color="#26a635", anchor="w")
        self.draw_prize.pack(anchor="sw", ipady=5, pady=(10, 0), padx=(15, 0))

        # Fim da apuração
        self.end_img_data = Image.open("images/fim.png")
        self.end_img = customtkinter.CTkImage(dark_image=self.end_img_data, light_image=self.end_img_data)
        self.end = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.end, frame_end), image=self.end_img, text="Fim da apuração", fg_color="transparent", font=self.font_left, hover_color="#26a635", anchor="w")
        self.end.pack(anchor="sw", ipady=5, pady=(10, 0), padx=(15, 0))

        # Premiação
        self.prize_img_data = Image.open("images/distintivo.png")
        self.prize_img = customtkinter.CTkImage(dark_image=self.prize_img_data, light_image=self.prize_img_data)
        self.prize = customtkinter.CTkButton(self.left_frame, command = lambda: self.selected(self.prize, frame_prize), image=self.prize_img, text="Premiação", fg_color="transparent", font=self.font_left, hover_color="#26a635", anchor="w")
        self.prize.pack(anchor="sw", ipady=5, pady=(10, 0), padx=(15, 0))

         # Frames

        self.right_frames = customtkinter.CTkFrame(self, fg_color="#fff",  width=700, height=600, corner_radius=0)
        self.right_frames.pack_propagate(0)
        self.right_frames.pack(side="left")

        # Frame - Iniciar
        
        def frame_start(self):
            self.frame_start = customtkinter.CTkFrame(self.right_frames, fg_color="#fff",  width=700, height=600, corner_radius=0)
            self.frame_start.pack_propagate(0)
            self.frame_start.pack(side="left")

            self.title_start = customtkinter.CTkFrame(master=self.frame_start, fg_color="transparent")
            self.title_start.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

            customtkinter.CTkLabel(self.title_start, text="Iniciar", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")

        # Frame - Registrar nova aposta
        def frame_register(self):
            self.frame_register = customtkinter.CTkFrame(self.right_frames, fg_color="#fff",  width=700, height=600, corner_radius=0)
            self.frame_register.pack_propagate(0)
            self.frame_register.pack(side="left")

            self.title_register = customtkinter.CTkFrame(master=self.frame_register, fg_color="transparent")
            self.title_register.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

            customtkinter.CTkLabel(self.title_register, text="Registrar nova aposta", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")

        # Frame - Listas apostas
        def frame_list(self):
            self.frame_list = customtkinter.CTkFrame(self.right_frames, fg_color="#fff",  width=700, height=600, corner_radius=0)
            self.frame_list.pack_propagate(0)
            self.frame_list.pack(side="left")

            self.title_list = customtkinter.CTkFrame(master=self.frame_list, fg_color="transparent")
            self.title_list.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

            customtkinter.CTkLabel(self.title_list, text="Listas apostas", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")

        # Frame - Finalizar apostas e executar sorteio
        def frame_draw_prize(self):
            self.frame_draw_prize = customtkinter.CTkFrame(self.right_frames, fg_color="#fff",  width=700, height=600, corner_radius=0)
            self.frame_draw_prize.pack_propagate(0)
            self.frame_draw_prize.pack(side="left")

            self.title_draw_prize = customtkinter.CTkFrame(master=self.frame_draw_prize, fg_color="transparent")
            self.title_draw_prize.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

            customtkinter.CTkLabel(self.title_draw_prize, text="Finalizar apostas", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")

        # Frame - Fim da apuração
        def frame_end(self):
            self.frame_end = customtkinter.CTkFrame(self.right_frames, fg_color="#fff",  width=700, height=600, corner_radius=0)
            self.frame_end.pack_propagate(0)
            self.frame_end.pack(side="left")

            self.title_end = customtkinter.CTkFrame(master=self.frame_end, fg_color="transparent")
            self.title_end.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

            customtkinter.CTkLabel(self.title_end, text="Fim da apuração", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")

        # Frame - Premiação
        def frame_prize(self):
            self.frame_prize = customtkinter.CTkFrame(self.right_frames, fg_color="#fff",  width=700, height=600, corner_radius=0)
            self.frame_prize.pack_propagate(0)
            self.frame_prize.pack(side="left")

            self.title_prize = customtkinter.CTkFrame(master=self.frame_prize, fg_color="transparent")
            self.title_prize.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

            customtkinter.CTkLabel(self.title_prize, text="Premiação", font=self.font_titles, text_color="#2A8C55").pack(anchor="nw", side="left")

        frame_start(self)


    def diselected(self):
        self.start.configure(fg_color="transparent")
        self.register.configure(fg_color="transparent")
        self.list.configure(fg_color="transparent")
        self.draw_prize.configure(fg_color="transparent")
        self.end.configure(fg_color="transparent")
        self.prize.configure(fg_color="transparent")
        for frame in self.right_frames.winfo_children():
            frame.destroy()
            self.update()

    def selected(self, but, frame):
        self.diselected()
        but.configure(fg_color="#26a635")
        frame(self)

