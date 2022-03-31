require('minitest/autorun')

# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the
# character at the ith position moves to indices[i] in the shuffled string.
#
# Return the shuffled string.
#
def restore_string(str, indices)
  arr = Array.new(str.size)

  indices.zip(str.chars).each do |(idx, ch)|
    arr[idx] = ch
  end

  arr.join
end

class ShuffleStringTest < Minitest::Test
  def test_restore_string1
    str = 'codeleet'
    indices = [4, 5, 6, 7, 0, 2, 1, 3]

    assert_equal('leetcode', restore_string(str, indices))
  end

  def test_restore_string2
    str = 'abc'
    indices = [0, 1, 2]

    assert_equal('abc', restore_string(str, indices))
  end

  def test_restore_string3
    str = 'aiohn'
    indices = [3, 1, 4, 2, 0]

    assert_equal('nihao', restore_string(str, indices))
  end
end
