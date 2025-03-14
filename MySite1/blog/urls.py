from django.urls import path #config do url com nome que difinimos pra pesquisar na internet home no caso

from blog import views

urlpatterns = [
    path("", views.PostView.as_view(), name='home'),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]