from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Story)
admin.site.register(Profile)
admin.site.register(Comment)

