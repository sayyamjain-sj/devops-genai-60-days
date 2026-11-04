def contains_duplicate(nums):
    seen = set()

    for number in nums:
        if number in seen:
            return True

        seen.add(number)

    return False


def max_profit(prices):
    minimum_price = float("inf")
    maximum_profit = 0

    for price in prices:
        if price < minimum_price:
            minimum_price = price

        profit = price - minimum_price

        if profit > maximum_profit:
            maximum_profit = profit

    return maximum_profit


if __name__ == "__main__":
    print(
        contains_duplicate(
            [1, 2, 3, 1]
        )
    )

    print(
        max_profit(
            [7, 1, 5, 3, 6, 4]
        )
    )