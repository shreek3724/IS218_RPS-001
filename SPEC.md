# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

Implement one independent round with `determine_winner(player, computer)`. Rock versus
Paper returns `lose` because Paper beats Rock; all nine outcomes in the table remain the
source of truth. Add literal unit tests for all nine outcomes, one fixed-computer
request/result test, and one real-browser round plus replay. Reuse the supplied checks
that reject missing or unsupported moves with HTTP 400 and a helpful explanation. Do not
add scoring or saved history.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: https://github.com/shreek3724/IS218_RPS-001/issues/1
- Pull request / CI: add actual URLs when they exist.
- Implementation: [game.py](game.py) now resolves one independent round; see
  [unit and integration tests](tests/test_game.py) and
  [browser round/replay test](tests/e2e/test_round.py).
- Checks: `.venv/bin/python check.py` passed Black, Pylint, 23 non-browser
  tests, and 6 Chromium tests. Browser observation: player Rock, computer Rock,
  displayed tie.
