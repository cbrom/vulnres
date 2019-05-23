from django.contrib import admin
from .models import Patch, File, Vulnerability
# Register your models here.
admin.site.register(Patch)
admin.site.register(File)
admin.site.register(Vulnerability)