from django.db import models
import uuid


class Vegetable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    symptoms = models.ManyToManyField('Symptom')
    precautions = models.ManyToManyField('Precaution')

    def __str__(self):
        return self.name


class Fruit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    symptoms = models.ManyToManyField('Symptom')
    precautions = models.ManyToManyField('Precaution')

    def __str__(self):
        return self.name


class Symptom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Precaution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
