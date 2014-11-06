USAGE="usage: $0 database_name"
if [ $# -ne 1 ]
then
    echo $USAGE
    exit 1
fi

DATABASE=$1

set -x
psql -U postgres -c "DROP DATABASE IF EXISTS $DATABASE"
