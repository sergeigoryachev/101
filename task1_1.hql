SELECT hotel_country, count(*) as total_booking_per_country FROM booking1
WHERE is_booking = 1
GROUP BY hotel_country
ORDER BY total_booking_per_country desc
LIMIT 3;

