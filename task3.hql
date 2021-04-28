SELECT hotel_country, hotel_market, hotel_continent, COUNT(*) AS total_searches
FROM booking1
WHERE is_booking = 0
GROUP BY hotel_country, hotel_market, hotel_continent
ORDER BY total_searches DESC
LIMIT 3;
