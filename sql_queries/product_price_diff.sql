SELECT 
	psc.productcategoryid,
	psc.productsubcategoryid, 
	pc.name,
-- establish the highest and lowest price, then subtracts the MIN from the MAX 	
    MAX(prod.listprice) AS highest_price,
	MIN(prod.listprice) AS lowest_price,
	MAX(prod.listprice) - MIN(prod.listprice) AS price_difference
--pulls from productsubcategory table as base
FROM production.productsubcategory AS psc
--joins productcategory onto FROM
JOIN production.productcategory AS pc
ON psc.productcategoryid = pc.productcategoryid
--joins product onto FROM
JOIN production.product AS prod
ON psc.productsubcategoryid = prod.productsubcategoryid
--GROUPS prices to associated productids and names
GROUP BY psc.productcategoryid, psc.productsubcategoryid, pc.name
--orders by for readability
ORDER BY psc.productcategoryid, psc.productsubcategoryid
	
	
