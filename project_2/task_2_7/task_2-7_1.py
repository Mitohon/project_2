data = ["11.11.2011", "12.12.2012", "24.06.1975", "31.05.2016"]
files = ["seq1", "seq2", "seq3", "seq4"]
for name in files:
    for digits in data:
        new_name = name + ".fasta_ " + digits
        print(f"{new_name}")
print ()
data = ["11.11.2011", "12.12.2012", "24.06.1975", "31.05.2016"]
files = ["seq1", "seq2", "seq3", "seq4"]
for name, date in zip(files, data):
    new_name = name + ".fasta_ " + date
    print(new_name)