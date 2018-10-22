# Principles of Programming I
## Master of Data Science at Birkbeck, University of London
### 10/2018

### Course Format:
* On campus: 1 hour of lecture and 2 hours of lab per week
* Online: ~ 5 hours of coding coursework on websites & assignments

### Syllabus   
  1. Just Enough Python to Get Started  
  2. Program Control Structures  
  3. Collections and Strings  
  4. Memory and References  
  5. Recursion  
  6. Files, Modules and Exceptions   
  7. Software development principles   
  8. Basics of Object-oriented programming   
  9. More of Object-Oriented Programming   
  10. Functional Programming  
  11. Fundamental Data Structures 

#### Week 1: Just Enough Python to Get Started
* Input, output, printing
* Values and data types
* Arithmetic
* Conditions: if, then, else

#### Week 2: Program Control Structures
* Loops: while, for, nested loops
* Functions: fruitful, argument passing, return values, composition

#### Week 3: Collections and Strings
1. Difference between function and methods:
Methods may amend the state of an object, but function wouldn't.
2. Mutating vs. non-mutating object  
* An object is immutable if <b>all</b> of its methods are immutable
* `.append()` is a mutating method
* set `{}` are mutable, unordered, and does not contain duplicates
* list `[]` can be amended/mutated

<b>List</b> 
* python has zero indexing (i.e. first item always has index of 0)
* List operations: `sort()`,`reverse()`,`extend()`
* List[from: up to but not including]
* Iterate through a list with index:
```
for index in range(0, len(my_list)):
  print("Element", index, "is", my_list[index])
```

* Iterate through a list without index:
```
for element in my_list: 
  print(element, "is in the list")
```



<b>Set</b>
* Sets `{}` have no order: {1,4} is the same as {4,1}. You cannot access the index/position of an item in a set. 
* Sets must to store immutable objects: the set itsel is mutable, but objects in a set must be immutable.
  * Intergers are ok
  * List are not ok
  * Sets are not ok
* you can't use `+`, but you can use `|` for addition :
```
s1={}  
s2={}  
s3=s1|s2
```
* Iterate through a set:

```
for elemin s1:
  print(elem)
```


<b>Dictionary</b>
* Dictionaries associate keyswith values: `{“John Dow” : 123456789, “Michael Jackson” : 987654321}`
* Just like a set, dictionary is also not ordered.
* Dictionaries are mutable, but dictionary keys are immutable
* Cannot use list as keys for dictionary

Example:  
* `print(phonebook[“John Dow”])>> 123456789`
* `print(phonebook[“David Bowie”])>> Error`
* `phonebook[“David Bowie”] = 918273645` <- creating a new value pair
* `phonebook[“John Dow”] =6758493021` <- updating a value for the key>
* `“Michael Jackson” in phonebook>> True` <- check if a value is in the dictionary key
* `del phonebook[“Michael Jackson”]`  
`“Michael Jackson” in phonebook>> False` <- delete key/value for given key

Iterating through dictionary:
```
for key in dict:
  print(key, dict[key])
```
OR 
```
for key, valin dict.items():  
  print(key, val)
```
<b>Tuples</b>
* Tuple is for when you have a small (and better fixed) number of objects
* Tuples are <b>ordered</b> ,<b>indexed</b> and <b>immutable</b>.
* Objects stored in tuples is mutable(remember: tuples themselves are immutable)

* `tup= (‘a’, ‘b’, [100,200])`  
* `tup[2] = [500, 600]` <-Error  
* `tup[2][0] = 500` <-Ok  
* `tup[2][1] = 600` <-Ok  

#### Week 4: Memory and References

1. Memory partition: Stack and Heap  

<b>Stack</b> (similar to a locker): 
* Access to item is quick
* Only small items  

<b>Heap</b> (similar to a warehouse):
* Access to item is slow
* Large items  

Each variable A, B... mentioned in Python gets a "box" in the stack.  

The values of those variables are stored differently based on <u>datatype</u>.  

* Lighter datatype are stored on the stack
e.g.   
`integers, strings, floats, characters, Booleans`  
* Heavier datatypes are stored on the heap
with reference to the values stored on the stack, e.g.  
`lists, dictionaries, sets, classes`

When amending a list,  make a copy of the list (instead of the object itself)
```{py}
B=["Macbook","Toaster","Toilet Paper"]
C = B[:]
B[0] = “PC”
print(C)

```

Alternatively, use the `copy()` function
```{py}
import copy
...
C = copy.copy(B)
```

Double referencing, and `deepcopy()` function

M and N are still independent: 
```
import copy
M=[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
# attemps to copy M
N=copy.copy(M)
# this is not a real copy
```

This will make N truly independent of M: `deepcopy()`


```
N = copy.deepcopy(M)
```

#### Passing Arguments to Functions: 

For any variable `A`, when a function `fun(n)` is called on it:   
* a new variable n is created on the stack
* the stack content of `A` is copied to the stack content of `n`  

Therefore:
* If `A` has a lighter datatype, the <u>value</u> of A itself is copied to `n`
* If `A` has a heavier datatype, the <u>reference</u> to the value of `A` is copied to `n`
* The first mechanism of passing arguments is call by value
* The second mechanism is call by reference

Bottom line:
* Functions are called by <u>value</u> on arguments that are: `integers, floats, strings,...`
* Functions are called by <u>reference</u> on arguments that are: `lists, dictionaries, sets,...`

#### Returning function results

* What we have said about passing arguments to function applies to returning results from functions
* If `R` is the result to be returned from function `fun(n)` and `A = fun(n)`
  + If `R` has a lighter datatype, then the value of `R` itself is copied to `A`
  + If `R` has a heavier datatype, then the reference to the value of `R` is copied to `A`

#### Week 5: Recursion
#### Week 6. Files, Modules and Exceptions 
#### Week 7. Software development principles 
#### Week 8. Basics of Object-oriented programming 
#### Week 9. More of Object-Oriented Programming 
#### Week 10. Functional Programming
#### Week 11. Fundamental Data Structures 