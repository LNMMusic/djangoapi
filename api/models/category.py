from django.db import models
from rest_framework import serializers
import uuid
# const
EMPTY = {'null': True, 'blank': True}



# Model [DB Driver]
class Category(models.Model):
    # options
    options_color = [
        ('Black', 'Black'),
        ('Grey', 'Grey'),
        ('White', 'White')
    ]

    # fields
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50, **EMPTY)
    color = models.CharField(choices=options_color, max_length=5, default=options_color[0])

    def __str__(self):
        return str(self.name + ' ' + self.color)


# Schemas
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ['name', 'color']