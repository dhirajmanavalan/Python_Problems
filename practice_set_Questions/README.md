# Python Logical Problems – I/O, Data Types, Conditionals, Loops

## 1. ATM Transaction Validator

### Problem Statement
An ATM processes **N withdrawal requests sequentially**.

Rules:
- Withdrawal amount must be a multiple of 100.
- Account balance must never go negative.
- For each transaction, print `SUCCESS` or `FAILED`.

### Input
```text
InitialBalance
N
amount1
amount2
...
amountN
```

### Output
```text
SUCCESS
FAILED
SUCCESS
...
FinalBalance
```

### Sample Input
```text
5000
4
1200
155
2000
2500
```

### Sample Output
```text
SUCCESS
FAILED
SUCCESS
FAILED
1800
```

### Hint
Update balance only if both conditions are satisfied.

---

## 2. Smart Electricity Billing

### Problem Statement
Electricity bill is calculated slab-wise:

- First 100 units → ₹3/unit
- Next 100 units → ₹5/unit
- Remaining units → ₹8/unit
- If usage > 300 units, add 10% surcharge.

### Input
```text
units
```

### Output
```text
total_bill
```

### Sample Input
```text
350
```

### Sample Output
```text
1540
```

### Hint
Apply slabs incrementally, then apply surcharge conditionally.

---

## 3. Password Strength Evaluator

### Problem Statement
Given a password string:

- Must contain at least 1 digit
- Must contain at least 1 uppercase letter
- Length ≥ 8

Print `STRONG` or `WEAK`.

### Input
```text
password
```

### Output
```text
STRONG
```

### Sample Input
```text
Pass1234
```

### Sample Output
```text
STRONG
```

### Hint
Loop through characters and count conditions manually.

---

## 4. Traffic Signal Simulation

### Problem Statement
A signal cycles every second:

- 1–30 → RED
- 31–45 → YELLOW
- 46–90 → GREEN

Given a time `T`, print the signal color.

### Input
```text
T
```

### Output
```text
RED / YELLOW / GREEN
```

### Sample Input
```text
44
```

### Sample Output
```text
YELLOW
```

### Hint
Use modulo arithmetic and range checks.

---

## 5. Salary Deduction System

### Problem Statement
Employee salary rules:

- Basic salary given
- If late days > 5 → deduct 5%
- If late days > 10 → deduct 10%
- If absent days > 2 → deduct additional 5%

### Input
```text
salary
late_days
absent_days
```

### Output
```text
final_salary
```

### Sample Input
```text
50000
8
1
```

### Sample Output
```text
47500
```

### Hint
Apply deductions cumulatively, not exclusively.

---

## 6. Prime Range Analyzer

### Problem Statement
Print the count of prime numbers between `A` and `B` (inclusive).

### Input
```text
A
B
```

### Output
```text
prime_count
```

### Sample Input
```text
10
30
```

### Sample Output
```text
6
```

### Hint
Check divisibility up to √n.

---

## 7. Online Order Discount Engine

### Problem Statement
Discount rules:

- ≥ 5000 → 20% discount
- ≥ 3000 → 10% discount
- ≥ 1000 → 5% discount
- Otherwise → No discount

Print the final payable amount.

### Input
```text
amount
```

### Output
```text
payable_amount
```

### Sample Input
```text
3200
```

### Sample Output
```text
2880
```

### Hint
Apply only the highest applicable discount.

---

## 8. Binary to Decimal Converter (Without Built-in)

### Problem Statement
Convert a binary number to decimal without using built-in conversion functions.

### Input
```text
binary_number
```

### Output
```text
decimal_number
```

### Sample Input
```text
101101
```

### Sample Output
```text
45
```

### Hint
Process digits from right to left using powers of 2.

---

## 9. Mobile Battery Drain Simulator

### Problem Statement
Battery starts at 100%.

Each app drains a fixed percentage per minute.

Stop when battery ≤ 0 and print the number of minutes used.

### Input
```text
drain_per_minute
```

### Output
```text
minutes
```

### Sample Input
```text
7
```

### Sample Output
```text
15
```

### Hint
Use a loop until battery <= 0.

---

## 10. Exam Result Processor

### Problem Statement
Input marks for 5 subjects:

- If any mark < 35 → FAIL
- Else average ≥ 75 → DISTINCTION
- Else → PASS

### Input
```text
m1 m2 m3 m4 m5
```

### Output
```text
FAIL / PASS / DISTINCTION
```

### Sample Input
```text
80 78 74 90 88
```

### Sample Output
```text
DISTINCTION
```

### Hint
First validate the failure condition, then classify.

---

## 11. Number Compression Counter

### Problem Statement
Count how many times a number can be divided by 2 until it becomes odd.

### Input
```text
number
```

### Output
```text
count
```

### Sample Input
```text
40
```

### Sample Output
```text
3
```

### Hint
Use a loop and modulo check.

---

## 12. Vowel Frequency Analyzer

### Problem Statement
Count total vowels in a sentence (case-insensitive).

### Input
```text
sentence
```

### Output
```text
vowel_count
```

### Sample Input
```text
I Love Python
```

### Sample Output
```text
4
```

### Hint
Normalize case before comparison.

---

## 13. Train Ticket Fare Calculator

### Problem Statement
Fare rules:

- Distance × ₹2/km
- Senior citizen → 30% discount
- Child (<12 years) → 50% discount

### Input
```text
distance
age
```

### Output
```text
fare
```

### Sample Input
```text
200
65
```

### Sample Output
```text
280
```

### Hint
Calculate base fare first, then apply age-based rule.

---

## 14. Number Pattern Validator

### Problem Statement
Check whether digits of a number are strictly increasing from left to right.

### Input
```text
number
```

### Output
```text
YES / NO
```

### Sample Input
```text
13579
```

### Sample Output
```text
YES
```

### Hint
Compare adjacent digits.

---

## 15. Smart Door Lock System

### Problem Statement
User gets 3 attempts to enter the correct PIN.

- Correct PIN → ACCESS GRANTED
- All attempts wrong → LOCKED

### Input
```text
correct_pin
attempt1
attempt2
attempt3
```

### Output
```text
ACCESS GRANTED / LOCKED
```

### Sample Input
```text
4321
1111
2222
4321
```

### Sample Output
```text
ACCESS GRANTED
```

### Hint
Exit the loop early on success.

---

## 16. Water Tank Overflow Detector

### Problem Statement
Tank capacity is 1000L.

Inflow is added every minute.

Stop when overflow occurs and print the minute number.

### Input
```text
N
inflow1 inflow2 ... inflowN
```

### Output
```text
overflow_minute
```

### Sample Input
```text
5
200 300 250 400 100
```

### Sample Output
```text
4
```

### Hint
Accumulate volume gradually.

---

## 17. Armstrong Number Checker

### Problem Statement
Check whether a number equals the sum of cubes of its digits.

### Input
```text
number
```

### Output
```text
YES / NO
```

### Sample Input
```text
153
```

### Sample Output
```text
YES
```

### Hint
Extract digits using modulo and division.

---

## 18. Bus Seat Allocation

### Problem Statement
A bus has 40 seats.

For each booking request:

- If seats are available → CONFIRMED
- Otherwise → WAITLISTED

### Input
```text
N
request1
request2
...
```

### Output
```text
CONFIRMED / WAITLISTED
```

### Sample Input
```text
3
15
10
20
```

### Sample Output
```text
CONFIRMED
CONFIRMED
WAITLISTED
```

### Hint
Track remaining seats.

---

## 19. Number Mirror Validator

### Problem Statement
Reverse a number and check whether it is equal to the original number.

### Input
```text
number
```

### Output
```text
PALINDROME / NOT PALINDROME
```

### Sample Input
```text
1221
```

### Sample Output
```text
PALINDROME
```

### Hint
Build the reverse using arithmetic operations.

---

## 20. Digital Lock Countdown

### Problem Statement
Repeatedly subtract the sum of digits from a number until a single digit remains.

### Input
```text
number
```

### Output
```text
final_digit
```

### Sample Input
```text
987
```

### Sample Output
```text
6
```

### Hint
Use nested loops: digit-sum calculation inside the reduction loop.

---