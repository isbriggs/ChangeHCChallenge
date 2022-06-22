class Employee:
    # use slots for memory efficiency
    __slots__ = 'e_id', 'name', 'manager', 'salary'

    def __init__(self, e_id, name, manager, salary):
        self.e_id = e_id
        self.name = name
        self.manager = manager
        self.salary = salary

    # Supports 'Extra Credit' sorting
    def __lt__(self, other):
        return self.name < other.name

    # Supports 'Extra Credit' sorting and 'Mega Extra Credit' Unit Testing
    def __eq__(self, other):
        if (self.e_id == other.e_id and
                self.name == other.name and
                self.manager == other.manager and
                self.salary == other.salary):
            return True
        else:
            return False

    # Mostly for debugging, and supports output()
    def __str__(self):
        return self.name

    # Support for tree-like output
    def output(self, depth=0):
        # pad line with a number of tabs relative to how many supervisors you have
        return '\t' * depth + str(self) + "\n"
