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
    dl = DLinkedList(None)

    dl.append("node1")
    dl.append("node2")
    dl.append("node3")

    assert dl.head.data == "node1"
    assert dl.head.next_node.data == "node2"
    assert dl.head.next_node.prev_node.data == "node1"
    assert dl.head.next_node.next_node.data == "node3"