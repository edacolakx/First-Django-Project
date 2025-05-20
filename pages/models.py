from django.db import models

class Course(models.Model):
    title=models.CharField(max_length=50)#null=True yazılırsa null kalabilir defaultfalse
    description=models.TextField()
    imageUrl=models.CharField(max_length=50)#blank=True denirse boş bırakabilirsin demek false sa boş bırakmaz validation hatası verir default false
    date=models.DateField()
    isActive=models.BooleanField()

