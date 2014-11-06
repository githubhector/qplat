USAGE="usage: $0 database_name owner"
if [ $# -ne 2 ]
then
    echo $USAGE
    exit 1
fi

DATABASE=$1
OWNER=$2


SQL="CREATE DATABASE $DATABASE \
      WITH OWNER = $OWNER \
        ENCODING = 'UTF8' \
        TABLESPACE = pg_default \
        LC_COLLATE = 'en_US.UTF-8' \
        LC_CTYPE = 'en_US.UTF-8' \
        CONNECTION LIMIT = -1;"



set -x
psql -U postgres -c "$SQL"
