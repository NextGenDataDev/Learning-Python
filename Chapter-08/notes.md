# Chapter 8 — Control Flow

## What is Chapter 8 about?

Chapter 8 is about **making Python make decisions and repeat actions**.

The three big ideas are:

- `if / elif / else` → make decisions
- `for` loops → repeat over a sequence or iterable
- `while` loops → repeat while a condition remains true

The chapter also introduces common mistakes such as indentation errors, missing colons, using `=` instead of `==`, and infinite loops.

---

## 1. `if`, `elif`, and `else`

Think of this as Python asking:

> **"Which situation am I in?"**

```python
gpa = 4.5

if gpa >= 4.5:
    print("First Class")
elif gpa >= 3.5:
    print("Second Class Upper")
else:
    print("Keep pushing")
```

Python checks the conditions from top to bottom and executes the first branch whose condition is true.

### When should I think about using `if`?

Use `if` when the problem requires Python to **make a decision**.

Ask:

> **"If this condition is true, what should happen?"**

For example:

> "If a student's GPA is at least 4.5, print `First Class`."

That is a decision problem, so `if` is appropriate.

---

## 2. `elif`

`elif` means **"else if."**

It allows me to check another condition when the previous `if` condition was false.

```python
gpa = 3.8

if gpa >= 4.5:
    print("First Class")
elif gpa >= 3.5:
    print("Second Class Upper")
else:
    print("Keep pushing")
```

Python checks the conditions in order.

If the first condition is false, it checks the `elif`.

If all the conditions are false, Python reaches the `else`.

### Important idea

The order of conditions matters.

Python checks from top to bottom and stops at the first true branch.

---

## 3. `else`

`else` handles the situation where none of the previous conditions were true.

```python
gpa = 2.5

if gpa >= 4.5:
    print("First Class")
elif gpa >= 3.5:
    print("Second Class Upper")
else:
    print("Keep pushing")
```

Here, neither of the first two conditions is true, so Python executes `else`.

Think of `else` as:

> **"If none of the previous conditions happened, do this instead."**

---

## 4. `for` Loops

A `for` loop is used to **iterate through the items in a sequence or iterable**, such as a list, string, or range.

```python
for i in range(5):
    print(f"Week {i + 1}")
```

The loop performs the action for each value produced by `range(5)`.

### When should I think about using `for`?

Ask:

> **"Do I need to perform an action for each item in something?"**

For example:

> "Print every student's name."

> "Go through every transaction and check something."

> "Calculate something for every value in a list."

These are natural `for`-loop problems.

---

## 5. `while` Loops

A `while` loop keeps running **while its condition is true**.

```python
count = 0

while count < 3:
    print(f"Attempt {count + 1}")
    count += 1
```

The loop starts with `count = 0`.

Python checks:

```python
count < 3
```

If the condition is true, the loop runs.

Then:

```python
count += 1
```

changes the value of `count`.

Eventually, `count` becomes `3`, the condition becomes false, and the loop stops.

### The question I should always ask

> **"What will eventually make this condition false?"**

Before writing a `while` loop, I should know what will cause the loop to stop.

---

## 6. The Infinite Loop Problem

A common `while`-loop mistake is forgetting to change the value that controls the condition.

```python
count = 0

while count < 3:
    print(count)
```

Here, `count` never changes.

It remains `0`, so `count < 3` remains true forever.

This creates an **infinite loop**.

The lesson is:

> **A `while` loop needs a clear path toward making its condition false.**

Before running one, ask:

> **"What changes during this loop?"**

> **"When will the condition become false?"**

---

## 7. Indentation

Python uses indentation to show which lines belong inside a block of code.

```python
if gpa >= 4.5:
    print("First Class")
```

The `print()` statement is indented, so Python knows it belongs to the `if` block.

Indentation also matters inside loops:

```python
for name in students:
    print(name)
```

The indentation tells Python that `print(name)` belongs to the loop.

### Key point

> **Indentation is part of Python's syntax.**

Incorrect indentation can cause an error or change the way the code behaves.

---

## 8. Don't Forget the Colon `:`

Statements that introduce a block need a colon.

```python
if condition:
```

```python
for item in items:
```

```python
while condition:
```

The colon tells Python that the block of code belonging to this statement starts here.

Forgetting it can produce a syntax error.

---

## 9. `=` vs `==`

This is one of the most important beginner distinctions.

### `=`

`=` is used for **assignment**.

```python
gpa = 4.5
```

This means:

> Store the value `4.5` in the variable `gpa`.

### `==`

`==` is used for **comparison**.

```python
gpa == 4.5
```

This asks:

> Is `gpa` equal to `4.5`?

For example:

```python
if gpa == 4.5:
    print("First Class")
```

### Easy way to remember

```text
=   → give/store a value
==  → ask whether two values are equal
```

---

## 10. How Do I Know Which One to Use?

This is one of the most important things I should learn from this chapter.

When I receive a Python question, I shouldn't immediately ask:

> **"What syntax do I remember?"**

Instead, I should ask:

> **"What is the problem asking Python to do?"**

### Use `if` when...

I need Python to make a decision.

Question clue:

> **"If this is true, what should happen?"**

Example:

> "If the student's GPA is above 4.5, print `First Class`."

→ Decision → `if`

### Use `for` when...

I need to perform an action for each item in something.

Question clue:

> **"For every item, what should I do?"**

Example:

> "Print every student's name."

→ Repetition over a collection → `for`

### Use `while` when...

I need to keep doing something while a condition remains true.

Question clue:

> **"Keep doing this while what is true?"**

Example:

> "Keep asking for a valid GPA until the user enters one."

→ Condition-controlled repetition → `while`

---

## 11. Quick Decision Test

```text
Am I making a decision?
        ↓
       YES
        ↓
       if

Am I doing something for every item in a sequence?
        ↓
       YES
        ↓
       for

Do I need to keep repeating until a condition changes?
        ↓
       YES
        ↓
      while
```

Sometimes a problem needs **more than one structure**.

For example:

> "Check every student's GPA and classify each student."

I'm doing something for every student **and** making a decision about each student.

So I may need:

```python
for student in students:
    if ...:
        ...
    elif ...:
        ...
    else:
        ...
```

This is an important step in my reasoning: **one problem can require multiple control-flow structures.**

---

## 12. Translating Questions Into Python

I want to develop an **English → logic → Python** habit.

### Example 1

> "If a student's GPA is at least 4.5, print `First Class`."

First:

```text
What is the question asking?
→ Make a decision.

What condition am I checking?
→ GPA >= 4.5

What structure handles a decision?
→ if
```

Then:

```python
if gpa >= 4.5:
    print("First Class")
```

### Example 2

> "Print every number from 1 to 20."

First:

```text
What is the question asking?
→ Repeat an action.

What am I repeating over?
→ A sequence of numbers.

What structure is appropriate?
→ for
```

Then:

```python
for number in range(1, 21):
    print(number)
```

### Example 3

> "Keep asking for a valid GPA until the user enters one."

First:

```text
What is the question asking?
→ Repeat an action.

Do I know exactly how many attempts there will be?
→ No.

What determines when I stop?
→ The user enters a valid GPA.

What structure is appropriate?
→ while
```

This is the kind of reasoning I need to practise instead of trying to guess the syntax immediately.

---

## 13. Business Questions

Control flow becomes useful when working with real data and business problems.

- **"Classify customers as low, medium, or high value based on their spending."**
  - Decision → `if / elif / else`

- **"Loop through every transaction and flag transactions above a threshold."**
  - Repeat over transactions → `for`

- **"Keep asking for input until the user enters valid data."**
  - Repeat until a condition changes → `while`

- **"Check every student's GPA and assign a classification."**
  - Repeat + decision → `for` + `if / elif / else`

- **"Process each item in a list and calculate something for it."**
  - Repeat over a collection → `for`

The important part is not memorising these examples.

It is learning to recognise the **type of problem** being described.

---

## 14. Common Mistakes Checklist

### If statements

- Did I use the correct condition?
- Did I use `==` when I meant "is equal to"?
- Did I put `:` after the condition?
- Did I indent the code inside the block?
- Are my conditions in the correct order?

### For loops

- Am I iterating over the correct sequence or iterable?
- Did I put `:` after the loop statement?
- Did I indent the code inside the loop?

### While loops

- Is the condition initially true when it should be?
- What changes inside the loop?
- What will eventually make the condition false?
- Did I accidentally create an infinite loop?
- Did I put `:` after the condition?
- Did I indent the loop body?

---

## 15. The Bigger Lesson From Chapter 8

Chapter 8 isn't really about memorising:

```python
if
for
while
```

It is about learning to **translate a question into logic**.

When I get a question, I should slow down.

### Step 1 — Understand the question

What exactly am I being asked to do?

### Step 2 — Identify the logic

Am I:

- making a decision?
- repeating over items?
- repeating until a condition changes?
- doing more than one of these?

### Step 3 — Choose the structure

```text
Decision → if / elif / else
Known sequence/collection → for
Condition-controlled repetition → while
```

### Step 4 — Write the Python

Only after I understand the logic should I worry about the exact syntax.

This is the same habit I am trying to develop with SQL:

> **Don't start by asking, "What command do I remember?"**

> **Start by asking, "What does this question require me to calculate or do?"**

---

## Key Takeaways

```text
if / elif / else
→ make decisions

for
→ repeat over a sequence or iterable

while
→ repeat while a condition is true

:
→ introduces a Python block

indentation
→ tells Python what belongs inside a block

=
→ assignment

==
→ comparison
```

I should also remember:

- Python checks `if / elif / else` conditions from top to bottom.
- A `for` loop is useful for iterating through items in a sequence or iterable.
- A `while` loop continues while its condition is true.
- A `while` loop needs a clear path toward becoming false.
- Forgetting to update the controlling condition can create an infinite loop.
- One problem can require multiple control-flow structures.
- The wording of a question can give me clues about which structure I need.
- I should understand the problem before trying to write the code.

---

## Control-Flow Checklist

When I get a Python question, ask:

> **What decision am I making?**

> **What am I repeating?**

> **Am I repeating over a known sequence or collection?**

> **Or am I repeating until a condition changes?**

> **What will make my `while` condition false?**

> **Did I use `:`?**

> **Did I indent the block correctly?**

> **Did I use `=` or `==` for the right reason?**

> **Could this problem require more than one control-flow structure?**

---

# Chapter 8 in One Sentence

> **Control flow is about teaching Python when to make a decision, when to repeat something, and when to stop—and learning to recognise which structure a problem actually requires.**
