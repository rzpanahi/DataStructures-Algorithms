# Recursion Notes

## what is recursion?
Simply a function calling itself until a base condition.

## when to use recursion?
1. When we can divide the problem into sub-problems of similar nature.
2. When solving the sub-problem help us get to the main original problem.

## Solving Recursion Questions
1. Understand the problem (printing "321123")
2. Identify sub-problem (sub-problem is "2112")
3. Trust the recursive call (leap of Faith)
4. Link 1 and 2 (link "3 3" and "2112")
5. Set base condition (if 0 return)


## Base condition
Thw ways to find out base condition:
- find last valid input
- find first invalid input


## Recurrence Relation
Expresses the solution of a problem, os a function of solutions of the smaller instances of original problem.

basically a function of smaller instances of the same function, that expresses the recursion solution.


- ex: F(n) = n + F(n - 1)
- ex: F(n) = F(n - 1) + F(n - 2)