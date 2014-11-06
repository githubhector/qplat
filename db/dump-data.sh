TIMESTAMP=`date +"%Y-%m-%d-%H%M%S"`

set -x
pg_dump --data-only --column-inserts -U quantuser -f dumps/quant-$TIMESTAMP.sql quant
