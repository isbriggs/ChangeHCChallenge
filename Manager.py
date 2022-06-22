from Employee import Employee
class Manager(Employee):

    __slots__ = 'employee_list'

    def __init__(self, e_id, name, manager, salary, e_list=None):
        super().__init__(e_id, name, manager, salary)
        if e_list is None:
            e_list = []
        self.employee_list = e_list

    def __eq__(self, other):
        if (self.e_id == other.e_id and
                self.name == other.name and
                self.manager == other.manager and
                self.salary == other.salary and
                self.employee_list == other.employee_list):
            return True
        else:
            return False

    def output(self, depth=0):
        output = ''
        padding = '\t' * depth
        output += padding + str(self) + "\n"
        output += padding + "Employees of: " + str(self) + "\n"
        for e in sorted(self.employee_list):
            output += e.output(depth + 1)
        return output

