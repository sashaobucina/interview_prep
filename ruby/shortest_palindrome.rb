require('minitest/autorun')

# Given a string, find a way to convert it to a palindrome by inserting characters in front of it. What's the shortest
# palindrome that can be returned?
#
def shortest_palindrome(str)
  # find longest palindromic prefix
  n = str.size
  rev = str.reverse

  (0...n).each do |i|
    return rev[0...i] + str if str[0...(n - i)] == rev[i...n]
  end

  ''
end

class ShortestPalindromeTest < Minitest::Test
  def test_shortest_palindrome1
    assert_equal('elbbubble', shortest_palindrome('bubble'))
  end

  def test_shortest_palindrome2
    assert_equal('aaacecaaa', shortest_palindrome('aacecaaa'))
  end

  def test_shortest_palindrome3
    assert_equal('dcbabcd', shortest_palindrome('abcd'))
  end
end
