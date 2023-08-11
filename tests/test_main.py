import pytest

from main import Node, LinkedList


def test_node_init():
    node = Node(5)
    assert node.val == 5
    assert node.next is None

def test_node_str():
    node = Node(5)
    assert str(node) == "5"

def test_linked_list_init():
    ll = LinkedList()
    assert ll.head is None

    node = Node(5)
    ll_with_node = LinkedList(node)
    assert ll_with_node.head == node

def test_linked_list_append():
    ll = LinkedList()
    ll.append(5)
    assert ll.head.val == 5

    ll.append(6)
    assert ll.head.next.val == 6
    assert ll.head.next.next is None

def test_linked_list_len():
    ll = LinkedList()
    assert len(ll) == 0

    ll.append(5)
    assert len(ll) == 1

    ll.append(6)
    assert len(ll) == 2

def test_linked_list_iter():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)

    values = [val for val in ll]
    assert values == [5, 6, 7]

def test_linked_list_to_list():
    ll = LinkedList()
    assert ll.to_list() == []

    ll.append(5)
    ll.append(6)
    ll.append(7)
    assert ll.to_list() == [5, 6, 7]
