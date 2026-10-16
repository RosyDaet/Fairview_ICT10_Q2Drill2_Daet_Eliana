
from pyscript import document, display

# Mutable set
color = {"green", "yellow", "pink", "blue", "pink", "PINK"}
color.add("gravy")
display(color, target="output1")

# Set containing different data types
my_set = {1, 1.15, "number"}
display(my_set, target="output1")

# Union
set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "banana", "melon", "watermelon"}

display(set1 | set2, target="output1")
display(set1.union(set2), target="output1")

# Intersection
Iset = {"apple", "banana", "cherry"}
Iset2 = {"pineapple", "banana", "melon", "watermelon"}

display(Iset & Iset2, target="output1")
display(Iset.intersection(Iset2), target="output1")

# Difference
display(Iset - Iset2, target="output1")
display(Iset2 - Iset, target="output1")
display(Iset.difference(Iset2), target="output1")

# Symmetric difference
display(Iset ^ Iset2, target="output1")
display(Iset.symmetric_difference(Iset2), target="output1")

# Subset
A = {"burger", "fries"}
B = {"burger", "fries", "coke", "pie"}

display(A < B, target="output1")
display(A.issubset(B), target="output1")

# Superset
display(B >= A, target="output1")
display(B.issuperset(A), target="output1")
