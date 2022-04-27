from django.contrib import admin
from .models import UserProfile

admin.site.site_header = "Witaj w Portalu Health"
admin.site.site_title = "Health Admin Portal"
admin.site.index_title = "Witaj w Portalu Health"


@admin.register(UserProfile)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "bio"]
    search_fields = ["id", "user", "bio"]
