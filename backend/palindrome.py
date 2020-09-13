import time
from math import floor


def original_is_palindrome(s):
    r = ""
    for c in s:
        r = c + r
    for x in range(0, len(s)):
        if s[x] == r[x]:
            x = True
        else:
            return False
    return x


def is_palindrome(s):
    length = len(s)
    for x in range(0, floor(length / 2)):
        if s[x] != s[(length - 1) - x]:
            return False
    return True


def do_and_cache_factory(thing_to_do, cache=dict()):
    def do_and_cache(s):
        if s in cache:
            return cache[s]
        else:
            result = thing_to_do(s)
            cache[s] = result
            return result

    return do_and_cache


def main(words):
    tim_palindrome = do_and_cache_factory(is_palindrome)

    for word in words:
        print("\nWord:", word)

        start_og = time.time()
        response = original_is_palindrome(word)
        end_og = time.time() - start_og
        print("OG", response, f"{end_og:.9f}")

        start_th = time.time()
        response = tim_palindrome(word)
        end_th = time.time() - start_th
        print("TH", response, f"{end_th:.9f}")

        if end_og < end_th:
            print("OG faster!")
        elif end_og == end_th:
            print("Tie!")
        else:
            print("Tim faster!")


words = [
    "racecar",
    "abba",
    "racecat",
    "dogmaiamgod",
    "tonysopranonarposynottonysopranonarposynottonysopranonarposynottonysopranonarposynottonysopranonarposynottonysopranonarposynottonysopranonarposynottonysopranonarposynot",
    "racecar",
]

main(words)
