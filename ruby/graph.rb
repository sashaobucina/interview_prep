require('set')
require('minitest/autorun')

class Graph
  class << self
    def build(connections)
      graph = Graph.new

      connections.each do |(src, dest)|
        graph.add_edge(src, dest)
      end

      graph
    end
  end

  attr_reader :adjacency_list

  def initialize
    @adjacency_list = Hash.new(Set.new)
  end

  def add_vertex(val)
    @adjacency_list[val] = Set.new unless include?(val)
  end

  def add_edge(src, dest)
    add_vertex(src) unless include?(src)
    add_vertex(dest) unless include?(dest)

    @adjacency_list[src].add(dest)
    @adjacency_list[dest].add(src)
  end

  def remove_vertex(val)
    @adjacency_list.delete(val) if include?(val)

    @adjacency_list.each_value do |neighbors|
      neighbors.delete(val) if neighbors.include?(val)
    end
  end

  def remove_edge(src, dest)
    @adjacency_list[src].delete(dest)
    @adjacency_list[dest].delete(src)
  end

  def neighbors(val)
    @adjacency_list[val]
  end

  def include?(val)
    @adjacency_list.key?(val)
  end
end

class GraphTest < Minitest::Test
  def setup
    @graph = Graph.new
  end

  def test_add_vertex
    @graph.add_vertex(1)

    assert(@graph.include?(1))
    assert_empty(@graph.neighbors(1))
  end

  def test_add_edge
    @graph.add_edge(1, 2)

    assert_includes(@graph.neighbors(1), 2)
    assert_includes(@graph.neighbors(2), 1)
  end

  def test_remove_vertex
    @graph.add_edge(1, 2)
    @graph.add_edge(1, 3)
    @graph.add_edge(2, 3)

    @graph.remove_vertex(1)

    refute(@graph.include?(1))
    assert(@graph.include?(2))
    assert(@graph.include?(3))

    assert_includes(@graph.neighbors(2), 3)
    assert_includes(@graph.neighbors(3), 2)
  end

  def test_remove_edge
    graph = Graph.build([[1, 2], [1, 3], [2, 3]])

    graph.remove_edge(1, 2)

    assert(graph.include?(1))
    assert(graph.include?(2))
    assert(graph.include?(3))

    refute_includes(graph.neighbors(1), 2)
    refute_includes(graph.neighbors(2), 1)

    assert_includes(graph.neighbors(1), 3)
    assert_includes(graph.neighbors(2), 3)
  end
end
