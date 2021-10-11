import mongoengine
from mongoengine import Document


class User(Document):
    name = mongoengine.StringField()
    email = mongoengine.StringField()
    expo_token = mongoengine.StringField(null=True)

    def convert_to_json(self):
        result = self.to_mongo().to_dict()
        if "_id" in result:
            del result["_id"]
        return result