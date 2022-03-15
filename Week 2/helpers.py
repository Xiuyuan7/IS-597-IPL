

def make_connection(k, p):
    print("Testing credentials.")
    if k == 'abc' and p == '***':
        return True
    else:
        return False


def load_data(is_connection_ok):
    if is_connection_ok:
        print("Loading data!")
        return True
    else:
        print("Connection failure, shutting down.")
        return False


def start(k, p):
    print("Beginning attempt to log in and load data.")
    return load_data(make_connection(k, p))


# start('abc', '***')
# print()
# start('fhg', '***')
# print()
# start('abc', 'hfs')
