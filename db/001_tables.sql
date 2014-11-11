--------------------------------------------------------------------------------
--- Exchange table: one entry for each exchange where securities are traded
--------------------------------------------------------------------------------

CREATE TABLE exchange (
  id serial primary key,
  abbrev varchar(32) NOT NULL,
  name varchar(255) NOT NULL,
  city varchar(255),
  country varchar(255),
  currency varchar(64)
);


-------------------------------------------------------------------
--- Data source table: one entry for each source/vendor of data
-------------------------------------------------------------------

CREATE TABLE data_source (
  id serial primary key,
  name varchar(64) NOT NULL,
  website_url varchar(255)
);

-------------------------------------------------------------------
--- Symbol table: one entry per equity symbol. Can be any type 
--- of equity (stock, mutual fund, index, etc.)
-------------------------------------------------------------------

CREATE TABLE symbol (
  id serial primary key,
  symbol varchar(32) NOT NULL,
  description varchar(255),
  asset_type varchar(64) NOT NULL,
  sector varchar(255),
  industry varchar(255),
  data_source int references data_source(id),
  record_update_time timestamp NOT NULL
);

-------------------------------------------------------------------
--- Daily price table: end-of-day price and volume data
-------------------------------------------------------------------

CREATE TABLE daily_price (
  id serial primary key,
  data_source int references data_source(id),
  symbol int references symbol(id),
  date_time timestamp NOT NULL,
  open_price decimal(19,4),
  high_price decimal(19,4),
  low_price decimal(19,4),
  close_price decimal(19,4),
  adj_close_price decimal(19,4),
  volume bigint
);

-------------------------------------------------------------------
--- Investment account table
-------------------------------------------------------------------

CREATE TABLE investment_account (
    id serial primary key,
    account_type varchar(32),
    record_update_time timestamp NOT NULL
);

-------------------------------------------------------------------
--- Transaction table
-------------------------------------------------------------------

CREATE TABLE transaction (
  id serial primary key,
  data_source int references data_source(id),
  investment_account int references investment_account(id),
  date_time timestamp NOT NULL,
  action varchar(32) NOT NULL,
  symbol int references symbol(id),
  quantity int,
  price decimal(19,4),
  commission decimal(19,4),
  fees decimal(19,4),
  amount decimal(19,4), 
  record_update_time timestamp
);
