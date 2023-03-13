from Bio.Seq import Seq

s = input()
my_seq = Seq(s)
print(my_seq.count("A"), end=" ")
print(my_seq.count("C"), end=" ")
print(my_seq.count("G"), end=" ")
print(my_seq.count("T"), end=" ")