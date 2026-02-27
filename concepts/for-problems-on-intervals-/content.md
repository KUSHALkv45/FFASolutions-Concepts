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

2️⃣ Interval Merging

“Combine overlapping ranges”
Recognition
“Merge”, “union”, “combine”
Output intervals, not counts

Key idea
Sort by start, extend current interval while overlapping.

Template
```
sort by start
if cur.start ≤ prev.end → merge
else push new interval

```

Problems
Merge Intervals
Insert Interval
Interval List Intersections

## 🔗 Related Problems

- https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
- https://leetcode.com/problems/insert-interval/description/
