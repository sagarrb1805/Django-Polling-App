from django.db import models
from django.db.models.fields import CharField, IntegerField

class questions(models.Model):
    qid = IntegerField()
    question = CharField(max_length=255)
    option1 = CharField(max_length=255)
    option2 = CharField(max_length=255)
    option3 = CharField(max_length=255)
    option4 = CharField(max_length=255)
    vote1 = IntegerField()
    vote2 = IntegerField()
    vote3 = IntegerField()
    vote4 = IntegerField()
    
