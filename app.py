from database import User, Bet, Rounds, Draw_Prize, Draw_Prize_Winners_Relationship
from CTkTable import CTkTable
from CTkMessagebox import CTkMessagebox
import customtkinter

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
        self.font_titles = customtkinter.CTkFont(family="Arial", size=35, weight="bold")
        self.font_sub = customtkinter.CTkFont(family="Arial", size=20)
        self.font_table = customtkinter.CTkFont(family="Arial", size=10)


        # tiltes
        self.titles = ["Iniciar", "Registrar nova aposta", "Lista apostas", "Finalizar apostas e executar o sorteio", "Fim da apuração", "Premiação"]
        for i in self.titles:
            customtkinter.CTkLabel(master=self.tab(i), font=self.font_titles, text=i).grid(row=0, column=0, padx=20, pady=10)


        # Iniciar tab
        # draw prize number
        self.draw_price_number_data = Draw_Prize.select().count()
        self.draw_prize_number = customtkinter.CTkLabel(master=self.tab(self.titles[0]), font=self.font_sub, text=f"Sorteio nº: {self.draw_price_number_data}")
        if self.draw_price_number_data == 0:
            self.draw_prize_number.configure(text="Nenhum sorteio criado")
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
        # Name
        self.name_input = customtkinter.CTkEntry(master=self.tab(self.titles[1]), placeholder_text="Nome e Sobrenome do Apostador", width=210)
        self.name_input.grid(row=1, column=0, padx=20, pady=10, sticky="sw")
        # Cpf
        self.cpf_input = customtkinter.CTkEntry(master=self.tab(self.titles[1]), placeholder_text="Cpf do Apostador", width=210)
        self.cpf_input.grid(row=2, column=0, padx=20, pady=10, sticky="sw")
        # Add user Button
        self.new_a = customtkinter.CTkButton(master=self.tab(self.titles[1]), text="+ Adicionar Apostador", command=self.new_user)
        self.new_a.grid(row=3, column=0, padx=20, pady=10, sticky="sw")
        # Remove user Button
        self.remove_a = customtkinter.CTkButton(master=self.tab(self.titles[1]), text="- Remover Apostador (Sò precisa informar cpf)", command=self.remove_user)
        self.remove_a.grid(row=4, column=0, padx=20, pady=10, sticky="sw")
        # Combo box
        self.user_values = []
        self.state_choices = "readonly"
        for i in User.select():
            self.user_values.append(f"{i.name}, {i.cpf}")
        if not self.user_values:
            self.state_choices = "disabled"
        self.choices = customtkinter.CTkComboBox(master=self.tab(self.titles[1]), values=self.user_values, state=self.state_choices, width=230)
        self.choices.grid(row=1, column=1, padx=20, pady=10, sticky="sw")
        if User.select().count() != 0:
            self.last_user = User.get_by_id(User.select().count())
            self.choices.set(f"{self.last_user.name}, {self.last_user.cpf}")
        # Bet Numbers
        self.number_text = customtkinter.CTkLabel(master=self.tab(self.titles[1]), text="Digite os 5 números (sobre os números de 1 a 50)")
        self.number_text.grid(row=2, column=1, padx=20, pady=10, sticky="sw")
        self.number_fields = customtkinter.CTkFrame(master=self.tab(self.titles[1]))
        self.number_fields.grid(row=3, column=1, padx=20, pady=10, sticky="sw")
        self.n1 = customtkinter.CTkEntry(master=self.number_fields, placeholder_text="Num1", width=50)
        self.n1.grid(row=1, column=0, sticky="sw")
        self.n2 = customtkinter.CTkEntry(master=self.number_fields, placeholder_text="Num2", width=50)
        self.n2.grid(row=1, column=1, sticky="sw")
        self.n3 = customtkinter.CTkEntry(master=self.number_fields, placeholder_text="Num3", width=50)
        self.n3.grid(row=1, column=2, sticky="sw")
        self.n4 = customtkinter.CTkEntry(master=self.number_fields, placeholder_text="Num4", width=50)
        self.n4.grid(row=1, column=3, sticky="sw")
        self.n5 = customtkinter.CTkEntry(master=self.number_fields, placeholder_text="Num5", width=50)
        self.n5.grid(row=1, column=4, sticky="sw")
        self.add_bet = customtkinter.CTkButton(master=self.tab(self.titles[1]), text="+ Adicionar Aposta")
        self.add_bet.grid(row=4, column=1, padx=20, pady=10, sticky="sw")


        # Lista apostas tab
        self.table_data = [
                ["Numero do Sorteio", "Nome", "Cpf", "Números"]
            ]

        for i in Bet.select():
            numbers = [i.first, i.second, i.third, i.fourth, i.fifth]
            data = [i.register_number, i.user.name, i.user.cpf, numbers]
            self.table_data.append(data)

        self.table_frame = customtkinter.CTkScrollableFrame(master=self.tab(self.titles[2]), width=600)
        self.table_frame.grid(row=0, column=0, padx=20, pady=20)
        self.table = CTkTable(master=self.table_frame, values=self.table_data)
        self.table.pack()  
      
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
        self.new_d.configure(state="disabled")
        CTkMessagebox(title="Sucesso", icon="check", message="Sorteio criado com sucesso!\n\nOBS: Você só poderá criar outro sorteio após a finalização do sorteio atual.")


    def field_verification(self):
        if len(self.cpf_input.get()) != 11:
            CTkMessagebox(title="Erro", message="O cpf deve exatos 11 números!!!", icon="cancel")
        elif not self.cpf_input.get().isnumeric():
            CTkMessagebox(title="Erro", message="O cpf deve conter apenas números!!!", icon="cancel")
        else:
            return True
        return False
    
    
    def refresh_combobox(self):
        self.new_user_values = []
        for i in User.select():
            self.new_user_values.append(f"{i.name}, {i.cpf}")
        self.choices.configure(values=self.new_user_values, state="readonly")
        self.choices.set(f"{self.name_input.get()}, {self.cpf_input.get()}")


    def new_user(self):
        if self.field_verification():
            user_cpf_repeated = False
            for i in User.select():
                if(self.cpf_input.get() == i.cpf):
                    user_cpf_repeated = True    
                    break
            if user_cpf_repeated:
                CTkMessagebox(title="Erro", message="Já existe um apostador com este cpf!!!", icon="cancel")
            elif self.name_input.get().isnumeric():
                CTkMessagebox(title="Erro", message="O nome deve conter apenas letras!!!", icon="cancel")
            elif self.name_input.get() == "":
                CTkMessagebox(title="Erro", message="O nome não pode ser vazio!!!", icon="cancel")
            else:
                User.create(name=self.name_input.get(), cpf=str(self.cpf_input.get()))
                CTkMessagebox(title="Sucesso", icon="check", message="O apostador foi criado com sucesso!")
                self.refresh_combobox()
            

    def remove_user(self):
        if self.field_verification():
            try: User.get(User.cpf == self.cpf_input.get())
            except:
                CTkMessagebox(title="Erro", message="O apostador não foi encontrado!!!", icon="cancel")
            finally:
                self.user_deleted = User.get(User.cpf == self.cpf_input.get())
                User.delete_by_id(self.user_deleted.id)
                self.refresh_combobox()
                if User.select().count() == 0:
                    self.choices.configure(values="")
                    self.choices.set("")
                    self.choices.configure(state="disabled")
                else:
                    self.before_user_deleted = User.get_by_id(User.select().count())
                    self.choices.set(f"{self.before_user_deleted.name}, {self.before_user_deleted.cpf}")
                CTkMessagebox(title="Sucesso", icon="check", message="O apostador foi removido com sucesso!")
                
        
    
    
