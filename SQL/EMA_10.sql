SELECT
  date,
  ticker,
  open,
  AVG(open) OVER (PARTITION BY ticker ORDER BY date ASC ROWS BETWEEN 10 PRECEDING AND CURRENT ROW) AS moving_avg
FROM
  xpech_michalica.stocks_v2;