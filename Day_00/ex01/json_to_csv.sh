# переводит файл, поданный первым аргументом из .jq в .csv, применяя фильтр filter.jq

INFILE=../ex00/hh.json
JQ="/Users/mcherrie/goinfre/homebrew/Cellar/jq/1.6/bin/jq" #где у меня лежит jq

$JQ -rf filter.jq $INFILE > hh.csv

# команда для вызова bash json_to_csv.sh