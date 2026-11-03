def two_sum(nums, target):
    """
    Return indices of two numbers whose sum equals target.

    Time: O(n)
    Space: O(n)
    """

    seen = {}

    for index, number in enumerate(nums):
        complement = target - number

        if complement in seen:
            return [seen[complement], index]

        seen[number] = index

    return []


def is_anagram(s, t):
    """
    Return True if two strings are anagrams.

    Time: O(n)
    Space: O(n)
    """

    if len(s) != len(t):
        return False

    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts:
            return False

        counts[char] -= 1

        if counts[char] < 0:
            return False

    return True


if __name__ == "__main__":
    print("DSA PROBLEM 1 — TWO SUM")
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))

    print()

    print("DSA PROBLEM 2 — VALID ANAGRAM")
    print(is_anagram("listen", "silent"))
    print(is_anagram("hello", "world"))