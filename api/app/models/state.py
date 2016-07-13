import peewee

@app.route()
class State(BaseModel):
    name = CharField(128, null = False, unique = True)
