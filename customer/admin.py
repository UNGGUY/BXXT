from django.contrib import admin

# Register your models here.
from customer import models

admin.site.register(models.User)
admin.site.register(models.Apply)
admin.site.register(models.Audit)
admin.site.register(models.Detail)
admin.site.register(models.Hospital)
admin.site.register(models.Manager)
admin.site.register(models.Ratio)
admin.site.register(models.Record)
admin.site.register(models.Section)
admin.site.register(models.UserType)




