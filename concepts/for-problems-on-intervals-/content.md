# For Problems On Intervals 

1️⃣ Overlap / Conflict Detection

“Do intervals clash?”
Recognition
Words like: overlap, intersect, conflict, non-overlapping
Often asks for min removals or yes/no

Key idea
Sort by end time, greedily keep the earliest finishing interval.
Why end time?
It leaves maximum room for future intervals.

Template
```
sort by end
keep last_end
if start < last_end → conflict
```

Problems
Non-overlapping Intervals
Minimum Number of Arrows to Burst Balloons
Remove Covered Intervals

## 🔗 Related Problems

- https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
