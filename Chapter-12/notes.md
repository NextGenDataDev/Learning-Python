# Chapter 12 — Object-Oriented Programming (OOP)

## 1. What Is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a way of organizing code by combining **data and the behavior that operates on that data** into objects.

Instead of having data and functions completely separate, OOP allows me to create objects that contain:

- **Attributes** → the object's data
- **Methods** → the actions the object can perform

A useful way to think about it is:

> **A class is a blueprint, while an object is an actual thing created from that blueprint.**

---

## 2. Understanding a Simple Class

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def classify(self):
        if self.gpa >= 4.5:
            return "First Class"

me = Student("Data Muse", 4.5)

print(me.classify())
```

### Output

```text
First Class
```

---

## What's Happening Here?

### 1. `class Student:`

This creates a **class** called `Student`.

The class acts as a blueprint for creating Student objects.

I'm basically saying:

> "A Student has a name, a GPA, and can perform actions such as classification."

---

### 2. `__init__()` — Initializing the Object

```python
def __init__(self, name, gpa):
```

`__init__()` is a special method that Python calls automatically when a new object is initialized.

It is used to initialize the object's attributes.

For example:

```python
me = Student("Data Muse", 4.5)
```

Python uses the values:

```text
name → "Data Muse"
gpa  → 4.5
```

and initializes:

```python
self.name = "Data Muse"
self.gpa = 4.5
```

### What is `self`?

`self` refers to the **specific object currently being worked with**.

So:

```python
self.name
```

means:

> "The `name` belonging to this particular Student object."

And:

```python
self.gpa
```

means:

> "The `gpa` belonging to this particular Student object."

---

### 3. `def classify(self):`

```python
def classify(self):
    if self.gpa >= 4.5:
        return "First Class"
```

This is a **method**.

A method is a function defined inside a class that represents behavior associated with its objects.

`classify()` looks at the GPA belonging to the specific Student object and determines whether it meets the condition.

For:

```python
me = Student("Data Muse", 4.5)
```

we have:

```python
self.gpa = 4.5
```

Since:

```python
4.5 >= 4.5
```

is `True`, the method returns:

```text
First Class
```

---

### 4. Creating an Object

```python
me = Student("Data Muse", 4.5)
```

This creates an **object**, also called an **instance**, of the `Student` class.

The class is the blueprint.

The object is the actual Student created from the blueprint.

Now the object has:

```python
me.name
me.gpa
```

which contain:

```text
Data Muse
4.5
```

---

### 5. Calling a Method

```python
print(me.classify())
```

This means:

> "Take the Student object stored in `me`, run its `classify()` method, and print the result."

The output is:

```text
First Class
```

---

# 3. The Whole OOP Idea in One Sentence

> **OOP allows me to bundle related data (attributes) and behavior (methods) together inside objects created from classes.**

---

# 4. Same Blueprint, Different Objects

What happens if I create another student?

```python
friend = Student("Ada", 3.2)
```

Now I have two different objects:

```text
me
friend
```

They were both created from the same `Student` class, but they contain different data.

```text
me
name → Data Muse
gpa  → 4.5

friend
name → Ada
gpa  → 3.2
```

However, there's an important issue with our current `classify()` method.

It only says what to return when:

```python
self.gpa >= 4.5
```

is true.

For Ada:

```python
3.2 >= 4.5
```

is false.

Since there is no `else` statement, the function reaches the end without returning a value.

Python therefore returns:

```python
None
```

So:

```python
print(friend.classify())
```

would output:

```text
None
```

### Better Version

```python
def classify(self):
    if self.gpa >= 4.5:
        return "First Class"
    else:
        return "Not First Class"
```

Now:

```python
print(me.classify())
print(friend.classify())
```

would output:

```text
First Class
Not First Class
```

This demonstrates an important OOP idea:

> **The same class can be used to create many objects, and each object can produce different results based on its own data.**

---

# 5. Instance Methods

These are the methods I already know from the `classify()` example.

Instance methods:

- Work with a specific object.
- Usually take `self` as their first parameter.
- Can access that object's attributes through `self`.

Example:

```python
class Course:
    def __init__(self, code, units):
        self.code = code
        self.units = units

    def describe(self):
        return f"{self.code} has {self.units} units"
```

Create an object:

```python
c = Course("CSC301", 3)
```

Call its method:

```python
print(c.describe())
```

Output:

```text
CSC301 has 3 units
```

The method works with the specific `Course` object stored in `c`.

---

# 6. Class Methods

A **class method** works with the class itself rather than one specific object.

It uses the:

```python
@classmethod
```

decorator and takes `cls` as its first parameter.

Example:

```python
class Course:
    all_courses = []

    def __init__(self, code, units):
        self.code = code
        self.units = units
        Course.all_courses.append(self)

    @classmethod
    def count_courses(cls):
        return len(cls.all_courses)
```

Create two courses:

```python
c1 = Course("CSC101", 2)
c2 = Course("CSC301", 3)
```

Then:

```python
print(Course.count_courses())
```

Output:

```text
2
```

### Why `cls` instead of `self`?

A simple way to remember it:

```text
self → this specific object

cls → the class itself
```

Class methods are useful when the operation concerns the class as a whole or when creating objects through alternative constructors.

---

# 7. Static Methods

A **static method** is a function placed inside a class because it is logically related to that class, but it does not need access to either:

- a specific object (`self`)
- the class (`cls`)

It uses:

```python
@staticmethod
```

Example:

```python
class Course:

    @staticmethod
    def is_valid_code(code):
        return code.startswith("CSC")
```

Use it like:

```python
print(Course.is_valid_code("CSC301"))
```

Output:

```text
True
```

The method doesn't need information from a particular Course object or from the Course class itself.

It's essentially a utility function that belongs conceptually with the class.

---

# 8. Special / Dunder Methods

Special methods are methods whose names begin and end with double underscores:

```text
__method__
```

They are often called **dunder methods**, short for "double underscore methods."

Python calls many of them automatically in response to certain operations.

| Method | When it is used | Example |
|---|---|---|
| `__init__` | When an object is initialized | `Course("CSC301", 3)` |
| `__str__` | When an object is converted to a string, such as with `print()` | `print(c)` |
| `__repr__` | When Python requests an official/debug representation | `repr(c)` |
| `__len__` | When `len()` is used | `len(c)` |
| `__eq__` | When objects are compared with `==` | `c1 == c2` |
| `__add__` | When objects are combined with `+` | `c1 + c2` |

These methods allow my own objects to interact with Python's built-in operations.

---

# 9. `__str__`

`__str__` controls the human-readable string representation of an object.

Example:

```python
class Course:
    def __init__(self, code, units):
        self.code = code
        self.units = units

    def __str__(self):
        return f"Course: {self.code}, {self.units} units"
```

Now:

```python
c = Course("CSC301", 3)

print(c)
```

Output:

```text
Course: CSC301, 3 units
```

Without a custom `__str__`, printing the object would not give this clean description.

---

# 10. `__len__`

`__len__` allows an object to work with Python's `len()` function.

```python
class Course:
    def __init__(self, code, units):
        self.code = code
        self.units = units

    def __len__(self):
        return self.units
```

Now:

```python
c = Course("CSC301", 3)

print(len(c))
```

Output:

```text
3
```

---

# 11. Properties

A **property** allows a method to be accessed like an attribute.

It uses:

```python
@property
```

Example:

```python
class Course:
    def __init__(self, units):
        self._units = units

    @property
    def is_major(self):
        return self._units >= 3
```

Create an object:

```python
c = Course(3)
```

Then:

```python
print(c.is_major)
```

Output:

```text
True
```

Notice that I don't use:

```python
c.is_major()
```

I use:

```python
c.is_major
```

The `@property` decorator makes the method behave like an attribute when accessed.

### Important Distinction

A property is **not another main method type** in the same sense as instance, class, and static methods.

It is a mechanism for controlling attribute-style access to a method.

---

# 12. Quick Comparison

| Type | Decorator | First parameter | Main purpose |
|---|---|---|---|
| Instance method | None | `self` | Work with a specific object's data |
| Class method | `@classmethod` | `cls` | Work with class-level data or provide alternate constructors |
| Static method | `@staticmethod` | None | Utility function related to the class |
| Special/dunder method | Depends on method | Usually `self` | Customize how objects interact with Python operations |
| Property | `@property` | `self` | Access calculated or controlled values like attributes |

---

# 13. The Most Important Distinction

When I get confused about these methods, I should ask:

### "What does this method need access to?"

```text
Does it need one specific object's data?
        ↓
Instance method
        ↓
self
```

```text
Does it need information about the class itself?
        ↓
Class method
        ↓
cls
```

```text
Does it need neither?
        ↓
Static method
        ↓
no self/cls
```

This is much more useful than trying to memorize the decorators without understanding why they exist.

---

# 14. Rule of Thumb

I don't need to use every type of method just because Python provides them.

A good starting point is:

> **Start with instance methods.**

Use:

- `@classmethod` when the operation genuinely concerns the class.
- `@staticmethod` when a utility function logically belongs to the class but doesn't need `self` or `cls`.
- Special methods when I want my objects to interact naturally with Python operations.
- `@property` when I want attribute-style access to calculated or controlled values.

The goal isn't to use as many OOP features as possible.

The goal is to use the **right tool for the problem**.

---

# 15. Key Takeaways

### OOP

```text
Class
→ Blueprint for creating objects

Object / Instance
→ Actual thing created from a class

Attribute
→ Data belonging to an object

Method
→ Behavior/action defined inside a class

self
→ Refers to the current object

cls
→ Refers to the class
```

### Method Types

```text
Instance method
→ Works with one specific object's data

Class method
→ Works with class-level data

Static method
→ Utility function related to class

Special/dunder method
→ Customizes how objects interact with Python operations
```

### Other OOP Features

```text
__init__
→ Initializes an object's attributes

__str__
→ Controls the object's human-readable string representation

@property
→ Allows method-based logic to be accessed like an attribute
```

---

# Final Lesson

The biggest lesson from Chapter 12 isn't simply:

> "Learn classes, objects, and different types of methods."

It's:

> **OOP is about organizing related data and behavior into objects created from reusable blueprints.**

A class defines what an object can have and do.

An object is a specific instance created from that class.

Different objects can use the same methods while producing different results because their data can be different.

And when working with methods, I should focus less on memorizing syntax and more on asking:

> **"What does this method need access to, and why does it belong here?"**
