from collections import deque
from unittest import TestCase


def are_sentences_similar(sentence1, sentence2):
    deque1 = deque(sentence1.split())
    deque2 = deque(sentence2.split())

    while deque1 and deque2:
        word1 = deque1.popleft()
        word2 = deque2.popleft()

        if word1 != word2:
            deque1.appendleft(word1)
            deque2.appendleft(word2)

            break

    if not deque1 or not deque2:
        return True

    while deque1 and deque2:
        word1 = deque1.pop()
        word2 = deque2.pop()

        if word1 != word2:
            return False

    return True


class SentenceSimilarityTest(TestCase):
    def test_sentence_similarity1(self):
        sentence1 = "My name is Haley"
        sentence2 = "My Haley"

        self.assertTrue(are_sentences_similar(sentence1, sentence2))

    def test_sentence_similarity2(self):
        sentence1 = "A lot of words"
        sentence2 = "of"

        self.assertFalse(are_sentences_similar(sentence1, sentence2))

    def test_sentence_similarity3(self):
        sentence1 = "Eating right now"
        sentence2 = "Eating"

        self.assertTrue(are_sentences_similar(sentence1, sentence2))
