from django.contrib import admin

# Register your models here.

from django.contrib import admin
# Register your models here.

class CreditStatusAdmin(admin.ModelAdmin):
    list_display = "status,holder,issuer,card,issuedate,closedate,line,fee,minspend,bonus".split(",")
    search_fields = list_display
from .models import CreditStatus
admin.site.register(CreditStatus,CreditStatusAdmin)

class PointsUsedAdmin(admin.ModelAdmin):
    list_display = "date,where,what,dollar_cost,point_cost,info".split(",")
    search_fields = list_display
from .models import PointsUsed
admin.site.register(PointsUsed,PointsUsedAdmin)


