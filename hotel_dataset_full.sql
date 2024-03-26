with hotels as 
(
	SELECT * FROM "2018"
	union
	SELECT * FROM "2019"
	union
	SELECT * FROM "2020"
)

select * 
from hotels
join market_segment using(market_segment) 
join meal_cost using(meal)