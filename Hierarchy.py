import sys
import pandas as pd
import pandera as pa
from Employee import Employee
from Manager import Manager

def main(argv):
    employees, supervisors, tot_salary = _read_input(argv[0])
    _process_managers(employees, supervisors)
    print(_output(employees, supervisors, tot_salary))

def _read_input(filename):
    employees = {}  # associate employee IDs to Employee objects
    supervisors = {}  # associate Manager IDs
    tot_salary = 0
    # Assumption: Files will be in JSON format
    data = pd.read_json(filename)
    schema = pa.DataFrameSchema({
        "id": pa.Column(pa.Int, nullable=False),
        "first_name": pa.Column(pa.String, nullable=False),
        "manager": pa.Column(pa.Float, nullable=True),
        "salary": pa.Column(pa.Int, nullable=False)
    })
    schema.validate(data)

    for index, d in data.iterrows():
        if pd.isna(d["manager"]):
            d["manager"] = None
        employees[d["id"]] = Employee(d["id"], d["first_name"], d["manager"], d["salary"])
        if d["manager"] not in supervisors.keys():
            supervisors[d["manager"]] = [d["id"]]
        else:
            supervisors[d["manager"]].append(d["id"])
        tot_salary += d["salary"]

    return employees, supervisors, tot_salary

# DEPRECATED: parsing raw TXT
#def _old_read_input(filename):
#    employees = {}
#    supervisors = {}
#    tot_salary = 0
#    with open(filename) as data:
#        data.readline()  # process the opening bracket
#        brace = data.readline()  # check for open brace
#        while '{' in brace:  # while more employees in the file
#            e_id = data.readline()  # first entry: id
#            name = data.readline()  # second entry: name
#            manager = data.readline()  # third entry: manager
#            salary = data.readline()  # fourth entry: salary

#            e_id, name, manager, salary = _clean_entry(e_id, name, manager, salary)

#            # store data
#            employees[e_id] = Employee(e_id, name, manager, salary)
#            if manager not in supervisors.keys():
#                supervisors[manager] = [e_id]
#            else:
#                supervisors[manager].append(e_id)
#            tot_salary += salary

#            data.readline()  # consume closing bracket
#            brace = data.readline()  # collect either next opening brace or closing bracket
#        data.close()
#        return employees, supervisors, tot_salary

# DEPRECATED: for cleaning raw TXT
#def _clean_entry(e_id, name, manager, salary):
#    # clean values
#    e_id = int(e_id[e_id.index(':') + 2: len(e_id) - 2])         # extract values from {"attribute" : val,},
#    name = name[name.index(':') + 2: len(name) - 2].strip('"')   # assuming that all inputs come after a colon and a space
#    manager = manager[manager.index(':') + 2: len(manager) - 2]  # and have a comma to be truncated (except salary)
#    if manager == 'null':
#        manager = None
#    else:
#        manager = int(manager)
#    salary = int(salary[salary.index(':') + 2: len(salary) - 1])

#    return e_id, name, manager, salary

def _process_managers(employees, supervisors):
    # update employees to managers
    for e_id in employees.keys():
        if e_id in supervisors.keys():
            emp = employees[e_id]
            employees[e_id] = Manager(emp.e_id, emp.name, emp.manager, emp.salary)

    for e in employees.values():  # add appropriate employees to manager's list
        if e.manager is not None:
            employees[e.manager].employee_list.append(e)


def _output(employees, supervisors, tot_salary):
    # get only the tops of the trees (in case there are multiple); those without supervisors
    # Assumption: there is always at least one employee with no supervisor.
    # Assumption: there are no circular references.
    tops = supervisors[None]

    # output the tree, starting from the top
    output = ""
    for t in tops:
        manager = employees[t]
        output += manager.output() + "\n"

    output += "Total salary: " + str(tot_salary)
    return output


if __name__ == '__main__':
    main(sys.argv[1:])
