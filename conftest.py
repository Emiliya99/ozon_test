import pytest

@pytest.fixture
def base_url():
    return "https://superheroapi.com/"

@pytest.fixture
def api_url(base_url):
    return f"{base_url}api/d150ffe8a4d060e0a1bed5328da59b3d/"

