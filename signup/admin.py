from django.contrib import admin
from .models import signup_table
from .models import faculty_signup
from .models import notes
from .models import asg
# Register your models here.

admin.site.register(signup_table)
admin.site.register(faculty_signup)
admin.site.register(notes)
admin.site.register(asg)