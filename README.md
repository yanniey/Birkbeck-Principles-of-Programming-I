# Principles of Programming I
## Master of Data Science at Birkbeck, University of London
### 10/2018

Summary:

### Syllabus   
  1: Just Enough Python to Get Started  
  2: Program Control Structures  
  3: Collections and Strings  
  4: Memory and References  
  5: Recursion  
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

<b>Set</b>
* Sets `{}` have no order: {1,4} is the same as {4,1}. You cannot access the index/position of an item in a set. 
* Sets must to store immutable objects: the set itsel is mutable, but objects in a set must be immutable.
  * Intergers are ok
  * List are not ok
  * Sets are not ok
* you can't use `+`, but you can use `|` for addition 
`s1={}  
s2={}  
s3=s1|s2`  
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


#### Week 4: Memory and References
#### Week 5: Recursion
#### Week 6. Files, Modules and Exceptions 
#### Week 7. Software development principles 
#### Week 8. Basics of Object-oriented programming 
#### Week 9. More of Object-Oriented Programming 
#### Week 10. Functional Programming
#### Week 11. Fundamental Data Structures 