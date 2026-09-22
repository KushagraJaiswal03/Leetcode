# Write your MySQL query statement below


select s.user_id ,IFNULL(ROUND(SUM(action='confirmed')/count(*),2),0.00)  AS confirmation_rate 
from Signups s
left join confirmations c
on s.user_id = c.user_id
group by s.user_id
