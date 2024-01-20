CREATE OR REPLACE TABLE bids_xpech_michalica.correlate AS
SELECT * FROM
(
  SELECT 
    a.ticker stock_a,
    b.ticker stock_b,
    a.data price_stock_a,
    b.data price_stock_b,
    COALESCE(a.date, b.date) date,
    CORR(a.data, b.data) OVER (ORDER BY a.date) correlation
    FROM
    (
      SELECT 
        date, 
        AVG(open) data, 
        ticker
      FROM `bids_xpech_michalica.assets`
      WHERE 
        ticker = 'AAPL'
      GROUP BY 
        ticker, date
    )a
    JOIN
    (
      SELECT 
        date, 
        AVG(open) data, 
        ticker
      FROM `bids_xpech_michalica.assets`
      WHERE 
        ticker = 'MSFT'
      GROUP BY 
        ticker, date
    )b
    ON a.date = b.date
) WHERE correlation is not null