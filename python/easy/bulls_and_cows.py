from collections import Counter


def get_hint(secret: str, guess: str) -> str:
    """
    # 299: You are playing the following Bulls and Cows game with your friend: You write down a number 
    and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a 
    hint that indicates how many digits in said guess match your secret number exactly in both digit 
    and position (called "bulls") and how many digits match the secret number but locate in the wrong 
    position (called "cows"). Your friend will use successive guesses and hints to eventually derive 
    the secret number.

    Write a function to return a hint according to the secret number and friend's guess, use A to indicate 
    the bulls and B to indicate the cows. 

    Please note that both secret number and friend's guess may contain duplicate digits.
    """
    counter = Counter(secret)

    bulls = cows = 0
    for i, ch in enumerate(guess):
        if ch in counter:
            if ch == secret[i]:
                bulls += 1
                cows -= int(counter[ch] <= 0)
            else:
                cows += int(counter[ch] > 0)

            counter[ch] -= 1

    return f"{bulls}A{cows}B"


if __name__ == "__main__":
    assert get_hint("1807", "7810") == "1A3B"
    assert get_hint("1123", "0111") == "1A1B"

    print("Passed all tests!")
