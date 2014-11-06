set -e

DATABASE=qplat
OWNER=qplatuser

echo "Dropping database $DATABASE..."
./drop-db.sh $DATABASE

echo "Creating database $DATABASE..."
./create-db.sh $DATABASE $OWNER

for SQL_FILE in *.sql
do
    CMD="psql -U $OWNER -d $DATABASE -f $SQL_FILE"
    echo "------------------------------------------------------------------------------------"
    echo "$CMD"
    eval $CMD
done
