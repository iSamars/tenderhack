from django.contrib import admin
from .models import Contract, Category, STU
from django.urls import reverse
from django.utils.html import format_html

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]

@admin.register(Contract)
class Contract(admin.ModelAdmin):
    list_display = ["id", "number", "cost", "customer_name", "provider_name"]
    search_fields = ["number"]

@admin.register(STU)
class STU(admin.ModelAdmin):
    list_display = ["id", "name", "get_category_link", "code"]
    search_fields = ["name", "category", "code"]

    def get_category_link(self, obj):
        url = (
            reverse("admin:main_category_changelist")
            + str(obj.category.id)
            + "/change"
        )
        return format_html(f'<a href="%s">%s</a>' % (url, obj.category.name))

    get_category_link.short_description = "Категория"