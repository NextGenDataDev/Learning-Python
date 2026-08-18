# Chapter 11 — Python Essentials: Errors, Files, and Modules

## 1. Try / Except: Error Handling

Error handling allows a program to deal with unexpected situations without crashing.

### When to use `try` / `except`

Use it when:

1. You're dealing with user input.
2. You're working with files, networks, or APIs.
3. You're doing operations that could fail, such as division.
4. You want to give a helpful error message instead of allowing the program to crash.

### Basic Syntax

```python
try:
    # Code that might cause an error
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if that error occurs
    print("You can't divide by 0")
finally:
    # Code that always runs
    print("Done")
```

### What each part does

- `try` → contains code that might raise an error.
- `except` → handles a particular error.
- `finally` → runs whether an error occurs or not.

---

## 2. Catch Specific Errors

It's better to catch the specific error I expect instead of using a broad `except` for everything.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number.")
```

Here, `ValueError` occurs when Python cannot convert the input into an integer.

Specific error handling makes the program easier to understand and debug.

---

## 3. Common Errors

### `ValueError`

Happens when a value has the correct general type but an inappropriate value.

```python
age = int("hello")
```

Python cannot convert `"hello"` into an integer, so a `ValueError` occurs.

### `TypeError`

Happens when an operation is performed on an inappropriate type.

```python
result = "5" + 2
```

A string and an integer cannot be added this way, so Python raises a `TypeError`.

### `ZeroDivisionError`

Happens when attempting to divide by zero.

```python
result = 10 / 0
```

### `NameError`

Happens when Python cannot find the variable or name being referenced.

```python
print(score)
```

If `score` has not been defined, Python raises a `NameError`.

---

## 4. Reading Errors Instead of Panicking

An error message is not just Python saying:

> "Something went wrong."

It usually tells me what went wrong and where.

When an error occurs, I should:

1. Read the traceback from top to bottom.
2. Find the line where the problem occurred.
3. Look at the error type at the bottom.
4. Read the message describing the problem.
5. Trace the problem back to the code that caused it.

### Important habit

> **Don't panic when I see a traceback. Read it.**

Deliberately causing an error and reading the actual message is useful practice because it builds the habit of debugging instead of guessing.

---

## 5. Files

Python can work with files so that programs can read existing information and save new information.

A common pattern is:

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

The `with` statement is useful because Python automatically handles closing the file after the block finishes.

### Common file modes

| Mode | Meaning |
|---|---|
| `"r"` | Read |
| `"w"` | Write and replace existing content |
| `"a"` | Append to existing content |

### Writing to a file

```python
with open("notes.txt", "w") as file:
    file.write("Learning Python")
```

Be careful with `"w"` because it replaces the existing contents of the file.

### Appending to a file

```python
with open("notes.txt", "a") as file:
    file.write("\nLearning SQL")
```

This adds content to the end of the file instead of replacing the existing content.

---

## 6. Modules

A module is a Python file containing code that can be imported and reused in another Python file.

For example, suppose I have:

```text
calculator.py
main.py
```

Inside `calculator.py`:

```python
def add(a, b):
    return a + b
```

I can use the function from `main.py`:

```python
from calculator import add

print(add(5, 3))
```

Output:

```text
8
```

The main idea is:

> **Write reusable code once, then import it where I need it.**

---

## 7. Why Modules Matter

Modules help me:

- Organize larger programs.
- Reuse code.
- Avoid putting everything into one huge file.
- Separate related functionality.
- Make projects easier to maintain.

As my Python projects become larger, organizing code into modules becomes increasingly useful.

---

## 8. Common Mistakes

### Mistake 1: Catching every error blindly

Avoid relying on:

```python
try:
    ...
except:
    ...
```

when I know which error I expect.

A specific exception is usually better:

```python
except ValueError:
```

This makes debugging easier and prevents unrelated problems from being hidden.

### Mistake 2: Forgetting that `"w"` replaces file contents

```python
open("notes.txt", "w")
```

does not mean "add something to the file."

It means write to the file and replace its existing contents.

Use `"a"` when I want to append.

### Mistake 3: Treating an error message as the enemy

A traceback contains useful information.

Instead of immediately searching for the answer, I should first ask:

> What error occurred?
>
> Which line caused it?
>
> What was Python trying to do?

---

## 9. Business / Practical Questions

The concepts in this chapter appear in real programs.

### Error handling

> "What happens if a user enters text where a number is expected?"

Use `try` / `except`.

### Files

> "How can a program save a user's records so they are still available later?"

Use file operations or another form of persistent storage.

### Modules

> "How can I separate database functions from the rest of my application?"

Put related functions into a module and import them where needed.

---

## 10. Key Takeaways

```text
try
→ Code that might cause an error

except
→ Handles an expected error

finally
→ Runs whether an error occurs or not

ValueError
→ Invalid value for an operation

TypeError
→ Incompatible type used in an operation

ZeroDivisionError
→ Division by zero

NameError
→ Python cannot find the referenced name

with open(...)
→ A convenient and safer way to work with files

"r"
→ Read

"w"
→ Write/replace

"a"
→ Append

module
→ A Python file containing reusable code
```

---

# Final Lesson

Chapter 11 is really about making Python programs **more reliable and organized**.

Instead of allowing every unexpected situation to crash the program, I can handle expected errors.

Instead of keeping everything in memory, I can work with files.

Instead of putting every function into one enormous script, I can organize reusable code into modules.

Most importantly:

> **When Python gives me an error, I should read the traceback before trying to fix it.**
