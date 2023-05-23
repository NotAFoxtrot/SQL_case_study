SELECT 
	EXTRACT(YEAR from orderdate) AS "Year",
	EXTRACT(MONTH from orderdate) AS "Month",
	SUM(subtotal)
FROM sales.salesorderheader
GROUP BY EXTRACT(YEAR from orderdate), EXTRACT(MONTH from orderdate)
ORDER BY EXTRACT(YEAR from orderdate), EXTRACT(MONTH from orderdate)