class Employee:

    __slots__ = 'e_id', 'name', 'manager', 'salary'

    def __init__(self, e_id, name, manager, salary):
        self.e_id = e_id
        self.name = name
        self.manager = manager
        self.salary = salary

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        if (self.e_id == other.e_id and
                self.name == other.name and
                self.manager == other.manager and
                self.salary == other.salary):
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def output(self, depth=0):
        return '\t' * depth + str(self) + "\n"
