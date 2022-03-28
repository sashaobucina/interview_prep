require('minitest/autorun')

class MinStack
  class Node
    attr_reader :val, :min

    def initialize(val, min:)
      @val = val
      @min = min
    end
  end

  attr_reader :items, :min

  def initialize
    @min = nil
    @items = []
  end

  def push(val)
    @min = val if min.nil? || val < min

    items << Node.new(val, min: @min)
  end

  def pop
    node = @items.pop

    if node.val == min
      @min = @items.empty? ? nil : @items.last.min
    end

    node.val
  end

  def peek
    @items[-1].val
  end
end

class MinStackTest < Minitest::Test
  def setup
    @stack = MinStack.new
  end

  def test_min_empty
    assert_nil(@stack.min)
  end

  def test_push_empty
    @stack.push(1)

    assert_equal(1, @stack.min)
  end

  def test_push_multiple
    @stack.push(5)
    @stack.push(1)
    @stack.push(2)

    assert_equal(1, @stack.min)
  end

  def test_push_min
    @stack.push(2)
    assert_equal(2, @stack.min)

    @stack.push(1)
    assert_equal(1, @stack.min)
  end

  def test_pop
    @stack.push(1)
    @stack.push(5)
    @stack.push(2)

    assert_equal(2, @stack.pop)
    assert_equal(5, @stack.pop)
    assert_equal(1, @stack.pop)
  end

  def test_pop_min
    @stack.push(5)
    @stack.push(2)
    @stack.push(1)

    @stack.pop
    assert_equal(2, @stack.min)

    @stack.pop
    assert_equal(5, @stack.min)
  end

  def test_peek
    @stack.push(5)
    @stack.push(2)
    @stack.push(1)

    assert_equal(1, @stack.peek)
  end
end
