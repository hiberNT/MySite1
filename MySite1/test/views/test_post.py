import pytest #configurando o teste do view to passando pra que ele deve esperar o code 200 que é o code que se espera quando o get url da certo e espera ter um Hello World 

from django.urls import reverse



@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'Hello World'