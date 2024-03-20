from peewee import *

db = SqliteDatabase("theluckygame.db", pragmas={"foreign_keys": 1})   

class User(Model):
    name = CharField(null=False)
    cpf = CharField(unique=True, null=False)
    wins = IntegerField(default=0)

    class Meta:
        database = db

class Draw_Prize(Model):
    rounds = IntegerField(default=0)
    numbers = CharField(default= "-", null=True)
    finished = BooleanField(default=False)
    has_winner = BooleanField(default=False)
    class Meta:
        database = db

class Bet(Model):
    user = ForeignKeyField(User, backref="users", on_delete="CASCADE")
    draw_prize = ForeignKeyField(Draw_Prize, backref="draw_prize", on_delete="CASCADE")
    register_number = IntegerField(null=False)
    first = IntegerField(null=False)
    second = IntegerField(null=False)
    third = IntegerField(null=False)
    fourth = IntegerField(null=False)
    fifth = IntegerField(null=False)

    class Meta:
        database = db

class Draw_Prize_Winners_Relationship(Model):
    draw_prize = ForeignKeyField(Draw_Prize, backref="draw_prize", on_delete="CASCADE")
    user = ForeignKeyField(User, backref="users", on_delete="CASCADE")
    register_number = IntegerField(null=False)
    class Meta:
        database = db
    



