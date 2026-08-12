DaMu-Learning ZIP.zip
Zip Archive
Let's deal with tech here. I'm on a deadline to learn all the July to December documents in this ZIP file in 60 days. 
Why you may ask. I want to have at least something, a portfolio and projects on me. So that I can actually find a good placement for this 2 months IT. It may not be paid, but I'm aiming for a respectable company in Ikeja. It'd actually be a bonus and blessing to me if I get something paid.
But the problem is, I find learning boring. So I don't even open these documents when I know I have a goal to reach. A goal that'd make me happy. I even asked Claude to make these documents for me since I hated watching/video learning. I like reading so these were good to me.
But I just find education boring. Help me!!!😭
What option should I pick? I'm trying to s t up my Git...
??
??
??
??
??
??
Wednesday 7:11 PM
techher25-field-of-view-brochure (1).pdf
PDF
Heyyy... I'm back. So today I attended a tech program that was sponsored my IHS and was brought to life by Techlytics Institute of Technology. This programme was meant for the girls who underwent the online programme of 8 weeks. And they got a freaking certificate to boot. I won't lie I was jealous of my friend (the one I kept waiting for to buy her gym equipment up until this week). Normally, I used to follow her, do whatever she does, buy whatever she buys. She doesn't go to class so I was surprised when she said she was doing these online classes. SO now she has lots of DS and ML projects on her github then along with this computer vision project from this programme and the certificate she got. She's basically employable now. Unlike me that still doesn't have anything to show for it. I was jealous at her and sad for me at the same time.
Anyways, I want you to read through the attached documents and extract the names of the IHS founder, Techlytics founder, the panel speakers that spoke (they were three, one lecturer from UI) and other people you feel i should look into for my growth.
techher25-field-of-view-brochure (1)(1).pdf
PDF
Here's the brochure again
Pasted markdown.md
File
This is for chapter 6, how'd i do?:


Pasted markdown(1).md
File
I sent the text as an attachment
Pasted markdown(2).md
File
Here it is.
Sunday 10:02 PM
Chapter_7_Python_Basics_Notes.md
File
What do you think of this md file for chapter 7??
Chapter_8_Control_Flow_Notes.md
File
Here it is.

Done. I renewed and proofread Chapter 8 while preserving the original structure, terminology, and learning focus. I also added the missing “How do I know which structure to use?” reasoning layer and the English → logic → Python workflow.

Download the renewed Chapter 8 Markdown file 

Chapter_8_Control_Flow_Notes_Edited.md
Document
Chapter_9_Data_Structures_Notes.md
File
Here's the md file for chapter 9

Got it — I have the Chapter 9 Markdown file.

What do you want me to do with it: rate it and point out the issues, like we did for Chapter 8, or go straight to creating the renewed/proofread .md version?

Rate it then generate an edited and proofread version of it.
Chapter 9 rating: 9.1/10

This was already a strong note. The main improvements I made were about precision, reasoning, and making the notes useful when you're actually solving exercises.

What I changed
Tightened the definitions of lists, tuples, dictionaries, and sets.
Made IndexError vs KeyError more explicit.
Clarified the difference between in and .get().
Expanded the list-comprehension reasoning instead of just showing syntax.
Added a stronger "How do I choose the right data structure?" section.
Added a systematic way to break down data-structure questions.
Added more targeted common-error checklists.
Connected Chapter 9 to the reasoning approach we're building from Chapters 5–8: understand → break down → choose structure → code.
Preserved your actual Chapter 9 struggle rather than replacing it with generic textbook material.
Your biggest improvement

Your original note already said:

"I shouldn't think of these structures as random syntax."

That's exactly right.

I've expanded that into a decision-making framework because I don't want you reaching an exercise and thinking:

"Okay... they taught me dictionaries, lists and comprehensions. Which one am I supposed to magically know they want?" 😭

Instead, you'll have a set of questions to ask before coding.

Download the edited and proofread Chapter 9 Markdown file 

Chapter_9_Data_Structures_Notes_Edited.md
Document

Library
/
Period
/
Chapter_9_Data_Structures_Notes_Edited.md
Chapter 9 — Data Structures
What is Chapter 9 about?

Chapter 9 is about the basic Python structures I use to hold and organize data before pandas enters the picture.

It covers:

Lists []
Tuples ()
Dictionaries {}
Sets
Indexing and slicing
Dictionary key/value access
List comprehensions
Common errors such as IndexError, KeyError, and trying to modify a tuple

The bigger question is:

What kind of data am I holding, and which structure makes the most sense for it?

1. Lists

A list is ordered and mutable, meaning its items have a position and I can change the list after creating it.

courses = ["CSC321", "CSC322", "CSC331"]

I can:

courses.append("CSC341")
courses[0]      # first item
courses[-1]     # last item
courses[1:3]    # slice
Indexing

Python starts indexing from 0.

0 → first item
1 → second item
2 → third item

So if:

courses = ["CSC321", "CSC322", "CSC331"]

then:

courses[0]

returns:

CSC321
Slicing

Slicing lets me retrieve a range of items.

courses[1:3]

This starts at index 1 and stops before index 3.

IndexError

If a list does not contain the index I request, Python can raise:

IndexError: list index out of range

When I see this error, I should ask:

"How many items are actually in this list, and which indexes exist?"

2. Dictionaries

A dictionary stores key-value pairs.

student = {
    "name": "Data Muse",
    "gpa": 4.5,
    "department": "Computer Science"
}

I can retrieve a value using its key:

student["gpa"]

I can also add a new key-value pair:

student["year"] = 300

Think of a dictionary like this:

key          → value
"name"       → "Data Muse"
"gpa"        → 4.5
"department" → "Computer Science"

Instead of asking Python for an item by position, I can ask for the value associated with a specific key.

3. My Chapter 9 Dictionary Struggle

When I built my own dictionary, I had a small issue in the Courses list involving an extra empty string/adjacent string literal.

A cleaner version was:

me = {
    "Name": "NeuralMutee",
    "Department": "Computer Science",
    "GPA": 3.0,
    "Courses": ["CSC335", "CSC301", "CSC313", "MAT352", "GES103"]
}

The important lesson was not just the typo.

It was:

When a data structure looks wrong, inspect what is actually inside it.

I should pay attention to quotation marks, commas, brackets, parentheses, braces, and unexpected empty values.

4. KeyError

If I try:

student["age"]

but "age" does not exist in the dictionary, Python can raise:

KeyError

The distinction I need to remember is:

IndexError
→ invalid list position

KeyError
→ missing dictionary key
5. in vs .get()

This was one of the things I worked through in Chapter 9.

in
if "age" in student:
    print(student["age"])

This asks:

"Does this key exist?"

.get()
student.get("age")

If the key does not exist, .get() returns None instead of raising a KeyError.

I can also provide a default:

student.get("age", "Not available")

So:

in
→ checks whether the key exists

.get()
→ retrieves the value safely and can provide a default
6. List Comprehensions

A list comprehension is a compact way of creating a new list from an iterable.

squares = [x**2 for x in range(10)]

I can also filter values:

high_gpas = [g for g in [4.8, 3.2, 2.9, 4.1] if g > 3.5]

I can read this almost like English:

"Give me g for every g in this list, if g > 3.5."

Breaking it down
[g for g in gpas if g > 3.5]

means:

What do I want to put into the new list?
→ g

Where am I getting it from?
→ gpas

What condition must it satisfy?
→ g > 3.5
7. Chapter Exercise: Filtering Course Codes

A useful exercise is:

Get only the courses that start with "CSC3" from a list of course codes.

The logic is:

Take each course
→ check whether it starts with "CSC3"
→ keep it if the condition is true
→ put the results into a new list

The important thing is not just memorising the final comprehension.

I should be able to explain why each part is there.

8. Tuples

Tuples are ordered but immutable, meaning their items have positions but the tuple cannot be modified after creation.

my_tuple = ("CSC321", "CSC322")

I can access an item:

my_tuple[0]

But I cannot change an item:

my_tuple[0] = "CSC301"

That produces a TypeError.

The important distinction is:

List
→ ordered + mutable

Tuple
→ ordered + immutable
9. Sets

Sets are useful when I care about unique values and membership.

A set does not keep duplicate values.

For example:

departments = {"Computer Science", "Physics", "Computer Science"}

represents the unique values:

Computer Science
Physics

Sets are useful for questions such as:

"Which unique departments appear in this data?"

or:

"Have I already seen this value?"

The important idea is:

Use a set when uniqueness and membership are more important than keeping duplicate values.

10. Choosing the Right Data Structure

This is one of the most important lessons from Chapter 9.

I shouldn't think of lists, tuples, dictionaries, and sets as random Python syntax.

I should first ask:

"What kind of data am I holding, and how do I need to use it?"

If I need...

An ordered collection that I may change:

→ list

Ordered data that should not be changed:

→ tuple

Key → value relationships:

→ dictionary

Unique values or membership checks:

→ set

11. A Better Way to Read Data-Structure Questions

When I get a question, I should ask:

Step 1 — What am I storing?

Is it:

a collection of values?
a record with named properties?
unique values?
data that should remain unchanged?
Step 2 — How will I access it?

Do I need:

positions/indexes?
keys?
membership checks?
Step 3 — Will I need to change it?

If yes, a list may make sense.

If the data should remain unchanged, a tuple may be more appropriate.

Step 4 — Do duplicates matter?

If I need unique values, a set may be appropriate.

This is the same problem-solving habit I'm developing in SQL and Chapter 8:

Don't start with the syntax. Start with what the question is asking me to represent or do.

12. Business Questions
Lists

"Store the courses a student is taking."

Dictionaries

"Store a customer's name, location, and spending."

Sets

"Find the unique departments represented in a dataset."

List comprehensions

"From all transactions, give me only transactions above ₦100,000."

Dictionary safety

"If a customer record does not contain a phone number, don't crash the program."

13. Common Mistakes Checklist
Lists
Did I remember that indexing starts at 0?
Am I accessing an index that actually exists?
Did I accidentally use the wrong slice boundaries?
Am I confusing an index with the value stored at that index?
Dictionaries
Does the key actually exist?
Could accessing it directly cause a KeyError?
Should I use in or .get()?
Did I accidentally create an unexpected value because of a missing comma or quotation mark?
Tuples
Am I trying to modify an immutable tuple?
If I need to change the collection, should I use a list instead?
Sets
Do I actually need duplicates?
Am I choosing a set when order or indexed access matters?
List comprehensions

Before writing one, can I explain:

What value do I want in the new list?
What am I iterating over?
What condition, if any, should filter the values?
14. My Biggest Lesson

The biggest lesson from Chapter 9 is not:

"Memorise lists, tuples, dictionaries, and sets."

It is:

Choose the data structure based on what the data represents and how I need to use it.

For example:

Need ordered + changeable?
→ list

Need ordered + unchangeable?
→ tuple

Need key → value access?
→ dictionary

Need unique values?
→ set

And when I encounter an error, I should use the error message as a clue.

IndexError
→ check the list index

KeyError
→ check the dictionary key

TypeError when modifying a tuple
→ remember that tuples are immutable
Key Takeaways
List
→ ordered, mutable

Tuple
→ ordered, immutable

Dictionary
→ key-value pairs

Set
→ unique values

IndexError
→ invalid list index

KeyError
→ missing dictionary key

.get()
→ safely retrieves a dictionary value

in
→ checks whether a key exists

List comprehension
→ compact way to create/filter a list

I should also remember:

Python list indexing starts at 0.
Slicing can retrieve a range of list items.
Dictionaries let me access values through keys.
.get() can prevent a missing dictionary key from causing a KeyError.
Tuples are immutable.
Sets are useful for uniqueness and membership.
A list comprehension can combine iteration, transformation, and filtering.
The right data structure depends on what I need to store and how I need to work with it.
When I get stuck, I should break the question into smaller logical steps instead of guessing the syntax.
Chapter 9 Reasoning Checklist

When I get a data-structure question, ask:

What kind of data am I storing?

Do I need it to be ordered?

Will I need to change it?

Do I need to access values by position or by key?

Do duplicates matter?

What exactly does the question want me to produce?

Can I explain the logic before writing the syntax?

Chapter 9 in One Sentence

Data structures are the different ways Python lets me organize information so I can access, change, filter, and work with it effectively—and choosing the right one starts with understanding what the problem requires.