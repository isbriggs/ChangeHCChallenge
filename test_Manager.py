from unittest import TestCase
from Employee import Employee
from Manager import Manager

# Super Extra Credit: Unit Testing

class TestManager(TestCase):
    def test_output(self):
        m = Manager(1, "Bob", None, 100000, [Employee(2, "Alice", 1, 10000), Employee(3, "Charlie", 1, 10000)])
        correct = "Bob\nEmployees of: Bob\n\tAlice\n\tCharlie\n"
        self.assertEqual(m.output(), correct)
