import random
import time
from database import User, Bet, Draw_Prize, Draw_Prize_Winners_Relationship
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

        self.actual_draw_prize = 0
        if Draw_Prize.select().count() > 0:
            self.actual_draw_prize = Draw_Prize.get_by_id(Draw_Prize.select().count())

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
        self.draw_prize_number_data = Draw_Prize.select().count()
        self.draw_prize_number = customtkinter.CTkLabel(master=self.tab(self.titles[0]), font=self.font_sub, text=f"Sorteio nº: {self.draw_prize_number_data}")
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
        self.choices.set("")
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
        self.buttons_frame = customtkinter.CTkFrame(master=self.tab(self.titles[1]))
        self.buttons_frame.grid(row=4, column=1, padx=20, pady=10, sticky="sw")
        self.add_bet = customtkinter.CTkButton(master=self.buttons_frame, text="+ Adicionar Aposta", command=self.add_bet)
        self.add_bet.grid(row=0, column=0, padx=(0, 10), sticky="sw")
        self.surprise_bet = customtkinter.CTkButton(master=self.buttons_frame, text="Aposta surpresinha", command=self.surprise_bet)
        self.surprise_bet.grid(row=0, column=1, padx=(10, 0), sticky="sw")


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
        # title
        self.final_text = customtkinter.CTkLabel(master=self.tab(self.titles[3]), font=self.font_sub, text=f"Deseja finalizar as apostas e iniciar o Sorteio nº{self.draw_prize_number_data}?")
        self.final_text.grid(row=1, column=0, padx=20, pady=10, sticky="sw")
        # rounds
        self.round = customtkinter.CTkLabel(master=self.tab(self.titles[3]), text="Rodada: 0")
        # numbers
        self.draw_prize_numbers = customtkinter.CTkLabel(master=self.tab(self.titles[3]), text=f"Números Sorteados: -")
        if self.draw_prize_number_data > 0:
            self.draw_prize_numbers.configure(text=f"Números Sorteados: {self.actual_draw_prize.numbers}")
            self.round.configure(text=f"Round: {self.actual_draw_prize.rounds}")
        self.round.grid(row=2, column=0, padx=20, pady=10, sticky="sw")
        self.draw_prize_numbers.grid(row=3, column=0, padx=20, pady=10, sticky="sw")
        # execute draw_prize button
        self.final_but = customtkinter.CTkButton(master=self.tab(self.titles[3]), text="Executar Sorteio", command=self.start_draw_prize)
        if self.draw_prize_number_data > 0:
            if self.actual_draw_prize.numbers != "-":
                self.final_but.configure(state="disabled")
        self.final_but.grid(row=4, column=0, padx=20, pady=10, sticky="sw")
        # OBS
        self.final_obs = customtkinter.CTkLabel(master=self.tab(self.titles[3]), text=f"OBS: Após executar o sorteio você não poderá mais criar apostas no mesmo")
        self.final_obs.grid(row=5, column=0, padx=20, pady=10, sticky="sw")

        # Fim da apuração tab
        
        # Premiação

        # Se não tiver nenhum sorteio criado
        if self.draw_prize_number_data == 0:
            self.draw_prize_number.configure(text="Nenhum sorteio criado!")
            self.final_but.configure(state="disabled")
            self.final_text.configure(text="Nenhum sorteio criado!")


    def table_window(self):
        self.window = customtkinter.CTkToplevel()
        self.window.resizable(width=False, height=False)
        self.table_data = [
                ["Número do Sorteio", "Rodadas", "Numeros Sorteados", "Finalizado", "Vencedores"]
        ]
        for i in Draw_Prize.select():
            winners = []
            for j in Draw_Prize_Winners_Relationship.select():
                if i.id == j.draw_prize.id:
                    winners.append(f"[{j.user.name}]")
            winners.sort()
            finished = ""
            if i.finished:
                finished = "Sim"
            else:
                finished = "Não"
            if i.has_winner == False:
                winners = "-"
            data = [i.id, i.rounds, i.numbers, finished, winners]
            self.table_data.append(data)

        self.table_frame = customtkinter.CTkScrollableFrame(master=self.window, width=700)
        self.table_frame.grid(row=0, column=0, padx=20, pady=20)
        self.table = CTkTable(master=self.table_frame, values=self.table_data)
        self.table.pack()  

    def new_draw_prize(self):
        Draw_Prize.create()
        self.draw_prize_number.configure(text=f"Sorteio nº: {Draw_Prize.select().count()}")
        CTkMessagebox(title="Sucesso", icon="check", message="Sorteio criado com sucesso!\n\nOBS: Você só poderá criar outro sorteio após a finalização do sorteio atual.")
        self.new_d.configure(state="disabled")
        self.actual_draw_prize = Draw_Prize.get_by_id(Draw_Prize.select().count())
        self.refresh_texts()


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
        

    def refresh_bet_table(self):
        self.new_table_data = [
                ["Numero do Sorteio", "Nome", "Cpf", "Números"]
        ]
        for i in Bet.select():
            numbers = [i.first, i.second, i.third, i.fourth, i.fifth]
            data = [i.register_number, i.user.name, i.user.cpf, numbers]
            self.new_table_data.append(data)
        self.table.destroy()
        self.table = CTkTable(master=self.table_frame, values=self.new_table_data)
        self.table.pack()  



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
                self.choices.set("")
                CTkMessagebox(title="Sucesso", icon="check", message="O apostador foi removido com sucesso!")
                self.refresh_bet_table()


    
    def add_bet(self):
        if self.n1.get() == "" or self.n2.get() == "" or self.n3.get() == "" or self.n4.get() == "" or self.n5.get() == "":
            CTkMessagebox(title="Erro", message="Digite todos os valores!!!", icon="cancel")
        elif not self.n1.get().isnumeric() or not self.n2.get().isnumeric() or not self.n3.get().isnumeric() or not self.n4.get().isnumeric() or not self.n5.get().isnumeric():
            CTkMessagebox(title="Erro", message="Digite apenas números!!!", icon="cancel")
        elif not 1 <= int(self.n1.get()) <= 50 or not 1 <= int(self.n2.get()) <= 50 or not 1 <= int(self.n3.get()) <= 50 or not 1 <= int(self.n4.get()) <= 50 or not 1 <= int(self.n5.get()) <= 50:
            CTkMessagebox(title="Erro", message="Todos os números devem estar sobre 1 e 50!!!", icon="cancel")
        elif self.choices.get() == "":
            CTkMessagebox(title="Erro", message="Você deve selecionar um apostar!!!", icon="cancel")
        else:
            self.user_info = self.choices.get()
            self.user_cpf = self.user_info[len(self.user_info) - 11 : len(self.user_info)]
            Bet.create(user=User.get(User.cpf == self.user_cpf), draw_prize=Draw_Prize.get_by_id(Draw_Prize.select().count()), register_number=1000+Bet.select().count()+1, first=int(self.n1.get()), second=int(self.n2.get()), third=int(self.n3.get()), fourth=int(self.n4.get()), fifth=int(self.n5.get()))
            CTkMessagebox(title="Sucesso", icon="check", message="A aposta foi criada com sucesso!")
            self.refresh_bet_table()

    def surprise_bet(self):
        if self.choices.get() == "":
            CTkMessagebox(title="Erro", message="Você deve selecionar um apostar!!!", icon="cancel")
        else:
            self.n1_random=random.randint(1, 50)
            self.n2_random=random.randint(1, 50)
            self.n3_random=random.randint(1, 50)
            self.n4_random=random.randint(1, 50)
            self.n5_random=random.randint(1, 50)
            self.user_info = self.choices.get()
            self.user_cpf = self.user_info[len(self.user_info) - 11 : len(self.user_info)]
            Bet.create(user=User.get(User.cpf == self.user_cpf), draw_prize=Draw_Prize.get_by_id(Draw_Prize.select().count()), register_number=1000+Bet.select().count()+1, first=self.n1_random, second=self.n2_random, third=self.n3_random, fourth=self.n4_random, fifth=self.n5_random)
            CTkMessagebox(title="Sucesso", icon="check", message="A aposta surpresa foi criada com sucesso!")
            self.refresh_bet_table()

    def start_draw_prize(self):
        self.exist_bet = False
        for i in Bet.select():
            if Draw_Prize.select().count() > 0:
                if i.draw_prize.id == self.actual_draw_prize.id:
                    self.exist_bet = True
                    break
        if self.exist_bet:
            self.configure(state="disabled")
            self.final_but.configure(state="disabled")
            self.actual_draw_prize.numbers = f"{random.randint(1, 50)}"
            for i in range(1, 5):
                self.actual_draw_prize.numbers += f", {random.randint(1, 50)}"
            self.actual_draw_prize.rounds += 1
            self.actual_draw_prize.save()
            self.draw_prize_numbers.configure(text=f"Números Sorteados: {self.actual_draw_prize.numbers}")
            self.round.configure(text=f"Rodada: {self.actual_draw_prize.rounds}")
            self.update()
            time.sleep(1)
            for i in range(5, 29):
                time.sleep(0.5)
                self.actual_draw_prize.numbers += f", {random.randint(1, 50)}"
                self.actual_draw_prize.rounds += 1
                self.actual_draw_prize.save()
                self.draw_prize_numbers.configure(text=f"Números Sorteados: {self.actual_draw_prize.numbers}")
                self.round.configure(text=f"Rodada: {self.actual_draw_prize.rounds}")
                self.update()
            time.sleep(1)
            self.configure(state="normal")
        else:
            CTkMessagebox(title="Erro", message="Você deve criar ao menos uma aposta!!!", icon="cancel")
    
    def refresh_texts(self):
        self.final_text.configure(text=f"Deseja finalizar as apostas e iniciar o Sorteio nº: {self.actual_draw_prize.id}?")
        self.final_but.configure(state="normal")
                
        
    
    
