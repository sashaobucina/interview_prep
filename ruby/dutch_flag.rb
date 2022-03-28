require('minitest/autorun')

def dutch_flag(arr)
  counts = [0, 0, 0]
  arr.each { |num| counts[num] += 1 }

  i = 0
  counts.each_with_index do |count, val|
    (0...count).each do
      arr[i] = val
      i += 1
    end
  end
end

class DutchFlagTest < Minitest::Test
  def test_dutch_flag_sort
    arr = [2, 0, 1, 0, 2]

    dutch_flag(arr)

    assert_equal([0, 0, 1, 2, 2], arr)
  end
end
