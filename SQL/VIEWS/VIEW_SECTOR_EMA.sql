CREATE MATERIALIZED VIEW IF NOT EXISTS bids_xpech_michalica.sector_view as SELECT 
    stc.date,
    stc.ticker,
    em.moving_avg, 
    stc.open,
    ds.sector
  FROM 
    bids_xpech_michalica.assets stc 
  JOIN
   bids_xpech_michalica.ema10 em 
    ON 
      stc.ticker = em.ticker 
      AND 
      stc.date = em.date
  JOIN
    bids_xpech_michalica.dim_ticker dt
    ON
    stc.ticker = dt.ticker
  JOIN
    bids_xpech_michalica.dim_sector ds
    ON
    dt.sector = ds.sector