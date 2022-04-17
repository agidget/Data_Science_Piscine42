#!/bin/bash
param1="search_field=name"
param2="text="
param2+=${1// /%}

curl -k -G --data-urlencode $param1 --data-urlencode $param2 \
        -H 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies' \
        | jq '.' > hh.json


# 'data scientist'