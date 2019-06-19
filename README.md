Unicorn Hue
===

This just turns your unicorn hat into a hue light that cycles in about an hour.

It works by incrementing a hue value, and converting that along with a set value for lightness and saturation into Red Blue Green which is then used to display a colour.

Put a smoked glass bowl over your unicorn hat, et voilà, a hue lamp.

Requirements
---
- sudo pip install unicornhat colorsys

Run
---
- sudo /path/to/hue.py

Play with time.sleep(6) and h = h + 0.001 if you want it to cycle faster.



