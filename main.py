from database import db, User, Bet, Draw_Prize, Draw_Prize_Winners_Relationship
from app import App


db.connect()

db.create_tables([User, Bet, Draw_Prize, Draw_Prize_Winners_Relationship])

#Draw_Prize.create(rounds=0, first = 10, second = 34, third = 42, fourth = 29, fifth= 50)

#draw_prize = Draw_Prize.get(Draw_Prize.id == 1)
#user = User.get(User.id==1)

#User.create(name="jose", cpf="24434234", wins="0")
#user1 = User.get(User.id==2)
#Draw_Prize_Winners_Relationship.create(draw_prize_id=draw_prize, user_id=user1)

'''a = Draw_Prize.get_by_id(1)
a.numbers = "-"
a.rounds = 0
a.has_winner = False
a.save()'''

'''Draw_Prize.delete_by_id(2)'''

app = App()
app.mainloop()


#user2 = User.create(name="Jose", cpf="321312312", wins=0)
#draw_price1 = Draw_Price.create(rounds=0, first = 10, second = 34, third = 42, fourth = 29, fifth= 50)
#draw_price1= Draw_Price.get(Draw_Price.id==1)
#round1 = Rounds.create(round_number=0, draw_price=draw_price1, has_winner=True)
#round2 = Rounds.create(round_number=24, draw_price=draw_price1, has_winner=True)
#user1 = User.get(User.id==1)
#user2 = User.get(User.id==2)
#round2 = Rounds.get(Rounds.id==2)
#bet2 = Bet.create(user=user2, draw_price=draw_price1, round_number=round2.round_number, first = 5, second = 2, third = 12, fourth = 30, fifth= 50)
#print(round2)
#winner = Draw_Price_Winners_Relationship.create(draw_price=draw_price1, user=user2)



'''class User():
    def __init__(self, name, cpf, round, bets):
        self.name = name
        self.cpf = cpf
        self.round = round
        self.bets = bets
        self.winner = False
    def increase_round() {

    }
    def __str__(self):
        return f"Name: {self.name}, Cpf: {self.cpf}, Bet: {self.bet}, Winner: {self.winner}"

n = str(input("Name: "))
cpf = str(input("CPF: "))
first = int(input("1st number: "))
second = int(input("2nd number: "))
third = int(input("3rd number: "))
fourth = int(input("4th number: "))
fifth = int(input("5th number: "))
bets = [round=[first, second, third, fourth, fifth]]
user1 = User(n, cpf, bets)
print(user1.bet[0])

print(user1)

class Sorteio():
    def __init__(self, users):
        self.users = users'''


