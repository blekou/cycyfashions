from django.contrib import admin
from .import models

admin.site.register(models.Categorie),
admin.site.register(models.Tag),
admin.site.register(models.Article),
admin.site.register(models.Commentaire),

class ArticleInline(admin.TabularInline):
    model = models.Article
    extra = 0

class CategorieAdmin(admin.ModelAdmin):

    list_display = ('nom','status','date_add','date_update',)
    list_filter = ('status', 'date_add', 'date_update',)
    search_field = ('nom',)
    date_hierarchy = 'date_add',
    actions = ('active','desactivé',)
    list_display_links = ['nom'],
    list_per_page = 5
    ordering = ['nom'],

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'la selection a été activé avec succès ')
    
    active.short_description = "activé les catégories séléctionné"


class TagAdmin(admin.ModelAdmin):
    
    list_display = ('nom','status','slug','date_add','date_update',)
    list_filter = ('status', 'date_add', 'date_update',)
    search_field = ('nom',)
    date_hierarchy = 'date_add',
    actions = ('active','desactivé',)
    list_display_links = ['nom'],
    list_per_page = 5
    ordering = ['nom'],

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'la selection a été activé avec succès ')
    
    active.short_description = "activé les catégories séléctionné"


class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ('nom','status','date_add','date_update',)
    list_filter = ('status', 'date_add', 'date_update',)
    search_field = ('nom',)
    date_hierarchy = 'date_add',
    actions = ('active','desactivé',)
    list_display_links = ['nom'],
    list_per_page = 5
    ordering = ['nom'],

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'la selection a été activé avec succès ')
    
    active.short_description = "activé les catégories séléctionné"


class CommentaireAdmin(admin.ModelAdmin):
    
    list_display = ('username','status','date_add','date_update',)
    list_filter = ('status', 'date_add', 'date_update',)
    search_field = ('username',)
    date_hierarchy = 'date_add',
    actions = ('active','desactivé',)
    list_display_links = ['username'],
    list_per_page = 5
    ordering = ['username'],

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'la selection a été activé avec succès ')
    
    active.short_description = "activé les catégories séléctionné"





