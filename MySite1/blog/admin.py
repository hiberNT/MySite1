from django.contrib import admin

# Register your models here.
from .models import Post #conectando o post para ta o controle dele pro django


class PostAdmin(admin.ModelAdmin): #passando pra aparecer uma lista desses itens la no site do admin
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
  
    
admin.site.register(Post, PostAdmin)#fazendo o registro do post pra aparecer la no admin quando entrar no site
