
-------------------------------------------------------------------------------------------
--- Schema roughly follows:
--- http://www.quantstart.com/articles/Securities-Master-Database-with-MySQL-and-Python
-------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------
--- Exchange table: one entry for each exchange where securities are traded
--------------------------------------------------------------------------------

CREATE TABLE exchange (
  id serial primary key,
  abbrev varchar(32) NOT NULL,
  name varchar(255) NOT NULL,
  city varchar(255),
  country varchar(255),
  currency varchar(64),
);


-------------------------------------------------------------------
--- Data source table: one entry for each source/vendor of data
-------------------------------------------------------------------

CREATE TABLE data_source (
  id serial primary key,
  name varchar(64) NOT NULL,
  website_url(255),
);

-------------------------------------------------------------------
--- Symbol table: one entry per equity symbol. Can be any type 
--- of equity (stock, mutual fund, index, etc.)
-------------------------------------------------------------------

CREATE TABLE symbol (
  id serial primary key,
  exchange_id int references exchange(id)
  ticker varchar(32) NOT NULL,
  instrument varchar(64) NOT NULL,
  name varchar(255)
  sector varchar(255)
  currency varchar(32)
);


-------------------------------------------------------------------
--- Daily price table: end-of-day price and volume data
-------------------------------------------------------------------

CREATE TABLE daily_price (
  id serial primary key,
  data_source_id references data_source(id)
  symbol_id int references symbol(id)
  date_time datetime NOT NULL,
  open_price decimal(19,4),
  high_price decimal(19,4),
  low_price decimal(19,4),
  close_price decimal(19,4),
  adj_close_price decimal(19,4),
  volume bigint,
);
