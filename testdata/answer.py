import csv

with open("5_5 SOL.csv") as f:
	csv_reader = csv.reader(f, delimiter=',')
	l = [a for a in csv_reader]
	for c in l[1:]:
		for q in c:
			print(q, end="\t")
		print()