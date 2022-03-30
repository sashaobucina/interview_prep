require 'minitest/autorun'

# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
#   - Rank is an integer starting from 1.
#   - The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
#   - Rank should be as small as possible.
#
def rank_transform(arr)
  sorted_arr = arr.sort

  i = 0
  rank = 1
  rank_map = {}
  while i < sorted_arr.length
    num = sorted_arr[i]

    while i < sorted_arr.length - 1 && sorted_arr[i] == sorted_arr[i + 1]
      rank_map[num] = rank
      i += 1
    end

    rank_map[num] = rank

    i += 1
    rank += 1
  end

  arr.map { |x| rank_map[x] }
end

class RankTransformTest < Minitest::Test
  def test_rank_transform1
    arr = [40, 10, 20, 30]

    ranked_arr = rank_transform(arr)

    assert_equal([4, 1, 2, 3], ranked_arr)
  end

  def test_rank_transform2
    arr = [100, 100, 100]

    ranked_arr = rank_transform(arr)

    assert_equal([1, 1, 1], ranked_arr)
  end

  def test_rank_transform3
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]

    ranked_arr = rank_transform(arr)

    assert_equal([5, 3, 4, 2, 8, 6, 7, 1, 3], ranked_arr)
  end

  def test_rank_transform_empty
    assert_empty(rank_transform([]))
  end
end
