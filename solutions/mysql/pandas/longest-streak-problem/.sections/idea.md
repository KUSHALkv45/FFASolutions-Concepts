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