from progature.engine.structures import DLinkedList, Node


def test_nodes():
    node = Node("node")
    next_node = Node("next node")
    prev_node = Node("prev node")

    node.next_node = next_node
    node.prev_node = prev_node


    assert node.data == "node"
    assert node.next_node == next_node
    assert node.prev_node == prev_node

def test_doubly_linked_list_iniate():
    dll = DLinkedList([1, 2, 3, 4])

    print(dll)