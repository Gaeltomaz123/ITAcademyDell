from peewee import *

db = SqliteDatabase("theluckygame.db")   

class User(Model):
    name = CharField()
    cpf = CharField(unique=True)
    wins = IntegerField()

    class Meta:
        database = db

class Draw_Prize(Model):
    rounds = IntegerField(default=0)
    first = IntegerField(null=True)
    second = IntegerField(null=True)
    third = IntegerField(null=True)
    fourth = IntegerField(null=True)
    fifth = IntegerField(null=True)
    finished = BooleanField(default=False)
    class Meta:
        database = db

class Rounds(Model):
    round_number = IntegerField()
    draw_prize = ForeignKeyField(Draw_Prize, backref="draw_prize")
    has_winner = BooleanField(default=False)

    class Meta:
        database = db

class Bet(Model):
    user = ForeignKeyField(User, backref="users")
    draw_prize = ForeignKeyField(Draw_Prize, backref="draw_prize")
    round_number = ForeignKeyField(Rounds.round_number, backref="round")
    first = IntegerField()
    second = IntegerField()
    third = IntegerField()
    fourth = IntegerField()
    fifth = IntegerField()

    class Meta:
        database = db

class Draw_Prize_Winners_Relationship(Model):
    draw_prize = ForeignKeyField(Draw_Prize, backref="draw_prize")
    user = ForeignKeyField(User, backref="users")

    class Meta:
        database = db
    



