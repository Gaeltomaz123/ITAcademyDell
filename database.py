from peewee import *

db = SqliteDatabase("theluckygame.db")   

class User(Model):
    name = CharField()
    cpf = CharField(unique=True)
    wins = IntegerField()

    class Meta:
        database = db

class Numbers(Model):
    user = ForeignKeyField(User, backref="users")
    first = IntegerField()
    second = IntegerField()
    third = IntegerField()
    fourth = IntegerField()
    fifth = IntegerField()

    class Meta:
        database = db

class Rounds(Model):
    round_number = IntegerField()
    numbers = ManyToManyField(Numbers, backref="numbers")

    class Meta:
        database = db

class Draw_Price(Model):
    rounds = ForeignKeyField(Rounds, backref="rounds")
    winners = ManyToManyField(User, backref="users")
    first = IntegerField()
    second = IntegerField()
    third = IntegerField()
    fourth = IntegerField()
    fifth = IntegerField()

    class Meta:
        database = db
    



