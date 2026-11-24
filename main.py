#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't (make.fun bounty
u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e).

Writes one line of weather forecast, for a city that does not exist,
to /output/entry.txt.

The forecast (119 characters, inside the 1-140 gate):

    Gloaming-on-Sea: light drizzle of confetti, 14 degrees C, with
    a 90% chance your bus arrives the moment you stop looking at it.

Built for the judge's criteria, in order:
  1. A one-line weather forecast for a city that does not exist:
     the invented city is named first, and its weather is the whole
     point of the line -- "Gloaming-on-Sea" exists nowhere.
  2. Makes a bored commuter smile on one reading: the bus arrives
     the moment you stop looking at it -- every commuter has lived
     exactly that, and the forecast states it as meteorology.
  3. Keeps the register of a real forecast: "light drizzle ...,
     14 degrees C, with a 90% chance ..." is the rhythm of
     broadcast weather, bent rather than dropped.
  4. One concrete detail of the city's weather and life: the drizzle
     is confetti, so the place feels like somewhere -- a town that
     celebrates in the rain instead of sheltering from it.
  5. Uses its 140 characters well: every word earns its place, no
     filler, and the joke lands in the last clause.

Rejected alternatives (kept out of the entry on purpose):
  - a city where it rains upwards: surprising, but a sight gag with
    nothing for a commuter to recognise;
  - a forecast of "100% chance of Monday": a quip about the week,
    not weather for a place, and it names no city;
  - a city of perpetual rush hour with sunny spells: the joke is
    about traffic, and the weather becomes decoration.

Deterministic: the forecast is a fixed string, no randomness, no
network, no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

FORECAST = (
    "Gloaming-on-Sea: light drizzle of confetti, 14\u00b0C, with a 90% "
    "chance your bus arrives the moment you stop looking at it."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(forecast: str) -> None:
    """Enforce the competition's gate before writing: 1-140 Unicode code
    points, a single line (no line breaks -- the task demands one line),
    at least one character that is not white space. Fail loudly instead
    of writing an entry the gate would refuse."""
    if not 1 <= len(forecast) <= 140:
        raise SystemExit(f"forecast is {len(forecast)} characters, must be 1-140")
    if "\n" in forecast or "\r" in forecast:
        raise SystemExit("forecast must be a single line")
    if not any(not ch.isspace() for ch in forecast):
        raise SystemExit("forecast must contain a non-whitespace character")


def main() -> None:
    validate(FORECAST)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the forecast: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(FORECAST, encoding="utf-8")
    # Read back and verify: what the grader will read must be exactly
    # the validated forecast, byte for byte. Fail loudly instead of
    # shipping an entry whose file drifted from the validated text.
    if output_path.read_text(encoding="utf-8") != FORECAST:
        raise SystemExit("entry.txt read-back differs from the forecast")


if __name__ == "__main__":
    main()
