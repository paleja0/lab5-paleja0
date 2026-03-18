# Variables globales
int_global = None
str_global = None

def set_globals(some_int, some_str):
    global int_global, str_global
    int_global = some_int
    str_global = some_str


def get_globals():
    return (int_global, str_global)

print(get_globals())
set_globals(10, "Hello")
print(get_globals())