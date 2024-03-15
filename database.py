from peewee import *

db = SqliteDatabase("theluckygame.db")   

class User(Model):
    name = CharField()
    cpf = CharField(unique=True)
    wins = IntegerField()

    class Meta:
        database = db

class Draw_Price(Model):
    rounds = IntegerField()
    first = IntegerField()
    second = IntegerField()
    third = IntegerField()
    fourth = IntegerField()
    fifth = IntegerField()
    class Meta:
        database = db

class Rounds(Model):
    round_number = IntegerField()
    draw_price = ForeignKeyField(Draw_Price, backref="draw_price")
    has_winner = BooleanField(default=False)

    class Meta:
        database = db

class Bet(Model):
    user = ForeignKeyField(User, backref="users")
    draw_price = ForeignKeyField(Draw_Price, backref="draw_price")
    round_number = ForeignKeyField(Rounds.round_number, backref="round")
    first = IntegerField()
    second = IntegerField()
    third = IntegerField()
    fourth = IntegerField()
    fifth = IntegerField()

    class Meta:
        database = db

class Draw_Price_Winners_Relationship(Model):
    draw_price = ForeignKeyField(Draw_Price, backref="draw_price")
    user = ForeignKeyField(User, backref="users")

    class Meta:
        database = db
    



