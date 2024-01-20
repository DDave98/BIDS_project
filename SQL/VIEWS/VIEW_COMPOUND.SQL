CREATE MATERIALIZED VIEW IF NOT EXISTS bids_xpech_michalica.compound_view AS
SELECT
  dn.compound,
  dt.ticker,
  dd.date,
  st.open,
  st.volume
FROM
  `bids_xpech_michalica.dim_news` dn
JOIN
  `bids_xpech_michalica.assets` st
ON
  dn.ticker = st.ticker
JOIN
  bids_xpech_michalica.dim_ticker dt
ON
  st.ticker = dt.ticker
JOIN
  bids_xpech_michalica.dim_date dd
ON
  dd.date = st.date