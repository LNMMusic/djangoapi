from django.db import models
from rest_framework import serializers
import uuid
# const
EMPTY = {'null': True, 'blank': True}



# Model [DB Driver]
class Item(models.Model):
    # fields
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50, **EMPTY)
    active = models.BooleanField(default=False)
    # relationship [onetomany - manytomany]
    user = models.ForeignKey("User", on_delete=models.CASCADE, **EMPTY)
    category = models.ManyToManyField("Category", blank=True)

    # methods
    def __str__(self):
        return str(self.name)


# Schemas
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'active', 'user']