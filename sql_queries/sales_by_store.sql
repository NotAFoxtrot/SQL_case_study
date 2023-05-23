select s.name, storeid, soh.customerid, sum(soh.subtotal)
from sales.salesorderheader as soh
join sales.customer as c
using (customerid)
join sales.store as s
on storeid = businessentityid
group by 1,2,3
order by sum(soh.subtotal) DESC
--had to bunnyhop through tables in order to match up store id with the total sales