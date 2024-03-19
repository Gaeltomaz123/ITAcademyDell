from peewee import *

db = SqliteDatabase("theluckygame.db")   

class User(Model):
    name = CharField(null=False)
    cpf = CharField(unique=True, null=False)
    wins = IntegerField(default=0)

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
    register_number = IntegerField(null=False)
    first = IntegerField(null=False)
    second = IntegerField(null=False)
    third = IntegerField(null=False)
    fourth = IntegerField(null=False)
    fifth = IntegerField(null=False)

    class Meta:
        database = db

class Draw_Prize_Winners_Relationship(Model):
    draw_prize = ForeignKeyField(Draw_Prize, backref="draw_prize")
    user = ForeignKeyField(User, backref="users")
    class Meta:
        database = db
    



