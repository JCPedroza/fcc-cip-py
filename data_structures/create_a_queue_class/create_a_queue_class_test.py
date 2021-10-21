from create_a_queue_class import Queue


def assert_queue_state(queue, expected_list):
    assert queue.list == expected_list
    assert len(queue) == len(expected_list)
    assert queue.size() == len(expected_list)
    assert queue.is_empty() == (len(expected_list) == 0)
    assert queue.front() == (expected_list[0] if expected_list else None)


def test_basic_queue_operations():
    queue = Queue()
    assert_queue_state(queue, [])

    queue.enqueue(0)
    assert_queue_state(queue, [0])

    queue.enqueue(1).enqueue(2).enqueue(3)
    assert queue.dequeue() == 0
    assert queue.dequeue() == 1
    assert_queue_state(queue, [2, 3])

    queue.clear()
    assert_queue_state(queue, [])
