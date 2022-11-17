from django.contrib import admin
from .models import Hamster, Feeding, Toy

admin.site.register(Hamster)
admin.site.register(Feeding)
admin.site.register(Toy)
