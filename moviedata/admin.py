from django.contrib import admin
from .models import category, male_actor, female_actor, movie, multiplex, shows


class showcategory(admin.ModelAdmin):
    list_display = ["name", "desc"]


admin.site.register(category, showcategory)


class showactor(admin.ModelAdmin):
    list_display = ["name", "dob", "desc"]


admin.site.register(male_actor, showactor)


class showactress(admin.ModelAdmin):
    list_display = ["name", "dob", "desc"]


admin.site.register(female_actor, showactress)


class showmovie(admin.ModelAdmin):
    list_display = ["name", "desc", "actor", "actress", "movie_category"]


admin.site.register(movie, showmovie)


class showmultiplex(admin.ModelAdmin):
    list_display = ["name", "address", "no_of_screens", "city", "state", "website"]


admin.site.register(multiplex, showmultiplex)


class showshows(admin.ModelAdmin):
    list_display = [
        "movie_name",
        "multiplex",
        "showtime",
        "seats",
        "ticket_price",
        "type",
        "language",
    ]


admin.site.register(shows, showshows)
