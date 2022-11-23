#!/usr/bin/env bash -l

years=('2016' '2017' '2018' '2019' '2020' '2021')

quarters=('1' '2' '3' '4')

for y in ${years[@]}; do
	#statements
	for q in ${quarters[@]}; do
		#statements
		python lda.py $y $q
	done
done