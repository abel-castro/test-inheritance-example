from django.test import TestCase
from django.urls import reverse_lazy

from .models import BasketballPlayer, SoccerPlayer
from .serializers import BasketballPlayerSerializer, SoccerPlayerSerializer


def create_test_basketball_player():
    return BasketballPlayer.objects.create(
        name="Lebron James",
        slug="lebron-james",
        age=36,
        points_scored=13000,
        assists=9700,
        rebounds=9800,
    )


def create_test_soccer_player():
    return SoccerPlayer.objects.create(
        name="Lionel Messi",
        slug="lionel-messi",
        age=33,
        goals_scored=734,
        assists=291,
        yellow_cards=81,
    )


class TestBasketballPlayerAPI(TestCase):
    def setUp(self) -> None:
        self.basketball_player = create_test_basketball_player()

    def test__response_ok(self):
        url = reverse_lazy(
            "basketball_player", kwargs={"slug": self.basketball_player.slug}
        )
        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data == BasketballPlayerSerializer(self.basketball_player).data


class TestSoccerPlayerAPI(TestCase):
    def setUp(self) -> None:
        self.soccer_player = create_test_soccer_player()

    def test__response_ok(self):
        url = reverse_lazy("soccer_player", kwargs={"slug": self.soccer_player.slug})
        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data == SoccerPlayerSerializer(self.soccer_player).data
