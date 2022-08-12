import pytest
from culturemesh import app

@pytest.fixture
def client():
  """Configures the app for testing
  Sets app config variable ``TESTING`` to ``True``
  :return: App for testing
  """
  #app.config['TESTING'] = True
  client = app.test_client()
  yield client

def test_landing_aliases(client):
  landing = client.get("/")
  assert client.get("/index/").data == landing.data

def test_landing(client):
  landing = client.get("/")
  html = landing.data.decode()
  # Check that links to `about` and `login` pages exist
  assert "<a href=\"/about/\">About</a>" in html
  assert " <a href=\"/home/\">Login</a>" in html
  # Spot check important text
  assert "At CultureMesh, we're building networks to match these " \
    "real-world dynamics and knit the diverse fabrics of our world " \
      "together." in html
  assert "1. Join a network you belong to." in html
  assert landing.status_code == 200