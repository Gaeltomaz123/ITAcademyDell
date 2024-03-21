from database import db, User, Bet, Draw_Prize, Draw_Prize_Winners_Relationship
from app import App


db.connect()


db.create_tables([User, Bet, Draw_Prize, Draw_Prize_Winners_Relationship])

app = App()
app.mainloop()


