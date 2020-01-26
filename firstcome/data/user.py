import datetime
import mongoengine


class User(mongoengine.Document):

    name = mongoengine.StringField()
    email = mongoengine.StringField(unique=True)
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'users',
        'indexes': [
            'email',
            'created_date',
            'name',
        ]
    }
