from django.contrib import admin
from .models import Food, Movie, Subscription, TVShow, MovieStream, TVStream, Feedback


admin.site.register(Food)
admin.site.register(Movie)
admin.site.register(Subscription)
admin.site.register(TVShow)
admin.site.register(MovieStream)
admin.site.register(TVStream)
admin.site.register(Feedback)