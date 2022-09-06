#!/bin/sh

JQ="/Users/mcherrie/goinfre/homebrew/Cellar/jq/1.6/bin/jq" #где у меня лежит jq
OUTPUT_FILE="./hh.json"
VACANCY_AMOUNT="20" # количество вакансий, которое надо вывести
VACANCY_NAME="${1/ /+}" # название вакансии - первый аргумент, у нас ‘data scientist’
curl -k -H 'User-Agent: api-test-agent' -G "https://api.hh.ru/vacancies?text=$VACANCY_NAME&per_page=$VACANCY_AMOUNT" | $JQ > $OUTPUT_FILE

# запускать командой bash hh.sh ‘data scientist’
