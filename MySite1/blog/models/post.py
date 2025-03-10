from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):#aqui sao as config do site que vai ser um blog esses comandos usados CharField,TextField... sao todos fornecidos pela biblioteca do django que jas nos tras essa montagem
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) #identificação do nosso post no blog
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)#campo de atualização de dados tipo pra ve se foi atualizado alguma noticia e talz
    content = models.TextField() #parte da escrita q seria todo o texto
    created_on = models.DateTimeField(auto_now_add =True)#campo de hr e data
    status = models.IntegerField(choices=STATUS, default=0)#para podermos criar um rascunho ou publicar um post

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title