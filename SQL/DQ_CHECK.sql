CREATE OR REPLACE TABLE `imperial-sensor-400812.xpech_michalica.stocks_v2` AS
SELECT * EXCEPT(rn)
FROM (
  SELECT *, ROW_NUMBER() OVER(PARTITION BY ticker ORDER BY ticker) rn
  FROM `imperial-sensor-400812.xpech_michalica.stocks_v2`
) 
WHERE rn = 1 