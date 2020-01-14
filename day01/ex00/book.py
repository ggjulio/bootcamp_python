import datetime as dt

class Book:
    def __init__(self, ):
        Recipe.creation_date = (dt.datetime.now() if Recipe.creation_date is None)
        Recipe.last_update = dt.datetime.now()
