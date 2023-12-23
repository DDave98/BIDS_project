CREATE OR REPLACE MATERIALIZED VIEW xpech_michalica.ema_view AS
  SELECT 
    stc.date,
    stc.ticker,
    em.moving_avg, 
    stc.open,
    ds.sector
  FROM 
    xpech_michalica.stocks_v2 stc 
  JOIN
    xpech_michalica.ema_10 em 
    ON 
      stc.ticker = em.ticker 
      AND 
      stc.date = em.date
  JOIN
    xpech_michalica.dim_ticker dt
    ON
      stc.ticker = dt.ticker
  JOIN
    xpech_michalica.dim_sector ds
    ON
      dt.sector = ds.sector