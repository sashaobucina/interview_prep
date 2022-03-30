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

  def depth(node = @root)
    return 0 if node.nil?
    return 1 if node.leaf?

    1 + [depth(node.left), depth(node.right)].max
  end

  def complete?
    queue = [root]
    incomplete = false

    until queue.empty?
      node = queue.shift

      return false if node.right && !node.left
      return false if incomplete && (node.right || node.left)

      queue << node.left if node.left
      queue << node.right if node.right

      incomplete = (node.left.nil? || node.right.nil?)
    end

    true
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

  def test_depth_empty
    tree = BinaryTree.new(nil)

    assert_equal(0, tree.depth)
  end

  def test_depth_root
    tree = BinaryTree.build([1])

    assert_equal(1, tree.depth)
  end

  def test_depth_multiple
    tree = BinaryTree.build([1, 2, 3, 4, 5, 6, nil, 8])

    assert_equal(4, tree.depth)
  end

  def test_complete
    tree = BinaryTree.build([1, 2, 3, 4, 5, 6])

    assert_predicate(tree, :complete?)
  end

  def test_complete_full
    tree = BinaryTree.build([1, 2, 3, 4, 5, 6, 7])

    assert_predicate(tree, :complete?)
  end

  def test_complete_sparse
    tree = BinaryTree.build([1, 2, nil])

    assert_predicate(tree, :complete?)
  end

  def test_incomplete
    tree = BinaryTree.build([1, 2, 3, 4, 5, nil, 7])

    refute_predicate(tree, :complete?)
  end

  def test_incomplete2
    tree = BinaryTree.build([1, 2, 3, 5, nil, 7, 8])

    refute_predicate(tree, :complete?)
  end
end
