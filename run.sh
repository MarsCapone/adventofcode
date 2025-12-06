#!/usr/bin/env zsh

year="$1"
day="$2"
shift 2

cd "$year"

exec python3 aoc${day}.py $@