from create_a_stack_class import Stack


def assert_stack_state(stack, expected_list):
    assert stack.list == expected_list
    assert stack.is_empty() == (not expected_list)
    assert len(stack) == len(expected_list)
    assert stack.size() == len(expected_list)
    assert stack.peek() == (expected_list[-1] if expected_list else None)


def test_basic_stack_operations():
    stack = Stack()
    assert_stack_state(stack, [])
    assert stack.pop() is None

    stack.push(0)
    assert_stack_state(stack, [0])

    stack.push(1).push(2).push(3)
    assert_stack_state(stack, [0, 1, 2, 3])

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert_stack_state(stack, [0, 1])

    stack.clear()
    assert_stack_state(stack, [])
