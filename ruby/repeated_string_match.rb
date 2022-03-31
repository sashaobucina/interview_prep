require('minitest/autorun')

def repeated_string_match(a, b)
  k = (b.size / a.size) + 2

  (0..k).each do |i|
    repeated_a = a * i

    return i if repeated_a.include?(b)
  end

  -1
end

class RepeatedStringMatchTest < Minitest::Test
  def test_repeated_string_match1
    a = 'abcd'
    b = 'cdabcda'

    assert_equal(3, repeated_string_match(a, b))
  end

  def test_repeated_string_match2
    a = 'a'
    b = 'aaaa'

    assert_equal(4, repeated_string_match(a, b))
  end

  def test_repeated_string_match3
    a = 'aaaaaaaaaaaaaaaaab'
    b = 'ba'

    assert_equal(2, repeated_string_match(a, b))
  end

  def test_repeated_string_match4
    a = 'abcd'
    b = 'cdabcdae'

    assert_equal(-1, repeated_string_match(a, b))
  end

  def test_repeated_string_match5
    a = 'abaabaa'
    b = 'abaababaab'

    assert_equal(-1, repeated_string_match(a, b))
  end
end
