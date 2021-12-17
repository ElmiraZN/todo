from django.contrib import admin
from .models import ToDo, ToMeet, goal_for_month


admin.site.register(ToDo)
admin.site.register(ToMeet)
admin.site.register(goal_for_month)
