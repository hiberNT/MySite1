#from django.http import HttpResponse #config do view no http configura o resultado que queremos mostrar no resultado final pro cliente que é a função do view inclusive
from django.views import generic #biblioteca do django
from blog.models import Post



class PostView(generic.ListView): #passando a lista que vai listar o post     
    queryset = Post.objects.filter(status=1).order_by("-created_on")#quando o url bater na home executa esse queryset dai gera a rendererização do html uma vez q fizermos isso vai enviar os dados desse queryset pra dentro do index.html e ai o propio django faz a conversão pra fazer uma lista q ta la no html
    template_name = "index.html"
    
class PostDetail(generic.DetailView): #msm coisa la de cima so q agr no outro index
    model = Post
    template_name = "post_detail.html"    