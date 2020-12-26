'''



Given input two lists
find intersection and have to remove duplicates


A = {0, 2, 4, 6, 8}; 
B = {1, 2, 3, 4, 5}; 
  
# union 
print("Union :", A | B) 
  
# intersection 
print("Intersection :", A & B) 
  
# difference 
print("Difference :", A - B) 
  
# symmetric difference 
print("Symmetric difference :", A ^ B) 
Output:

('Union :', set([0, 1, 2, 3, 4, 5, 6, 8]))
('Intersection :', set([2, 4]))
('Difference :', set([8, 0, 6]))
('Symmetric difference :', set([0, 1, 3, 5, 6, 8]))
'''

def interList(Num1,Num2):
    return list(set(Num1)&set(Num2))

def minuList(Num1,Num2):
    return list(set(Num1)-set(Num2))


def UnionList(Num1,Num2):
    return list(set(Num1)|set(Num2))

def SymmetricDiffList(Num1,Num2):
    return list(set(Num1)^set(Num2))


'''
the symmetric difference of two sets, also known as the disjunctive union,
 is the set of elements which are in either of the sets, 
 but not in their intersection.
'''