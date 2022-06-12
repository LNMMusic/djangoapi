from django.db import models
import uuid

# const
EMPTY = {'null': True, 'blank': True}


# Model [DB Driver]
class User(models.Model):
    # fields
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    username = models.CharField(max_length=50, **EMPTY)
    password = models.CharField(max_length=100, **EMPTY)
    fullname = models.CharField(max_length=50,)
    email    = models.EmailField()
    
    # methods
    def __str__(self):
        return str(self.username)



# Schemas [serializer] [endpoints]
# ...