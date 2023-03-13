import csv
with open('biostat.csv','r') as csv_file:
 f=csv.reader(csv_file)
 #(csv_file)
 for fi in f:
  print(fi)
 