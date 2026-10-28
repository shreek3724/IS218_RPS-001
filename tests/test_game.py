"""Rule and request checks for RPS-001."""

# pytest injects fixtures by name.
# pylint: disable=redefined-outer-name,missing-function-docstring

import pytest

import app as web
from game import determine_winner

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_determine_winner_returns_expected_outcome(player, computer, expected):
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
def test_submitted_round_uses_real_rules_and_displays_result(monkeypatch):
    web.app.config.update(TESTING=True)
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    response = web.app.test_client().post("/", data={"move": "rock"})
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "You chose" in page and "Rock" in page
    assert "Computer chose" in page and "Paper" in page
    assert "Computer wins" in page
    assert 'data-outcome="lose"' in page
