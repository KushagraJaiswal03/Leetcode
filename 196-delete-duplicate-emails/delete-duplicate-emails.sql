delete p2
FROM Person p1 inner join Person p2
where p1.email = p2.email and
p1.id < p2.id 