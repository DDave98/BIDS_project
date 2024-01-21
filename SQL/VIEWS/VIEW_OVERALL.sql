CREATE MATERIALIZED VIEW IF NOT EXISTS bids_xpech_michalica.overall_view AS
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
  FROM `bids_xpech_michalica.assets` stc
  JOIN
    `bids_xpech_michalica.dim_date` dd
  ON
    stc.date = dd.date
  JOIN 
    `bids_xpech_michalica.dim_ticker` dt
  ON
    stc.ticker = dt.ticker
  JOIN 
    `bids_xpech_michalica.dim_sector` ds
  ON
  dt.sector = ds.sector