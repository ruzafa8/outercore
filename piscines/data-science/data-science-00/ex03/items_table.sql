CREATE TABLE IF NOT EXISTS item (
    product_id SERIAL NOT NULL,
    category_id BIGSERIAL,
    category_code TEXT,
    brand TEXT,
);

COPY PUBLIC.item
FROM '/home/alex/42/outercore/piscines/data-science/data-science-00/subject/item/item.csv'
DELIMITER ',' CSV HEADER;