#models.py
from django.db import models

class Todo(models.Model):
	added_date = models.DateTimeField()
	text = models.Charfield(max_length =200)