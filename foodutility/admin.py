from django.contrib import admin
from .models import CustomUser,Volunteer_Detail,Donor_Detail,Donate_Money,Donate_Food

admin.site.register(CustomUser)
admin.site.register(Volunteer_Detail)
admin.site.register(Donor_Detail)
admin.site.register(Donate_Money)
admin.site.register(Donate_Food)