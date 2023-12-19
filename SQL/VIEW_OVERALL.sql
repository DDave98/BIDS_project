CREATE MATERIALIZED VIEW xpech_michalica.test_view AS
  SELECT 
    dt.ticker,
    ds.sector,
    dd.date,
    dd.day,
    dd.month,
    dd.year,
    stc.high, 
    stc.low, 
    stc.open, 
    stc.close 
  FROM `imperial-sensor-400812.xpech_michalica.stocks_v2` stc
  JOIN
    `imperial-sensor-400812.xpech_michalica.dim_date` dd
  ON
    stc.date = dd.date
  JOIN 
    `imperial-sensor-400812.xpech_michalica.dim_ticker` dt
  ON
    stc.ticker = dt.ticker
  JOIN 
    `imperial-sensor-400812.xpech_michalica.dim_sector` ds
  ON
  dt.sector = ds.sector