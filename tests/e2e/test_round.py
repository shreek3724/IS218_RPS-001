"""Real-browser RPS-001 round and replay checks."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_player_can_play_a_round_and_replay(page: Page, live_server, monkeypatch):
    """A browser click uses real rules for consecutive independent rounds."""
    computer_moves = iter(("paper", "rock"))
    monkeypatch.setattr(web.random, "choice", lambda _moves: next(computer_moves))

    page.goto(live_server)
    page.get_by_role("button", name="Rock", exact=True).click()

    expect(page.get_by_label("This round’s choices")).to_contain_text("Rock")
    expect(page.get_by_label("This round’s choices")).to_contain_text("Paper")
    expect(page.locator("[data-outcome='lose']")).to_contain_text("Computer wins")

    page.get_by_role("button", name="Paper", exact=True).click()

    expect(page.get_by_label("This round’s choices")).to_contain_text("Paper")
    expect(page.get_by_label("This round’s choices")).to_contain_text("Rock")
    expect(page.locator("[data-outcome='win']")).to_contain_text("You win!")
