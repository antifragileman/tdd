from django.urls import reverse
import json



def test_hw():
    assert "kdfskgbj"=="kdfskgbj"
    assert "ff"!="dfkjng"


def test_ping(client):
    url=reverse("ping")
    response=client.get(url)
    content=json.loads(response.content)
    assert response.status_code==200
    assert content["ping"]=="pong!"