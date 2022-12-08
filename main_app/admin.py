from django.contrib import admin
from .models import Hamster, Feeding, Toy, Photo

admin.site.register(Hamster)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)
