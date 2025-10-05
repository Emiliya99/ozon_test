import pytest
from .superhero import SuperHero

@pytest.mark.superhero_get
class TestSuperHero:
    def test_get_max_height_superhero_male_work(self, api_url):
        superhero_male = SuperHero(api_url)
        superhero_male.get_max_height_superhero('Male', True)

    def test_get_max_height_superhero_female_work(self, api_url):
        superhero_male = SuperHero(api_url)
        superhero_male.get_max_height_superhero('Female', True)

    # @pytest.mark.xfail
    def test_get_max_height_superhero_none_work(self, api_url):
        superhero_male = SuperHero(api_url)
        superhero_male.get_max_height_superhero('-', True)

    def test_get_max_height_superhero_male_no_work(self, api_url):
        superhero_male = SuperHero(api_url)
        superhero_male.get_max_height_superhero('Male', False)

    def test_get_max_height_superhero_female_no_work(self, api_url):
        superhero_male = SuperHero(api_url)
        superhero_male.get_max_height_superhero('Female', False)

    def test_get_max_height_superhero_none_no_work(self, api_url):
        superhero_male = SuperHero(api_url)
        superhero_male.get_max_height_superhero('-', False)