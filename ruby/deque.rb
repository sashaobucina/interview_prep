class Deque
  attr_reader :items

  def initialize(items: [])
    @items = items
  end

  def push(val)
    @items << val
  end

  def push_left(val)
    @items.unshift(val)
  end

  def pop
    @items.pop
  end

  def pop_left
    @items.shift
  end

  def empty?
    @items.empty?
  end

  def present?
    !empty?
  end
end
