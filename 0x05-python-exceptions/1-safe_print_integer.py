afe_print_integer(value):
    try:
        print('{:d}'.format(value))
    except (Exception):
        return (False)
    return True
