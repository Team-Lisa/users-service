import mongoengine
from mongoengine import Document


class User(Document):
    name = mongoengine.StringField()
    email = mongoengine.StringField()
    expo_token = mongoengine.StringField(null=True)
    last_connection = mongoengine.DateTimeField()

    def convert_to_json(self):
        result = self.to_mongo().to_dict()
        result["last_connection"] = result["last_connection"].strftime('%Y-%m-%d')
        if "_id" in result:
            del result["_id"]
        return result