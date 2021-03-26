from pytest import mark


from django.test import TestCase
from django.urls import reverse_lazy

from .models import BasketballPlayer, SoccerPlayer
from .serializers import BasketballPlayerSerializer, SoccerPlayerSerializer


def create_test_basketball_player():
    basketball_player, created = BasketballPlayer.objects.get_or_create(
        name="Lebron James",
        slug="lebron-james",
        age=36,
        points_scored=13000,
        assists=9700,
        rebounds=9800,
    )
    return basketball_player


def create_test_soccer_player():
    soccer_player, created = SoccerPlayer.objects.get_or_create(
        name="Lionel Messi",
        slug="lionel-messi",
        age=33,
        goals_scored=734,
        assists=291,
        yellow_cards=81,
    )
    return soccer_player


class AthleteTest(TestCase):
    __test__ = False
    view_name = ""
    serializer_class = None

    def setUp(self) -> None:
        self.test_athlete = None

    @mark.django_db
    def test__response_ok(self):
        url = reverse_lazy(self.view_name, kwargs={"slug": self.test_athlete.slug})
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == self.serializer_class(self.test_athlete).data


class TestBasketballPlayerAPI(AthleteTest):
    __test__ = True
    view_name = "basketball_player"
    serializer_class = BasketballPlayerSerializer

    def setUp(self) -> None:
        self.test_athlete = create_test_basketball_player()


class TestSoccerPlayerAPI(AthleteTest):
    __test__ = True
    view_name = "soccer_player"
    serializer_class = SoccerPlayerSerializer

    def setUp(self) -> None:
        self.test_athlete = create_test_soccer_player()
