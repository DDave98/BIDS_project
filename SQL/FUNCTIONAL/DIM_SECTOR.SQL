CREATE OR REPLACE TABLE bids_xpech_michalica.dim_sector
AS SELECT DISTINCT(sector) 
FROM bids_xpech_michalica.dim_ticker;