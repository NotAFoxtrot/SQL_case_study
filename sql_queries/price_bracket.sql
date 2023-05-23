select sum(case when productlistpricehistory.listprice > 1000 then 1 else 0 end) as above_1000,
		sum(case when (productlistpricehistory.listprice < 1000) and (productlistpricehistory.listprice >100) then 1 else 0 end) as below_1000_above_100,
		sum(case when (productlistpricehistory.listprice < 100) and (productlistpricehistory.listprice >0) then 1 else 0 end) as below_100_above_0
from production.productlistpricehistory
-- no need to join, just had to do conditional sums in the select in order to obtain brackets