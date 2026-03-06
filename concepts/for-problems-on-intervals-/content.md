# For Problems On Intervals 

The 6 core interval models (this covers ~90%)

I’ll give each model:

what it means

how to recognize it

the canonical solution idea

example problems (LC-style)

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
sort by end
keep last_end
if start < last_end → conflict
Problems

Non-overlapping Intervals

Minimum Number of Arrows to Burst Balloons

Remove Covered Intervals

👉 This is the foundation model.

2️⃣ Interval Merging

“Combine overlapping ranges”

Recognition

“Merge”, “union”, “combine”

Output intervals, not counts

Key idea

Sort by start, extend current interval while overlapping.

Template
sort by start
if cur.start ≤ prev.end → merge
else push new interval
Problems

Merge Intervals

Insert Interval

Interval List Intersections

This one is easy but trains your overlap intuition.

3️⃣ Resource Allocation (VERY IMPORTANT)

“How many rooms / machines / CPUs do we need?”

Recognition

Meetings, rooms, machines, servers

Count of simultaneous intervals

Key idea

Sort by start

Use a min-heap of end times

If earliest end ≤ current start → reuse

Mental model

Heap stores active intervals.

Template
sort by start
for each interval:
    if heap.min_end ≤ start:
        pop
    push end
answer = heap size
Problems

Meeting Rooms II

Minimum Number of Platforms

CPU Task Scheduling

This is where heaps start feeling “magical”.

4️⃣ Interval DP / Weighted Scheduling (HARD but structured)

“Pick best non-overlapping intervals”

Recognition

Each interval has profit/weight

Want max sum

Overlaps not allowed

Key idea

Sort intervals

For each interval:

skip it

or take it + best compatible future interval

Binary search next valid interval

Template
sort by start
dp[i] = max(
    dp[i+1],
    profit[i] + dp[next_non_overlap]
)
Problems

Maximum Profit in Job Scheduling

Weighted Interval Scheduling

Scheduling with Profits

You already solved this. That’s huge.

5️⃣ Sweep Line / Event Model

“Something changes over time”

Recognition

Count at time points

Max overlap

Skyline-type problems

Key idea

Convert intervals into events:

+1 at start

−1 at end

Then sweep.

Template
events = [(start, +1), (end, -1)]
sort events
cur += delta
track max
Problems

Car Pooling

My Calendar

The Skyline Problem (advanced)

This avoids heaps entirely sometimes.

6️⃣ Greedy Replacement (Advanced Interval Trick)

“Keep best set so far, replace bad choices”

Recognition

Maximize count under constraints

Can replace earlier choice with better one

Key idea

Sort by end (or start)

Use max-heap

If constraint violated → remove worst interval

Template
sort intervals
push interval into heap
if constraint violated:
    pop worst
Problems

Course Schedule III

Max Number of Events That Can Be Attended

This is unintuitive at first, then extremely powerful.

How HARD interval problems are made

Hard interval problems are usually:

model 4 (DP) + binary search

model 3 (heap) + greedy invariant

model 5 (sweep) + tricky ordering

combinations of 2 models

They are not new models, just layered.

A universal 3-question checklist (use this every time)

When you see an interval problem, ask:

What do I sort by?

start?

end?

What is “active”?

overlapping intervals?

available resources?

Among active ones, which matters most?

earliest end?

max profit?

smallest / largest?

If you answer these, the solution structure appears.

Practice ladder (very important)

Don’t random-grind. Do this in order.

Level 1 (foundation)

Merge Intervals

Non-overlapping Intervals

Level 2 (heap intuition)

Meeting Rooms II

Minimum Number of Platforms

Level 3 (greedy replacement)

Course Schedule III

Max Events Attended

Level 4 (hard DP)

Maximum Profit Job Scheduling

Weighted Interval Scheduling variants

After this, most “hard” interval problems feel familiar.

