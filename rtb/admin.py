from django.contrib import admin
from rtb.models import UserProfile, Review, Business, Boba, Flavour, Ingredient, User

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Business)
admin.site.register(Boba)
admin.site.register(Flavour)
admin.site.register(Ingredient)