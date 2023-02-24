from django.contrib import admin
from web.models import (Ad, Banner, Blog, Cart, CartItem, Category, Feedback,
                        FilterPrice, Product, SpecialOffer, SubCategory, Team)

# Register your models here.

admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(SpecialOffer)
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(Feedback)
admin.site.register(Ad)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(FilterPrice)
