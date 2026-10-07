# What I checked, and what the agent got wrong

Write this yourself, in your own words. It is the part of the repo that proves the work is yours.

## What the agent got wrong
The agent proposed to use float division but i corrected it to just remove one dash so that the logic works 
Also agent asked to delete a function but when i said it to cross check it turned out it was being called in a file

## What I checked before I accepted its work
Wear bug: wear_percent(14900, 15000)
old code: 14900 // 15000 = 0 → 0% → not flagged. 
New code: 14900 / 15000 * 100 = 99.33% → above 80% → flagged. ✓

80% rule untouched: km_wachter.py line 6 still reads WARN_AT_PERCENT = 80. settings.cfg line 9 still reads warn_at_percent = 80. Neither was touched that how i checked before accepting its work

## What the data actually said
the risk score only uses km_since_service, load_factor, and avg_daily_km — the three that actually separated the groups. Age and odometer were deliberately left out because the data did not support them.
