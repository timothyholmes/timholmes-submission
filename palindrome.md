# Phillies - Tim Holmes

Programmatic submission for Tim Holmes.

## Question 1: Palindrome

The following Python function checks whether a string is a palindrome. Please explain, in 250 words or less, how you'd improve this code and why. We’re not looking for a simple one-line rewrite here - submissions will be graded based on the clarity by which you describe what the improvements are, and also WHY they should be made. 

```python
def is_palindrone(s):
    r=""
    for c in s:
        r = c +r
    for x in range(0, len(s)):
        if s[x] == r[x]:
            x = True
        else:
            return False
    return x
```

## Answer 1

```python
def is_palindrome(s):
    length = len(s)
    for x in range(0, floor(length / 2)):
        reflected_index = (length - 1) - x
        if s[x] != s[reflected_index]:
            return False
    return True
```

We could make two changes to improve the space and time complexity. The first thing we should do is remove the initial loop that reverses the string. Due to the nature of palindromes, we already have all the information needed for this function in the input. This allows us to remove the `r` variable, reducing space complexity by half. Without the second variable to compare the string against, we must compare it against itself. This means that on each pass of the for loop we will check a character at each end of string, incrementing one index closer to the center at a time with two cursors. Since we are checking two characters on each pass, we only need to iterate for half the time. So the for loop needs to be for half of the string's length rather than the entire thing; we can even take the `floor` of the quotient, reducing the loops one more in cases with odd number strings. We never need to compare the middle character of an odd number string, since it's always the same on both sides.

I've included a time trial with a few different strings (even length palindrome, odd length, many characters, and not a palindrome), at `backend/palindrome.py`. You can run it after installing the tools in the main README, with the following commands.

```zsh
cd backend
poetry run python palindrome.py
```