require('minitest/autorun')
require_relative('deque')

def sentences_similar?(sentence1, sentence2)
  deque1 = Deque.new(items: sentence1.split)
  deque2 = Deque.new(items: sentence2.split)

  while deque1.present? && deque2.present?
    word1 = deque1.pop_left
    word2 = deque2.pop_left

    next unless word1 != word2

    deque1.push_left(word1)
    deque2.push_left(word2)

    break
  end

  return true if deque1.empty? || deque2.empty?

  while deque1.present? && deque2.present?
    word1 = deque1.pop
    word2 = deque2.pop

    return false if word1 != word2
  end

  true
end

# rubocop:disable Style/Documentation(RuboCop)
class SentenceSimilarityTest < Minitest::Test
  def test_sentence_similarity1
    sentence1 = 'My name is Haley'
    sentence2 = 'My Haley'

    assert(sentences_similar?(sentence1, sentence2))
  end

  def test_sentence_similarity2
    sentence1 = 'A lot of words'
    sentence2 = 'of'

    refute(sentences_similar?(sentence1, sentence2))
  end

  def test_sentence_similarity3
    sentence1 = 'Eating right now'
    sentence2 = 'Eating'

    assert(sentences_similar?(sentence1, sentence2))
  end
end
# rubocop:enable Style/Documentation(RuboCop)
