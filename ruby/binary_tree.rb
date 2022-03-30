require('minitest/autorun')

class BinaryTree
  class Node
    attr_accessor :val, :left, :right

    def initialize(val, left: nil, right: nil)
      @val = val
      @left = left
      @right = right
    end

    def leaf?
      left.nil? && right.nil?
    end

    def inspect
      "{#{val}, left: #{left.inspect}, right: #{right.inspect}}"
    end
  end

  class << self
    def build(vals)
      return if vals.empty?

      root = Node.new(vals.first)
      queue = [root]

      i = 1
      until queue.empty?
        node = queue.shift

        next if node.nil?

        node.left = vals[i] ? Node.new(vals[i]) : nil
        queue << node.left
        i += 1

        break unless i < vals.length

        node.right = vals[i] ? Node.new(vals[i]) : nil
        queue << node.right
        i += 1
      end

      BinaryTree.new(root)
    end
  end

  attr_reader :root

  def initialize(root)
    @root = root
  end
end

class BinaryTreeTest < Minitest::Test
  def test_build
    tree = BinaryTree.build([1, 2, 3, nil])

    assert_equal(1, tree.root.val)
    assert_equal(2, tree.root.left.val)
    assert_equal(3, tree.root.right.val)

    assert_nil(tree.root.left.left)
    assert_nil(tree.root.left.right)

    assert_nil(tree.root.right.left)
    assert_nil(tree.root.right.right)
  end
end
