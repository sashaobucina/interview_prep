require('minitest/autorun')

def num_odd_subarrays(arr)
  odd = 0
  even = 0
  total = 0

  curr_sum = 0
  arr.each do |num|
    curr_sum += num

    if curr_sum.odd?
      odd += 1
      total += even + 1
    else
      even += 1
      total += odd
    end
  end

  total % ((10**9) + 7)
end

class OddSumSubarrayTest < Minitest::Test
  def test_odd_sum_subarrays1
    arr = [1, 3, 5]

    assert_equal(4, num_odd_subarrays(arr))
  end

  def test_odd_sum_subarrays2
    arr = [2, 4, 6]

    assert_equal(0, num_odd_subarrays(arr))
  end

  def test_odd_sum_subarrays3
    arr = [1, 2, 3, 4, 5, 6, 7]

    assert_equal(16, num_odd_subarrays(arr))
  end
end
