from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(ContactMessage)
admin.site.register(TeamMember)
admin.site.register(Avatar)

# Super user: superuser1 pass: hola123
# Usuario de prueba: user2 pass: Vegeta_1999