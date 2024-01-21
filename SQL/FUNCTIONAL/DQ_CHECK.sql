CREATE OR REPLACE TABLE `bids_xpech_michalica.assets` AS
SELECT * EXCEPT(rn)
FROM (
  SELECT *, ROW_NUMBER() OVER(PARTITION BY ticker ORDER BY ticker) rn
  FROM `bids_xpech_michalica.assets`
) 
WHERE rn = 1 