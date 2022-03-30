require('minitest/autorun')

class Trie
  class Node
    attr_reader :nodes
    attr_accessor :word

    def initialize(word = nil)
      @word = word
      @nodes = {}
    end

    def word?
      !@word.nil?
    end

    def leaf?
      nodes.empty?
    end
  end

  def initialize
    @head = Node.new
  end

  def add(word)
    curr = @head
    word.each_char do |ch|
      curr.nodes[ch] = Node.new unless curr.nodes.key?(ch)

      curr = curr.nodes[ch]
    end

    curr.word = word
  end

  def remove(word)
    curr = @head
    stack = [[nil, @head]]

    word.each_char do |ch|
      return nil unless curr.nodes.key?(ch)

      curr = curr.nodes[ch]
      stack << [ch, curr]
    end

    return unless curr.word?

    remove_chain(stack)
  end

  def startswith?(prefix)
    curr = @head
    prefix.each_char do |ch|
      return false unless curr.nodes.key?(ch)

      curr = curr.nodes[ch]
    end

    true
  end

  def depth(word)
    curr = @head
    word.each_char do |ch|
      return -1 unless curr.nodes.key?(ch)

      curr = curr.nodes[ch]
    end

    word.size
  end

  def empty?
    @head.nodes.empty?
  end

  private

  def remove_chain(stack)
    ch, node = stack.pop
    parent_ch, parent = stack.pop

    unless node.leaf?
      node.word = nil
      return
    end

    parent.nodes.delete(ch)

    until stack.empty?
      node = parent
      ch = parent_ch
      parent_ch, parent = stack.pop

      break if node.word?
      break unless node.leaf?

      parent.nodes.delete(ch)
    end
  end
end

class TrieTest < Minitest::Test
  def setup
    @trie = Trie.new
  end

  def test_add
    @trie.add('cherry')

    assert_equal(6, @trie.depth('cherry'))
  end

  def test_startswith
    @trie.add('looper')

    assert(@trie.startswith?('loop'))
    refute(@trie.startswith?('leep'))
    assert(@trie.startswith?('looper'))
  end

  def test_remove_leaf
    @trie.add('on')
    @trie.add('leep')
    @trie.add('loop')
    @trie.add('looper')

    @trie.remove('looper')

    refute(@trie.startswith?('looper'))
  end

  def test_remove_non_leaf_word
    @trie.add('on')
    @trie.add('leep')
    @trie.add('loop')
    @trie.add('looper')

    @trie.remove('loop')

    assert(@trie.startswith?('loop'))
  end

  def test_remove_single_word
    @trie.add('loop')

    @trie.remove('loop')

    assert_predicate(@trie, :empty?)
  end

  def test_remove_entire_branch
    @trie.add('loop')
    @trie.add('other')

    @trie.remove('loop')

    refute(@trie.startswith?('loop'))
    assert(@trie.startswith?('other'))
  end
end
