SELECT user_id, srch_adults_cnt, srch_children_cnt, MAX(datediff(to_date(srch_co), to_date(srch_ci))) AS max_time
FROM booking1
WHERE srch_adults_cnt = 2 AND srch_children_cnt >= 1
GROUP BY user_id, srch_adults_cnt, srch_children_cnt
ORDER BY max_time desc
LIMIT 1;
