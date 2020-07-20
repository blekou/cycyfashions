from django.contrib import admin
from django.utils.safestring import mark_safe
from .import models


admin.site.register(models.SiteInfo),
admin.site.register(models.Reseaux_sociaux),
admin.site.register(models.Presentation),
admin.site.register(models.Slider),
admin.site.register(models.Categories),




class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('nom','titre', 'address',' image_view',)
    list_filter = ('nom', )
    ordering = ('date_add',)
    search_fields = ('nom',)
    list_per_page = 10
    fieldsets = [
        ('site info', {'fields':['nom', 'image', 'email']}),
        ('standars', {'filelds': ['status']})
    ]

    def image_view(self, obj):
        return mark_safe("<img src='{url}' width=100, height=50".format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model,admin_class)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('nom',' image_view',)
    list_filter = ('nom', )
    ordering = ('date_add',)
    search_fields = ('nom',)
    list_per_page = 10
    fieldsets = [
        ('site info', {'fields':['nom',]}),
        ('standars', {'filelds': ['status']})
    ]

    def image_view(self, obj):
        return mark_safe("<img src='{url}' width=100, height=50".format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model,admin_class)




class PresentationAdmin(admin.ModelAdmin):

    list_display = ('description', 'titre',' image_view',)
    list_filter = ('titre', )
    ordering = ('date_add',)
    search_fields = ('titre',)
    list_per_page = 10
    fieldsets = [
        ('presntation', {'fields':['titre', 'image', 'icone']}),
        ('standars', {'filelds': ['status']})
    ]

    def image_view(self, obj):
        return mark_safe("<img src='{url}' width=100, height=50".format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model,admin_class)


class SliderAdmin(admin.ModelAdmin):
    
    list_display = ('description', 'titre',' image_view',)
    list_filter = ('titre', )
    ordering = ('date_add',)
    search_fields = ('titre',)
    list_per_page = 10
    fieldsets = [
        ('presntation', {'fields':['titre', 'image', 'icone']}),
        ('standars', {'filelds': ['status']})
    ]

    def image_view(self, obj):
        return mark_safe("<img src='{url}' width=100, height=50".format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model,admin_class)




class Reseaux_sociauxAdmin(admin.ModelAdmin):

    list_display = ('nom', 'address',' image_view',)
    list_filter = ('nom', )
    ordering = ('date_add',)
    search_fields = ('nom',)
    list_per_page = 10
    fieldsets = [
        ('reseux sociaux', {'fields':['nom', 'image', 'icone']}),
        ('standars', {'filelds': ['status']})
    ]

    def image_view(self, obj):
        return mark_safe("<img src='{url}' width=100, height=50".format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model,admin_class)




