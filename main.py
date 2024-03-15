from database import db, User, Numbers, Rounds, Draw_Price

db.connect()

db.create_tables([User, Numbers, Rounds, Draw_Price])




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


