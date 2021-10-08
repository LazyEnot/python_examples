NUMBERS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

NUMBERS_1 = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

DOZEN_NAMES = {
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

ERROR_MESSAGE = [
    "Your input is not supported,",
    "please provide integer from",
    "0 to 999999"
]


def number_to_english(n: int) -> str:
    if isinstance(n, int) and 0 <= n <= 999_999:
        if n == 0:
            return "zero"
        else:
            result = []
            thousands = n // 1_000
            hundreds = n % 1_000

            if thousands:
                result.append(get_text_from_hundreds(thousands))
                result.append("thousand")

            if hundreds:
                result.append(get_text_from_hundreds(hundreds))

            return " ".join(i for i in result)
    else:
        return " ".join(i for i in ERROR_MESSAGE)


def get_text_from_hundreds(n: int) -> str:
    hundreds = n // 100
    dozens = n % 100
    result = []

    if hundreds:
        result.append(NUMBERS[hundreds])
        result.append("hundred")

    if dozens in NUMBERS_1.keys():
        result.append(NUMBERS_1[dozens])
    elif dozens:
        a = dozens // 10
        b = dozens % 10

        if a:
            result.append(DOZEN_NAMES[a])

        if b:
            result.append(NUMBERS[b])

    return " ".join([i for i in result])


if __name__ == "__main__":
    import sys
    try:
        print(number_to_english(int(sys.argv[1])))
    except ValueError:
        print(" ".join(i for i in ERROR_MESSAGE))
