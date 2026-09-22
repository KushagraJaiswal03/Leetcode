select p.product_id, IFNULL(ROUND(SUM(p.price*u.units)/SUM(u.units),2),0)AS average_pricE
from prices p
left join UnitsSold u
on p.prOduct_id=u.product_id
AND u.purchase_date >= p.start_date
and u.purchase_date <= p.end_date 
group by p.product_id