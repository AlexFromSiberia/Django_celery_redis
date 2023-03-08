from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    list_display_links = ("name", "email")

    # пагинация - по 10 записей на страницу
    list_per_page = 10
    # сколько можно максимально показать при нажатии кнопки `show all`
    list_max_show_all = 100
