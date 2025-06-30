from django.contrib import admin
from .models import PortfolioCategory, PortfolioImage

# Register your models here.


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]


admin.site.register(PortfolioImage)
