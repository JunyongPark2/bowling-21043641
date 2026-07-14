# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This repository is currently empty aside from a Python virtualenv (`.venv`, Python 3.14) and PyCharm project files (`.idea`). No source code, tests, or package layout exist yet. The project's purpose is to implement the **Bowling Game Kata** using TDD (Test-Driven Development).

## Commands

- Activate the virtualenv: `source .venv/bin/activate`
- Run tests: `pytest` (or `.venv/bin/pytest` if not activated)
- Run a single test: `pytest path/to/test_file.py::test_name`

No build/lint tooling is configured yet — set it up (or ask the user which tools they prefer) before assuming a specific linter/formatter.

## The Kata

Implement a `Game` class with:

- `roll(pins: int) -> None` — called once per ball thrown; `pins` is the number of pins knocked down.
- `score() -> int` — returns the total score for the completed game.

Do not implement input validation, roll/frame-count validation, or mid-game scoring — the kata intentionally omits these to keep focus on the core scoring logic.

### Scoring rules

- Game = 10 frames, each normally allowing 2 rolls to knock down 10 pins.
- **Spare** (10 pins across 2 rolls): frame bonus = pins on the *next 1 roll*.
- **Strike** (10 pins on the 1st roll): frame ends immediately; bonus = pins on the *next 2 rolls*.
- **10th frame**: if it's a spare or strike, the player gets fill ball(s) to complete the frame, up to a max of 3 rolls in that frame.

## Working style

This repo is for a TDD kata — when implementing, follow a red/green/refactor loop: write a failing test for one small piece of behavior, implement the minimum to pass it, then refactor, rather than writing the full `Game` class up front.
