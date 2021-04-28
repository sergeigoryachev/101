create table if not exists booking1 (date_time DATETIME, site_name INT, posa_continent INT, user_location_country INT, user_location_region INT, user_location_city INT, orig_destination_distance DOUBLE, user_id INT, is_mobile INT, is_package INT, channel INT, srch_ci DATE, srch_co DATE, srch_adults_cnt INT, srch_children_cnt INT, srch_rm_cnt INT, srch_destination_id INT, srch_destination_type_id INT, is_booking INT, cnt INT, hotel_continent INT, hotel_country INT, hotel_market INT, hotel_cluster INT)
row format delimited fields terminated by ','
STORED AS TEXTFILE;
