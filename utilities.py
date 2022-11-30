def print_incorrect_command_statement(
        number_arguments_required: int,
        number_arguments_provided: int) -> None:
    """ print statement saying why database command not executed

    :param number_arguments_required: number of arguments database command expects
    :param number_arguments_provided: number of arguments given w/ command
    """
    print(f'COMMAND NOT EXECUTED: REQUIRES {number_arguments_required} ARGUMENT(S), '
          f'{number_arguments_provided} ARGUMENTS(S) GIVEN')
