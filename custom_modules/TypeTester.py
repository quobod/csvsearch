import types


def arg_is_a_tuple(port_start_range):
    return (
        "<class 'tuple'>" == str(type(port_start_range))
        and not port_start_range == None
    )


def arg_is_an_int(port_start_range):
    return (
        "<class 'int'>" == str(type(port_start_range)) and not port_start_range == None
    )


def arg_is_a_string(port_start_range):
    return (
        "<class 'str'>" == str(type(port_start_range)) and not port_start_range == None
    )


def arg_is_a_dict(port_start_range):
    return (
        "<class 'dict'>" == str(type(port_start_range)) and not port_start_range == None
    )


def arg_is_a_list(port_start_range):
    return (
        "<class 'list'>" == str(type(port_start_range)) and not port_start_range == None
    )


def arg_is_a_float(port_start_range):
    return (
        "<class 'float'>" == str(type(port_start_range))
        and not port_start_range == None
    )


def arg_is_a_function(arg):
    return not arg == None and isinstance(arg, types.FunctionType)


def arg_is_none(arg):
    return str(type(arg)) == "<class 'NoneType'>" or arg == None or len(arg) == 0


def arg_is_null(arg):
    return arg.empty or arg == None


def arg_is_range(arg):
    if not arg == None:
        if "-" in arg:
            arg_split = str(arg).split("-")
            sport = arg_split[0]
            eport = arg_split[1]

            if arg_is_an_int(sport) and arg_is_an_int(eport):
                if sport < eport:
                    return True
    return False
