from django.contrib import admin

# Register your models here.
class MyStocksModelAdmin(admin.ModelAdmin):
    list_display=["id","Buy_Date","Sell_Date","Symbol","Quanity","Buy_Price","Sell_Price"]
    search_fields = list_display
from .models import MyStocks
admin.site.register(MyStocks, MyStocksModelAdmin)

class PricesModelAdmin(admin.ModelAdmin):
    list_display=["id","Date","Symbol","Price"]
    search_fields = list_display
from .models import Prices
admin.site.register(Prices, PricesModelAdmin)
