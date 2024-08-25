import itertools

#counter = counts the value 
counter = itertools.count(10 ,2)  #(start, step)

for i in counter:
    print(i)

    if i == 20:
        break


#cycle = creates a cycle 
l = ['a','b','c']    
cycler = itertools.cycle(l)

for i,letter in enumerate(cycler):
    print(i, letter,sep=":")

    if i == 20:
        break


#repeat = repeat the 
String = 'string'
repeater = itertools.repeat(String, 10) #(variable that contains the info you want to repeat, times to repeat )

print(list(repeater)) #here you have to convert to a list cause it is a itterable 



#accumalate = accumalates the numbers
import operator

numbers = [1,2,3,4,5]
accumalators = itertools.accumulate(numbers, operator.mul)

print(list(accumalators)) #operator.mul returns the multiplied accumalated numbers whereas default is add(+)


#chain = add two list and returns as a single list 
a = [1, 2, 3]
b = ['a', 'b', 'c']

combined = itertools.chain(a, b)

print(list(combined))


#dropwhile = drops the digits or variables according to the condition defined in the function 
z = [1, 2, 3, 4, 5, 6, 7, 1, 2, 2]
remaining = itertools.dropwhile(lambda n:n>3, z)
print(list(remaining))



#filterfalse

z_num = range(100)

filtered = itertools.filterfalse(lambda c:c % 10,z_num)
print(list(filtered))



#import itertools = groups the keys into iterable 
l_1 = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('b', 5), ('c', 6)]
grouped = itertools.groupby(l_1,lambda K:K[0])
for key,value in grouped:
    print(key,list(value), sep = ": ")



#slicing = slices the text 
l_string = ['a','b','c','d','e','f']

sliced = itertools.islice(l_string, 2, None)

print(list(sliced))



#pairwaise
l_pair = 'abcde'
paired = itertools.pairwise(l_pair)
print(list(l_pair))




#starmap 
l_star = [(2, 3),(2,4),(2,5)]
star_mapped = itertools.starmap(pow, l_star)
print(list(star_mapped))

#product = prints the cartesian product of two list 
List_1 = [1,2,3]
List_2 = ['a','b','c']
products = itertools.product(List_1, List_2)
for I_11 in list(products):
    print(I_11)



#permutations = do the permutations 
l_permute = ["A","B","C"]
permutations = itertools.permutations(l_permute, 2)
sorted_permutations = sorted(''.join(perm) for perm in permutations)
for perm in list(permutations):
    print(*perm)
#prints in lexogrraphical order 
#hackerrank soln
import itertools
S, K = input().split()
K = int(K)

permuted = itertools.permutations(S, K)




#combinations = do the combinations 
l_combine = [1,2,3,4,5]
combined = itertools.combinations(l_combine, 2)
for comb in list(combined):
    print(comb)


#combinations with replacement = do the replacement also print (1, 1)
l_combin1 = [1,2,3,4,5]
combined1 = itertools.combinations_with_replacement(l_combin1, 2)
for comb1 in combined1:
    print(comb1)