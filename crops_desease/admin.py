from django.contrib import admin
from crops_desease.models import Vegetable, Fruit, Precaution, Symptom

admin.site.register(Vegetable)
admin.site.register(Fruit)
admin.site.register(Precaution)
admin.site.register(Symptom)
