from unittest import TestCase
from Employee import Employee

# Super Extra Credit: Unit Testing

class TestEmployee(TestCase):
    def test_output(self):
        m = Employee(1, "Bob", None, 100000)
        correct = "Bob\n"
        self.assertEqual(m.output(), correct)
