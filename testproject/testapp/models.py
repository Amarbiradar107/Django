from django.db import models

# Create your models here.


from mongoengine import Document, StringField, IntField

class Person(Document):
    name = StringField(required=True, max_length=50)
    age = IntField(required=True)
