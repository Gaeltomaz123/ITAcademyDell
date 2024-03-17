from database import User, Bet, Rounds, Draw_Prize, Draw_Prize_Winners_Relationship
from CTkTable import CTkTable
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("TheLuckyGame")
        self.tab_view = Tab(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)
        self.resizable(width=False, height=False)


class Tab(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # tabs
        self.add("Iniciar")
        self.add("Registrar nova aposta")
        self.add("Lista apostas")
        self.add("Finalizar apostas e executar o sorteio")
        self.add("Fim da apuração")
        self.add("Premiação")

        # fonts
        self.font_left = customtkinter.CTkFont(family="Arial", size=15, weight="bold")
        self.font_titles = customtkinter.CTkFont(family="Arial", size=35, weight="bold")
        self.font_sub = customtkinter.CTkFont(family="Arial", size=20)
        self.font_table = customtkinter.CTkFont(family="Arial", size=10)

        # tiltes
        self.titles = ["Iniciar", "Registrar nova aposta", "Lista apostas", "Finalizar apostas e executar o sorteio", "Fim da apuração", "Premiação"]
        for i in self.titles:
            customtkinter.CTkLabel(master=self.tab(i), font=self.font_titles, text=i).grid(row=0, column=0, padx=20, pady=10)

        # Iniciar tab
        # draw prize number
        self.draw_prize_number = customtkinter.CTkLabel(master=self.tab(self.titles[0]), font=self.font_sub, text=f"Sorteio nº: {Draw_Prize.select().count()}")
        self.draw_prize_number.grid(row=0, column=1, padx=20, pady=10, sticky="sw")
        # table button
        self.table_btn = customtkinter.CTkButton(master=self.tab(self.titles[0]), text="Abrir Tabela de Sorteios", command=self.table_window)
        self.table_btn.grid(row=1, column=1, padx=20, pady=10, sticky="sw")
        # new draw prize
        self.state_new_d = customtkinter.NORMAL
        for i in Draw_Prize.select():
            if i.finished == False:
                self.state_new_d = customtkinter.DISABLED
        self.new_d = customtkinter.CTkButton(master=self.tab(self.titles[0]), text="+ Novo Sorteio", command=self.new_draw_prize, state=self.state_new_d)
        self.new_d.grid(row=2, column=1, padx=20, pady=10, sticky="sw")

        # Registrar nova aposta tab

        # Lista apostas tab
      
        # Finalizar apostas e executar o sorteio tab
        
        # Fim da apuração tab
        
        # Premiação

    def table_window(self):
        self.window = customtkinter.CTkToplevel()
        self.window.resizable(width=False, height=False)
        self.table_data = [
                ["Número do Sorteio", "Rodadas", "Numeros Sorteados", "Finalizado", "Vencedores"]
            ]

        for i in Draw_Prize.select():
            winners = []
            numbers = [i.first, i.second, i.third, i.fourth, i.fifth]
            for j in Draw_Prize_Winners_Relationship.select():
                if i.id == j.draw_prize.id:
                    winners.append(f"[{j.user.name}]")
            winners.sort()
            finished = ""
            if i.finished:
                finished = "Sim"
            else:
                finished = "Não"
                winners = "-"
                numbers = "-"
            data = [i.id, i.rounds, numbers, finished, winners]
            self.table_data.append(data)

        self.table_frame = customtkinter.CTkScrollableFrame(self.window, width=700)
        self.table_frame.grid(row=0, column=0, padx=20, pady=20)
        self.table = CTkTable(self.table_frame, values=self.table_data)
        self.table.pack()  

    def new_draw_prize(self):
        Draw_Prize.create()
        self.draw_prize_number.configure(text=f"Sorteio nº: {Draw_Prize.select().count()}")
        self.new_d.configure(state=customtkinter.DISABLED)
        self.table_window()
    
    
