from django.contrib import admin
from .models import UserData, Claim, ProcessedClaim
# Register your models here.

admin.site.register(UserData)
admin.site.register(Claim)
admin.site.register(ProcessedClaim)
