from unittest import TestCase
import pandera
import Hierarchy
from Employee import Employee
from Manager import Manager

# Super Extra Credit: Unit Testing

class Test(TestCase):

    def test_read_input(self):
        # standard case
        test = Hierarchy._read_input('test.json')
        correct = ({1: Employee(1, "Bob", None, 10000)}, {None: [1]}, 10000)
        self.assertEqual(test[0], correct[0])
        self.assertEqual(test[1], correct[1])
        self.assertEqual(test[2], correct[2])

        # test empty data
        with self.assertRaises(pandera.errors.SchemaError) as err:
            Hierarchy._read_input('empty.json')

        # test invalid data
        with self.assertRaises(pandera.errors.SchemaError) as err:
            Hierarchy._read_input('invalid.json')

# DEPRECATED: used for testing TXT processing
#    def test_clean_entry(self):
#        data = ('"id": 1,\n',
#                '"first_name": Bob,\n',
#                '"manager": null,\n',
#                '"salary": 10000\n')
#        test = Hierarchy._clean_entry(data[0], data[1], data[2], data[3])
#        correct = (1, 'Bob', None, 10000)
#        self.assertEqual(test[0], correct[0])
#        self.assertEqual(test[1], correct[1])
#        self.assertEqual(test[2], correct[2])
#        self.assertEqual(test[3], correct[3])

    def test_process_managers(self):
        # simple case
        test_emp = {1: Employee(1, "Bob", None, 10000)}
        test_sup = {None: [1]}
        correct_emp = {1: Employee(1, "Bob", None, 10000)}
        Hierarchy._process_managers(test_emp, test_sup)
        self.assertEqual(test_emp, correct_emp)

        # standard case (1 manager)
        test_emp = {1: Employee(1, "Bob", None, 10000),
                    2: Employee(2, "Nate", 1, 9000),
                    3: Employee(3, "Bri", 1, 9000)}
        test_sup = {None: [1], 1: [2, 3]}
        correct_emp = {1: Manager(1, "Bob", None, 10000, [Employee(2, "Nate", 1, 9000), Employee(3, "Bri", 1, 9000)]),
                       2: Employee(2, "Nate", 1, 9000),
                       3: Employee(3, "Bri", 1, 9000)}
        Hierarchy._process_managers(test_emp, test_sup)
        self.assertEqual(test_emp, correct_emp)

        # complex case (managers with managers)
        test_emp = {1: Employee(1, "Bob", None, 10000),
                    2: Employee(2, "Nate", 1, 9000),
                    3: Employee(3, "Bri", 2, 9000)}
        test_sup = {None: [1], 1: [2], 2: [3]}
        correct_emp = {1: Manager(1, "Bob", None, 10000, [Manager(2, "Nate", 1, 9000, [Employee(3, "Bri", 2, 9000)])]),
                       2: Manager(2, "Nate", 1, 9000, [Employee(3, "Bri", 2, 9000)]),
                       3: Employee(3, "Bri", 2, 9000)}
        Hierarchy._process_managers(test_emp, test_sup)
        self.assertEqual(test_emp, correct_emp)

    def test_output(self):
        # simple case
        data = ({1: Employee(1, "Bob", None, 10000)},
                {None: [1]},
                10000)
        test = Hierarchy._output(data[0], data[1], data[2])
        correct = "Bob\n\nTotal salary: 10000"
        self.assertEqual(test, correct)

        # complex case (managers with managers)
        data = ({1: Manager(1, "Bob", None, 10000, [Manager(2, "Nate", 1, 9000, [Employee(3, "Bri", 2, 9000)])]),
                 2: Manager(2, "Nate", 1, 9000, [Employee(3, "Bri", 2, 9000)]),
                 3: Employee(3, "Bri", 2, 9000)},
                {None: [1], 1: [2], 2: [3]},
                28000)
        test = Hierarchy._output(data[0], data[1], data[2])
        correct = "Bob\nEmployees of: Bob\n\tNate\n\tEmployees of: Nate\n\t\tBri\n\nTotal salary: 28000"
        self.assertEqual(test, correct)
