CREATE TABLE IF NOT EXISTS data_2022_dec (
    event_time TIMESTAMPTZ NOT NULL,
    event_type TEXT NOT NULL,
    product_id BIGINT NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    user_id BIGINT NOT NULL,
    user_session UUID
);

COPY PUBLIC.data_2022_dec
FROM '/home/alex/42/outercore/piscines/data-science/data-science-00/subject/customer/data_2022_dec.csv'
DELIMITER ',' CSV HEADER;