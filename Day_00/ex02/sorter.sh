INFILE=../ex01/hh.csv
OUTFILE=hh_sorted.csv

head -n 1 $INFILE > $OUTFILE; # перезаписываем первую строку с заголовками
tail -n +2 $INFILE | sort -t, -k2 -k1 >> $OUTFILE; # все кроме первой строки сортируем сначала по второму столбцу, потом по первому в порядке возрастания

# команда для вызова bash sorter.sh