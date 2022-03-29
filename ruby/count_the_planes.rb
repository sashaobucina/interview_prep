require 'minitest/autorun'

# The data that we have on planes currently in the air comes in the form of a grid, modeled by a matrix array.
#
# Within that matrix, the dots (.s) represent available airspace. The Ps that are neighboring each other model one
# plane each.
#
# Given a multi-dimensional array of .s and Ps exclusively, can you find the number of planes that there are in the sky?
# Planes may only be placed horizontally or vertically. A diagonal plane like this would not count as one plane.
# Instead, there will be 3 separate planes.
#
# Constraints:
#   - Total number of elements in the matrix <= 100000
#   - The elements will consist only of . and P characters
#   - The matrix can be empty
#   - Expected time complexity : O(n * m) where n and m are number of rows and columns respectively
#   - Expected space complexity : O(1)

# rubocop:disable Metrics/MethodLength
def num_planes(sky)
  return 0 if sky.empty? || sky.first.empty?

  count = 0
  r = sky.size
  c = sky.first.size

  (0...r).each do |row|
    (0...c).each do |col|
      next if sky[row][col] == '.'

      count += 1 unless adjacent_plane?(sky, row, col)
    end
  end

  count
end
# rubocop:enable Metrics/MethodLength

def adjacent_plane?(sky, row, col)
  r = sky.size
  c = sky.first.size

  (row + 1 < r && sky[row + 1][col] == 'P') || (col + 1 < c && sky[row][col + 1] == 'P')
end

class PlaneCounter < Minitest::Test
  def test_num_planes_empty
    assert_equal(0, num_planes([]))
  end

  def test_num_planes
    sky = [
      ['.', '.', '.', 'P'],
      ['P', 'P', '.', 'P'],
      ['.', '.', '.', 'P'],
      ['.', '.', '.', 'P']
    ]

    assert_equal(2, num_planes(sky))
  end

  def test_num_planes_diagonal
    sky = [
      ['.', '.', 'P'],
      ['.', 'P', '.'],
      ['P', '.', '.']
    ]

    assert_equal(3, num_planes(sky))
  end

  def test_num_planes_adjacent
    sky = [
      ['P', 'P', '.'],
      ['P', 'P', '.'],
      ['P', '.', 'P']
    ]

    assert_equal(3, num_planes(sky))
  end
end
