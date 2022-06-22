from Employee import Employee
class Manager(Employee):

    __slots__ = 'employee_list'

    def __init__(self, e_id, name, manager, salary, e_list=None):
        super().__init__(e_id, name, manager, salary)
        if e_list is None:
            e_list = []
        self.employee_list = e_list

    # Benefits 'Extra Credit' sorting feature, as well as 'Mega Extra Credit' unit testing.
    def __eq__(self, other):
        # if all fields are equal, these are the same, else they are not
        if (self.e_id == other.e_id and
                self.name == other.name and
                self.manager == other.manager and
                self.salary == other.salary and
                self.employee_list == other.employee_list):
            return True
        else:
            return False

    # Supports tree-like output
    def output(self, depth=0):
        output = ''
        # pad all lines with the same number of tabs, relative to how many supervisors you have
        padding = '\t' * depth
        output += padding + str(self) + "\n"
        output += padding + "Employees of: " + str(self) + "\n"
        # Extra Credit: sort employees alphabetically
        for e in sorted(self.employee_list):
            # call output of member employees at increased depth for tree-like readability
            output += e.output(depth + 1)
        return output

