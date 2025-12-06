#!/usr/bin/env zsh

function usage() {
    echo "Usage: SESSION={SESSION_COOKIE} $0 {year} {day}"
    exit 1
}

year="$1"
day="$2"

if [[ -z "$SESSION" || -z "$year" || -z "$day" ]]; then
    echo SESSION=$(echo "$SESSION" | base64)
    echo year=$1
    echo day=$2
    usage;
fi

mkdir -p "${year}"

echo "Writing to ${year}/${day}.txt"
curl -b "session=$SESSION" -s https://adventofcode.com/${year}/day/${day}/input > ${year}/${day}.txt