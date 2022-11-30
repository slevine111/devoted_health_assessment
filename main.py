from database_constructor import DatabaseConstructor
from utilities import print_incorrect_command_statement
import sys

list_databases = [DatabaseConstructor()]
for line in sys.stdin:
    line_stripped = line.strip()

    # end program if command == 'END'
    if line_stripped == 'END':
        break

    # operations to perform on list of databases if command relates to transaction
    if line_stripped == 'BEGIN':
        list_databases.append(
            DatabaseConstructor(
                list_databases[-1].data.copy(),
                list_databases[-1].count_by_value.copy()
            )
        )
        continue
    elif line_stripped == 'ROLLBACK':
        if len(list_databases) == 1:
            print('TRANSACTION NOT FOUND')
        else:
            list_databases = list_databases[0:-1]
        continue
    elif line_stripped == 'COMMIT':
        list_databases = [list_databases[-1]]
        continue

    # commands to perform on current database state
    line_split = line_stripped.split()
    db = list_databases[-1]
    number_command_arguments = len(line_split) - 1
    if line_split[0] == 'SET':
        if number_command_arguments != 2:
            print_incorrect_command_statement(2, number_command_arguments)
            continue
        db.set(line_split[1], line_split[2])
    elif line_split[0] == 'GET':
        if number_command_arguments != 1:
            print_incorrect_command_statement(1, number_command_arguments)
            continue
        db.get(line_split[1])
    elif line_split[0] == 'DELETE':
        if number_command_arguments != 1:
            print_incorrect_command_statement(1, number_command_arguments)
            continue
        db.delete(line_split[1])
    elif line_split[0] == 'COUNT':
        if number_command_arguments != 1:
            print_incorrect_command_statement(1, number_command_arguments)
            continue
        db.count(line_split[1])
    else:
        print('UNKNOWN COMMAND')
    list_databases[-1] = db



