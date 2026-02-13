
---

# Longest Streak Problem

## 💡 Idea

**Links:**

* [https://platform.stratascratch.com/coding/2131-user-streaks?code_type=3](https://platform.stratascratch.com/coding/2131-user-streaks?code_type=3)
* [https://platform.stratascratch.com/coding/2059-player-with-longest-streak?code_type=3](https://platform.stratascratch.com/coding/2059-player-with-longest-streak?code_type=3)

### Main Idea

If we have a table like this:

```
user_id     win/loss
u1          W
u1          L
u1          W
u1          W
u1          W
u1          L
u1          W
u1          L
u1          L
```

We need to find the **longest streak**, which in this case is **3**.

To do this, we must mark all **consecutive W’s** as one unique group.
For that, we can use a **running sum** and count the number of losses (`L`) up to the current row.

This will transform the table into:

```
user_id     win/loss     (running sum) group_id
u1          W            0
u1          L            1
u1          W            1
u1          W            1
u1          W            1
u1          L            2
u1          W            2
u1          L            3
u1          L            4
```

Now, we can group by `user_id` and the generated `group_id` (considering only wins).

If the question is about **consecutive date streaks** (for example, login streaks), we can use:

```
date - row_number()
```

This creates a unique group ID for each continuous date streak.

---

## 💻 Code

### For Question 1

```sql
WITH cte AS (
    SELECT
        user_id,
        date_visited,
        date_visited
          - ROW_NUMBER() OVER (
                PARTITION BY user_id
                ORDER BY date_visited
            ) AS req
    FROM user_streaks
    WHERE date_visited <= '2022-08-10'
    GROUP BY user_id, date_visited
),
cte2 AS (
    SELECT
        user_id,
        MAX(cnt) AS fin
    FROM (
        SELECT
            user_id,
            COUNT(user_id) AS cnt
        FROM cte
        GROUP BY user_id, req
    ) t
    GROUP BY user_id
)
SELECT
    user_id,
    fin AS streak_length
FROM (
    SELECT
        user_id,
        fin,
        DENSE_RANK() OVER (ORDER BY fin DESC) AS dr
    FROM cte2
) t
WHERE dr < 4;
```

---

### For Question 2

```sql
WITH cte AS (
    SELECT
        *,
        SUM(IF(match_result = 'L', 1, 0))
            OVER (PARTITION BY player_id ORDER BY match_date) AS rn
    FROM players_results
),
cte1 AS (
    SELECT
        player_id,
        COUNT(match_date) AS strcnt
    FROM cte
    WHERE match_result = 'W'
    GROUP BY player_id, rn
),
cte2 AS (
    SELECT
        player_id,
        MAX(strcnt) AS streak
    FROM cte1
    GROUP BY player_id
)
SELECT
    player_id,
    streak AS longest_win_streak
FROM cte2
WHERE streak = (SELECT MAX(streak) FROM cte2);
```

---


