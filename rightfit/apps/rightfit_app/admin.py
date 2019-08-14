from django.contrib import admin

# Register your models here.
from .models import Quote, School, User, Student, Activity, Major

admin.site.register(Quote)
admin.site.register(School)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Activity)
admin.site.register(Major)
