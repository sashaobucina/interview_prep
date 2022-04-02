require('minitest/autorun')

class LinkedList
  class Node
    attr_accessor(:val, :next)

    def initialize(val)
      @val = val
      @next = nil
    end

    def tail?
      @next.nil?
    end

    def to_s
      tail? ? val.to_s : "#{val} -> #{@next}"
    end
  end

  class << self
    def build(vals)
      linked_list = new

      vals.each do |val|
        linked_list.append(val)
      end

      linked_list
    end
  end

  attr_reader :head, :size

  def initialize
    @head = nil
    @size = 0
  end

  def prepend(val)
    node = Node.new(val)

    temp = @head
    @head = node
    node.next = temp

    @size += 1
  end

  def append(val)
    if @head.nil?
      @head = Node.new(val)
    else
      curr = @head
      curr = curr.next until curr.next.nil?

      curr.next = Node.new(val)
    end

    @size += 1
  end

  def delete(val)
    prev = nil
    curr = @head

    until curr.nil?
      if curr.val == val
        if prev.nil?
          @head = curr.next
        else
          prev.next = curr.next
        end

        @size -= 1
      end

      prev = curr
      curr = curr.next
    end
  end

  def find(val)
    curr = @head

    until curr.nil?
      return curr if curr.val == val

      curr = curr.next
    end

    false
  end

  def to_s
    @head.to_s
  end
end

class LinkedListTest < Minitest::Test
  def setup
    @ll = LinkedList.build([1, 2, 3, 4, 5])
  end

  def test_build
    assert_equal(5, @ll.size)
  end

  def test_delete_single
    ll = LinkedList.build([1])
    ll.delete(1)

    assert_nil(ll.head)
    assert_equal(0, ll.size)
  end

  def test_delete_head
    @ll.delete(1)

    assert_equal(4, @ll.size)
    assert_equal(2, @ll.head.val)
  end

  def test_delete_end
    @ll.delete(5)

    refute(@ll.find(5))
    assert_equal(4, @ll.size)
  end

  def test_delete_middle
    @ll.delete(3)

    refute(@ll.find(3))
    assert_equal(4, @ll.size)
  end

  def test_delete_nothing
    @ll.delete(6)

    assert_equal(5, @ll.size)
  end

  def test_find
    node = @ll.find(3)

    assert_kind_of(LinkedList::Node, node)
    assert_equal(3, node.val)
  end

  def test_find_false
    refute(@ll.find(6))
  end
end
