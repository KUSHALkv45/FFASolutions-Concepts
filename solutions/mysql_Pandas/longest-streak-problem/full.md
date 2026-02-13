# Longest Streak Problem

## 💡 Idea

```
link :  (https://platform.stratascratch.com/coding/2131-user-streaks?code_type=3)
link : (https://platform.stratascratch.com/coding/2059-player-with-longest-streak?code_type=3)

Main Idea :
if we have   table like this
user_id          win/loss
u1                    W
u1                     L
u1                     W
u1                     W
u1                     W
u1                      L
u1                     W
u1                     L
u1                     L


we have to find the longes streak here  which is 3  and for this we have to mark all consecutive W's as one unique group  for doing this the we can use rng sum and find the no of losses till current row

which will make our table look like this :

user_id          win/loss            (rngSum) groupId
u1                    W                          0
u1                     L                          1
u1                     W                        1
u1                     W                        1
u1                     W                        1
u1                      L                         2
u1                     W                        2
u1                     L                         3
u1                     L                         4

now we can group with user_i and unique group id we created  (with only wins ofcourse)

if the question is asked about consecutive dates streaks like logins etc .. use date - rowNumber this will create a unique group Id 

```

## 💻 Code

```python
#for 1st question :#

with cte as
(
select user_id , date_visited , date_visited - row_number() over (partition by user_id order by date_visited) as req
from  (select * from user_streaks where date_visited <= '2022-08-10' group by user_id , date_visited) t
),
cte2 as
(
select user_id , max(cnt) as fin
from
(
select user_id , count(user_id ) as cnt
from cte
group by 1,req
)t
group by 1
)

select user_id , fin as streak_length
from
(
select user_id , fin , dense_rank() over(order by fin desc) as dr
from cte2
) t
where dr < 4



#for 2nd question#

WITH cte AS (
    SELECT
        *,
        SUM(IF(match_result = 'L', 1, 0)) OVER (PARTITION BY player_id ORDER BY match_date) AS rn
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
WHERE streak = (SELECT MAX(streak) FROM cte2)
```

