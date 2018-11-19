# Principles of Programming I
## Master of Data Science at Birkbeck, University of London, 10/2018

### Course Format:
* On campus: 1 hour of lecture and 2 hours of lab per week
* Online: ~ 5 hours of coding coursework & assignments
* Exam: 1 hour practical exam(open-book, solution written on computer) + 1 hour written exam (closed-book, solution written on paper)

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
  12. Coursework Project

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

##### List
* python has zero indexing (i.e. first item always has index of 0)
* List operations: `sort()`,`reverse()`,`extend()`
* List[from: up to but not including]
* Iterate through a list with index:

```py
for index in range(0, len(my_list)):
  print("Element", index, "is", my_list[index])
```

* Iterate through a list without index:

```py
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
```python
s1={}  
s2={}  
s3=s1|s2
```
* Iterate through a set:

```python
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
```python
for key in dict:
  print(key, dict[key])
```
OR 
```python
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
```python
B=["Macbook","Toaster","Toilet Paper"]
C = B[:]
B[0] = “PC”
print(C)

```

Alternatively, use the `copy()` function
```python
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
Recursion must have a base case, similar to a `while` loop.

Recurvise and iterative implementations: recursive program will consume much more memory, making loop more efficient.

##### An example for recursion - calculate factorials:

```py
def fac(numb):
  if numb ==1: return 1
  else:
    fac_numb_minus_1 = fac(numb-1)
    result = numb*fac_numb_minus_1
    return result

fac(3)
```

1. Pros for using recursion ( in less demanding applications):
* many search and sort problems
* combinatorial problems: e.g., print all 0/1 strings of length n on Snakify  

2. Cons for using recursion:
* calling a function consumes more time and memory than adjusting a loop counter.
* high performance applications (graphic action games, simulations of nuclear explosions) hardly ever use recursion.      

Infinite Recursion (similar to infinite loop)

```py
def fac(numb):
  fac_numb_minus_1=fac(numb-1)
  result = numb*fac_numb_minus_1
  return result
```

* A recursive function must contain at least one non-recursive branch.
* The recursive calls must eventually lead to a non-recursive branch.


##### Calculate Fibonacci Numbers

```py
fib(0) = 0, fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)

def fib(n):
  if n == 0: return 0
  elif n==1: return 1 
  else:
    previous_fib_number = fib(n-1) 
    previous_previous_fib_number = fib(n-2)
    result = previous_fib_number + previous_previous_fib_number 
    return result
```

#### Week 6. Files, Modules and Exceptions 
* Files and Directories – text I/O, binary, random access
* Exceptions
* Modules and Libraries
* Random and important math functions

1. Files

* Opening a file
  ```py
  infile = open(“file1.txt”, "r") 
  ```
  or `“rb”` to inform Python the file is binary
* Read a number of symbols and return them as a string (and shift cursor) 
  ```py
  str = infile.read(10)
  ```
* Read a number of bytes and return them as a list 
  `ten_bytes = infile.read(10)`
* Read a whole line and return as string:
  `line = infile.readline()`
  + reading includes `\n` symbol too, so line will end with a character `\n` 
  + use `line.rstrip()` to remove that character
  + use `words = line.split(‘ ‘)` to get a list of words of line
  + `infile.readline()` returns empty string if cursor is at the end of file

* Writing to files
  + Opening a file
    `outfile = open(“file2.txt”, “w")` or `“wb”` to inform Python the file is binary
  + Convenient output formatting tool is string substitution % operator
    `formatted_string = string_where_substitutions_to_be_done % values`

    ```py
    N = 42
    formatted_string = “I have spotted %d camels” % N
    print(formatted_string)
    >>I have spotted 42 camels
    ```
    `%d` says that N should be formatted as a decimal integer

    ```py
    value = 3.14159265359
    print("%15.2f\n is pi" % value)
    >> 3.14
    ```
    `%15.2f` says that value should be printed as float, occupying 15 chars in total, and only2 chars after `.`

    `print(“I have spotted %d camels and pi is %15.2f” % (N, value))` using tuples to write to files.
  + Write a string to a file
    `outfile.write(str)`

* Example of reading and writing files
  ```py
  inputFileName = input("Input file name: ")
  outputFileName = input("Output file name: ")
  # open the input and output files
  infile = open(inputFileName, "r")
  outfile = open(outputFileName, "w")
  # Read the input and write the output.
  total = 0.0
  count = 0
  line = infile.readline() while line != "" :
  value = float(line) outfile.write("%15.2f\n" % value) total = total + value
  count = count + 1
  line = infile.readline()
  # Output the total and average.
  outfile.write("%15s\n" % "--------") 
  outfile.write("Total: %8.2f\n" % total) 
  avg = total / count 
  outfile.write("Average: %6.2f\n" % avg)
  # Close the files.
  infile.close() 
  outfile.close()  
  ```
* Reading the whole file at once (use with caution, e.g. when you know that the file is relatively small so that it doesn't take too much memory)
  ```py
  lines = infile.readlines()
  for line in lines:
    DoSomethingWith line
  ```
2. Exceptions
  ```py
  file_name = input("Enter name of the file to read: ")
  try:
      infile = open(file_name, "r")
      line = infile.readline()
      while line !='':
            print(line.rstrip())
            line = infile.readline()
  except FileNotFoundError:
      print('The file does not exist!')
  ```

  Ues `except Exception:` to cover all exceptions

#### Week 7. Software development principles (Errors and Testing, Unit testing, Git/Github)
1. Types of testing in software development
  * Unit test: when it fails, it tells you which piece of the code needs to be fixed
  * Integration test: when it fails, it says that pieces of the application are not working together as expected
  * Acceptance test: when it fails, it says that the application is not doing what the customer expects it to do
  * Regression test: when it fails, it says that the application no longer behaves the way it used to

2. Pytest for Unit Test
  For best practice, the test file should be in the same folder as the function that you want to test `my_module.py`. 

  ```py
  import pytest
  from my_module import *

  def test_somefunction():
      # some testing codes
  def test_someotherfunction()
      # some more testing codes
  ```

  Use `assert` statement for Pytest. The test is "passed" if the `Boolean_expression` evaluates to `True`, otherwise it failed.
  ```py
  def test_addition():
    assert(5==addition(3,2))
    # here addition(x,y) is the functon being tested
  ```

  To execute the tests, run `pytest` in command line when in the directory where both `test_somehting.py` and `my_module.py` are located.

  Only use `==` equality sign for integers. It might not work for floats. For floats, use `abs(A-B)<0.0001`

3. Test Driven Development(TDD)
  TDD Slangs:
    * Green: All tests pass
    * Red: Some tests fail
    * Refactor: Remove all duplicationa and smells created to just get the tests to work
    * Stub: a shortest possible implementation of a function that returns some meaning (but usually incorrect) value. Use stubs to check that functions return some sort of values. 

  ```py
  from my_math import *
  import pytest

  def test_reminder_by_2():
    assert mod_2(1) == 1
    assert mod_2(4) == 0
    

  def test_even():
    assert is_even(2) == True
    assert is_even(5) == False
  ```

  A stub would be:
  ```py
  def mod_2(n):
    # reminder from dvision by 2
    return 0
  
  def is_even():
    # test if the input is even
    return False
  ```

  On the command line(when you're in the correct folder where both functions are stored), simply type:
  ```py
  pytest
  ```

#### Week 8. Basics of Object-oriented programming 
1. Objects: code is written around an object, which is 
  * Data - a current state
  * Methods - operations that can access/change the state 

2. Classes: a "blueprint" for creating objects
  * A class is specified by
    + variable names to store data 
    + methods specified by 
      + method names
      + requires arguments to call them
      + their implementations

3. An example
  ```py
  class CashRegister : 
    def clear(self) :
      self._itemCount = 0 
      self._totalPrice = 0.0

    def addItem(self, price) :
      self._itemCount = self._itemCount + 1 
      self._totalPrice = self._totalPrice + price

    def getTotal(self) : # method 
      return self._totalPrice

    def getCount(self) : # method 
      return self._itemCount
  ```

4. The constructor: used to initialise the variables in an object
  ```py
  class CashRegister:
    def __init__(self):
      self._itemCount = 0
      self._totalPrice = 0.0
  ```
  The constructor should never be called explicitly, e.g. Don't do this:
  ```py
  register2346.__init__()
  ```

5. Methods, Self and Other
  * What if we want to call a method of a class from another method (i.e. asking about the variable of the same object, use `self`)
    ```py
    class CashRegister :
      def addItem(self, price):
        tot = self.getTotal()
        if tot <=100: self._itemCount = self._itemCount + 1 ...
    ```
  * Self and Other: distinguish object itself from `other`:
    ```py
    class CashRegister :
    def copy(self, other) : #copy the state of other cash register to this one
      self._itemCount = other._itemCount
      self._totalPrice = other._totalPrice
    ```
    In the main program:
    ```py
    register2346.copy(register5375)
    ```

6. Encapsulation

  * In Python there is no restriction on methods, but there's a convention that:
    + If a method starts **with underscore**, don't call them outside of the class definition code.
    ```py
    def main():
      ...
      register2346._totalPrice = 1000
    ```

7. Assigning Object Variables
  * Two instances of the same class that have the same content are **not identical to each ohter**

  ```py
  register2346 = CashRegister() 
  register5375 = CashRegister() 
  register2346.addItem(5.05) 
  register5375.addItem(5.05)
  
  print(register2346 == register5375)
  >> False
  ```

  * This is because `register2346` and `register5375` point to different pieces of memory, and therefore are not equal

  * To check that the content of two variables are the same:
  ```py
  class CashRegister :
    def isEqual(self, other):
      if self._itemCount == other._itemCount and self._totalPrice == other._totalPrice:
        return True
      else: return False
  ...
  def main():
    register2346 = CashRegister() 
    register5375 = CashRegister() 
    register2346.addItem(5.05) 
    register5375.addItem(5.05) 
    
    print(register2346.isEqual(register5375))
    >> True
  ```

8. Operators overloading: e.g. make `==` work in the same way as `isEqual(self,other)` by using operator overloading feature

  * `isEqual` should change to have a standard name `__eq__`, two arguments self and y, and return True or False i.e.,
  ```py
  class CashRegister : 
    def __eq__(self, y):
      if self._itemCount == y._itemCount and self._totalPrice == y._totalPrice: 
        return True
      else: return False
  ```

  Then we can do:
  ```py
  register2346 = CashRegister() 
  register5375 = CashRegister() 
  
  print(register2346 == register5375) 
  >> True
  ```


#### Week 9. More of Object-Oriented Programming 
#### Week 10. Functional Programming
#### Week 11. Fundamental Data Structures 
#### Exams
#### Regarding old exam papers
The file below provides not the final version (I publish what I could get) but the pre-final one that may slightly differ in wording, figures, and other minor things. The problems at the examination were anyway those from the file.  

The part-A "Practical" is an exam, where you program your solutions on a machine in our lab with a semi-locked and monitored account, which will be different from the account you currently use. You can use books, WWW, and any other resources (for example, the code of your solutions to the programming problems). For that reason, problems here are harder than in the other part.  

The part-B "Written" is the closed-book exam where you write the solutions on paper.
Each part is a 1 hour examination submitted and marked independently from the other part. They are likely to be in the same day though. 