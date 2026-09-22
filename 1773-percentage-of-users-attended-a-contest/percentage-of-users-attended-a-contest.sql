select contest_id ,ROUND(count(distinct user_id)*100/(select count(user_id)from Users),2) 
AS percentage
from Register
group by contest_id
order by percentage DESC, contest_id 