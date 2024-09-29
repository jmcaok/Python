# Python

## Variables

Variables act as storage containers for your data. To create a variable in Python, you just need to name it and set it equal to some value.

```python
variable_name = variable_value
```

For example:

```python
name = "Joseph"
```

Most programming langauges require you to declare variables with data types. Python doesn't require you to do this but you can for the sake of readability. You do that as follows:

```python
variable_name:data_type = variable_value
```

For example:

```python
name:string = "Joseph"
```

## Input-Output

### Input

To accept input, you can call the function `input` like so:

```python
input(prompt:string)
```

where `prompt` is a message you want to give the user before they enter input.

Generally, it is good practice to store your input in a variable, like so:

```python
in = input("Enter input")
```

### Output

To return output, you can call the `print` function like so:

```python
print(output)
```

where `output` can be any datatype, but the data type has to be the same.

For example:

```python
print("hello"+" there") #this is allowed
print(9 + 9) #this is allowed

print("hello" + 9)  #this is not allowed
```

There is a way to print different data types together.

You can use the `f-string`. The `f` here stands for `formatted`.

You use the `f-string` as follows:

```python
print(f"Some text {variable} some more text")
```

Here's an example using the `name` variable:

```python
print(f"Hello {name}!")
```

This prints:

```shell
Hello Joseph!
```

## If statements

An if-statement in python has the following structure:

```python
if some_condition:
    do_something
```

`some_condition` is a logical operation that has to be true for `do_something` to happen.
Here's an example program:

<!-- yay!!! 100!!! -->

```python
if a<b:
    print("Hello!")

```

If we set `a=8` and `b=9`, then the output will be:

```shell
Hello!
```

But, if we set `a=9` and `b=8`, then the output will be:

```shell

```

There is no output. Can you guess why that is?

The reason is because we haven't handled what to do in the case that `a>=b`.

To handle that, we can use an `if-else` operation:

```python
if a<b:
    print("Hello!")
else
    print("Bye bye!")
```

Now, if `some_condition` is not true, then whatever is in the `else` will execute.

This is fine but what if we want to handle more than one condition? What if we wanted something different to happen when `a=b`? We can do this using an `elif` operation:

```python
if a<b:
    print("Hello!")
elif a==b:
    print("How are you?")
else
    print("Bye bye!")
```

Now we should get three different outputs depending on what our condition is.

### Logical operators

Logical operators are symbols we use to make comparisons. All logical operations evaluate to `true` or `false`.
Here are some that you will need:

- `>`: greater than
  - evaluates true if the item on the left is greater than the item on the right
  - `9>8`: true
  - `7>9`: false
- `<`: less than
  - evaluates true if the item on the left is less than the item on the right
  - `7<9`: true
  - `9<6`: false
- `==`: equal to
  - evaluates true if the item on the left is equal to the item on the right
  - `9==9: true
  - `7==9`: false
- `!=`: not equal to
  - evaluates true if the item on the left is not equal to the item on the right
  - `9!=8`: true
  - `9!=9`: false

You can also combine greater than with equals, `>=`, and less than with equals, `<=`. However, you cannot combine anything else.

You can also use `and` or `or`.

`and` if-statements will only evaluate to true if all conditions in the if-statement are true.

```python
if 9>8 and 9==9:
    print("Hello!")
else:
    print("Bye!")
```

This will print:

```shell
Hello!
```

But:

```python
if 9<8 and 9==9:
    print("Hello!")
else:
    print("Bye!")
```

This will print:

<!-- yay!!! 200!!! -->

```shell
Bye!
```

`or` if-statements will evaluate to true if at least one condition in the if-statement is true.

```python
if 9>8 and 9==9:
    print("Hello!")
else:
    print("Bye!")
```

This will print:

```shell
Hello!
```

And:

```python
if 9<8 and 9==9:
    print("Hello!")
else:
    print("Bye!")
```

This will also print:

```shell
Hello!
```

But:

```python
if 9<8 and 9!=9:
    print("Hello!")
else:
    print("Bye!")
```

This will print:

```shell
Bye!
```

Python also contains an `in` operator which checks if an item is in a list:

```python
if 'a' in "hello":
    print("Hello!")
else:
    print("Bye!")
```

The output will be:

```shell
Bye!
```

since `a` is not in `hello`

## Lists

In python, arrays are called lists. List are a type of variable that stores values in sequential order and in contiguous memory (meaning next to each other in memory)

A list in python is declared as follows:

```python
array = []
```

This initializes an empty array.
You can also initialize it like this:

```python
array:list
```

There are two ways to add elements to a list:

- On initialization:
  ```python
  array = [1,2,3,4,5]
  ```
- In the program:

  ```python
  array.append(6)
  ```

  The `append` method works by adding an item to the array at the back of the array.

You can also remove an item from the array:

```python
array.pop(index)
```

where `index` is the index in the array of the element you want to delete.

for example:

```python
array = [1,2,3,4,5]
array.pop(2)
print(array)
```

The output will be:

```python
[1,2,4,5]
```

You might be asking "why did 3 get removed, and not 2?"

That's because for lists, we start counting from 0, not 1.

### Accessing elements in a list

You can access elements in a list by doing the following:

<!-- yay!!! 300!!! -->

```python
array[index]
```

where `index` is the index in the array.
For example:

```python
array = [1,2,3,4,5]
print(array[3])
```

The output will be:

```shell
4
```

You can also change values of items using this method:

```python
array = [1,2,3,4,5]
array[3] = 10
print(array)
```

The output will be:

```shell
[1,2,3,10,5]
```

### List length

You can check how many elements are in a list with the `len` function:

```python
array=[1,8,3,7,5]
array_size = len(array)
print(f"There are {array_size} elements.")
```

The output will be:

```shell
There are 5 elements.
```

### Strings

Strings are a type of list made up of characters. This means that any operation that works for lists, works for strings.

You initialize a string in two ways:

```python
name = ""
surname:string
```

## Loops

Loops allow us to do repetitive executions with less code.

### For loop

The for loop repeats over a specified interval, with set increments or decrements.

The structure of a for loop is:

```python
for i in range(start, end, increment):
    do_something
```

where `i` is the current iteration number, `start` is where the loop begins, `end` is where the loop stops, `increment` is how big the jump from one iteration to the next is.

Lets look at an example:

```python
for i in range(0,5,1):
    print(i)
```

The output is:

```shell
0
1
2
3
4
```

Notice how 5 isn't printed?

This is because the `range` function goes from `start` to `end-1`.
