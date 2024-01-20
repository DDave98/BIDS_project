CREATE OR REPLACE TABLE bids_xpech_michalica.ema50 AS SELECT
  date,
  ticker,
  open,
  AVG(open) OVER (PARTITION BY ticker ORDER BY date ASC ROWS BETWEEN 50 PRECEDING AND CURRENT ROW) AS moving_avg
FROM
  bids_xpech_michalica.assets;