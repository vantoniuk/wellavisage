from django.contrib import admin

from .models import Picture,Album

class PictureAdmin(admin.ModelAdmin):
	list_display = ('id','file_name', 'author', 'date')
	list_filter = ['author', 'date']
	
admin.site.register(Picture, PictureAdmin)

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('name', 'author', 'date')
	list_filter = ['author', 'date']

admin.site.register(Album, AlbumAdmin)	
