# Day-80-Unique-Letters

Day 80/100 - Python Program that Displays which Letters are in First String but not in Second

# Letters in First String but not in Second

A program to dynamically compare two user-provided strings and extract the specific characters that exist in the first string but are absent—or appear less frequently—in the second string, utilizing Python's `collections.Counter` module.

## 📝 Description

This program analyzes two separate strings inputted by the user to determine exactly which characters from the first sequence do not carry over to the second sequence.

The core logic is handled efficiently within the `find_unique_letters(str1, str2)` function. Instead of using nested loops or basic sets (which would eliminate duplicate characters), this script imports the `Counter` class from Python's built-in `collections` module. It converts both strings into `Counter` dictionary objects (`count1` and `count2`), which automatically tally the frequency of every character.

By performing a mathematical subtraction (`count1 - count2`), the script elegantly generates a new `Counter` object containing only the elements from the first string whose counts are greater than their counterparts in the second string. Finally, it iterates through these unique items and uses `result.extend([char] * count)` to rebuild and return a standard list of these specific characters.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A string of text representing the first sequence (`str1`), provided via the terminal prompt.


* **Input 2:** A string of text representing the second sequence (`str2`), provided via the terminal prompt.



### Output:

* A formatted string stating: "Letters in the first string but not in the second string: [unique_letters]" where `[unique_letters]` is a Python list object containing the isolated characters.



### Rules:

1. The program must import `Counter` from the `collections` module.


2. The program must prompt the user to input two separate strings.


3. The core logic must be encapsulated in a function named `find_unique_letters(str1, str2)`.


4. The function must tally the characters of both strings using `Counter()`.


5. The function must isolate the unique characters via subtraction (`count1 - count2`).


6. The function must unpack the resulting dictionary back into a list format and return it.


7. The driver code must capture the returned list and print it to the console.



---

## 💡 Examples

### Example 1 (Standard Words)

**Input:**

```text
apple
pie

```

**Output:**

```text
Letters in the first string but not in the second string: ['a', 'p', 'l']

```

**Explanation:**

* `count1` for "apple" is `{'a': 1, 'p': 2, 'l': 1, 'e': 1}`.


* `count2` for "pie" is `{'p': 1, 'i': 1, 'e': 1}`.


* The subtraction removes one 'p' and the 'e', leaving `{'a': 1, 'p': 1, 'l': 1}`. The list reconstructs this as `['a', 'p', 'l']`.



### Example 2 (Complete Subtraction)

**Input:**

```text
hello
hello world

```

**Output:**

```text
Letters in the first string but not in the second string: []

```

**Explanation:** Every single character in the first string ("hello") exists in equal or greater quantities in the second string ("hello world"). The subtraction eliminates all keys, resulting in an empty list `[]`.

### Example 3 (Case Sensitivity)

**Input:**

```text
Data
data

```

**Output:**

```text
Letters in the first string but not in the second string: ['D']

```

**Explanation:** Python's `Counter` evaluates characters with strict case sensitivity. The uppercase 'D' in the first string is not cancelled out by the lowercase 'd' in the second string, so it remains in the final output.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script as "Day 80.py").

```bash
git clone https://github.com/adiaryaz/Day-80-Unique-Letters.git
cd unique-letters

```

2. **Run the program**:

```bash
python "Day 80.py"

```

Enter your two strings sequentially when prompted to instantly discover exactly which character frequencies belong exclusively to the first sequence!
