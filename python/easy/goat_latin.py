def to_goat_latin(S: str) -> str:
    """
    # 824: A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

    We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

    The rules of Goat Latin are as follows:
        - If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
        For example, the word 'apple' becomes 'applema'.

        - If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
        For example, the word "goat" becomes "oatgma".

        - Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
        For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

    Return the final sentence representing the conversion from S to Goat Latin. 
    """
    ans = []

    vowels = {"a", "e", "i", "o", "u"}
    words = S.split()

    word_idx = 1
    for word in words:
        first_letter = word[0]
        if first_letter.lower() in vowels:
            word += "ma"
        else:
            word = word[1:] + first_letter + "ma"

        word += ("a" * word_idx)
        ans.append(word)

        word_idx += 1

    return " ".join(ans)


if __name__ == "__main__":
    S = "I speak Goat Latin"
    assert to_goat_latin(S) == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

    print("Passed all tests!")
