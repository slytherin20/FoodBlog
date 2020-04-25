from django.contrib import admin
from .models import Receipe,Category,Comment,Bookmark
from django.db import models

class commentAdmin(admin.ModelAdmin):
	list_display = ('name','text','title','created_on','active')
	list_filter = ('created_on','active')
	search_fields = ('name','email','text')
	actions = ['approve_comments']

	def approve_comments(self, request, queryset):
		queryset.update(active = True)


admin.site.register(Receipe)
admin.site.register(Category)
admin.site.register(Comment,commentAdmin)
admin.site.register(Bookmark)
