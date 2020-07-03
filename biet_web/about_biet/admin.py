from django.contrib import admin
from .models import Academic_Calender, Office_Staff, Deans, Governing_Body

# Register your models here.
admin.site.register(Academic_Calender)
admin.site.register(Office_Staff)
admin.site.register(Deans)
admin.site.register(Governing_Body)
