# def handle_name(fn, name):
#     print("Handle name")
#     fn(name)

# handle_name(lambda name: print(name), "Avner" )

say_hi = lambda name: f"hi {name}"
# print(say_hi('enosh'))

say_hi_my_age_is = lambda name, age: f"hi my name is {name}\nmy age is {age}"
# print(say_hi_my_age_is("itay", 42))


def print_it(args):
    print(args)

def do_some_with_name(fn):
    return lambda name: fn(name)

# print_name = do_some_with_name(print_it)
# print_name("Shalom")

print_name = do_some_with_name(lambda name: print(name))
# print_name("Yanay")

def increase_list(li):
    for index, e in enumerate(li):
        li[index] = e + 1
    return li

# print(increase_list([1,2,3]))

def increase(element):
    return element + 1

def hi_enosh(current):
    return f"hi enosh {current}"


my_list = [1,2,3,45,6,7,8,898098,0]
my_weird_list = list(map(lambda x: f"${x} great number", my_list))

# print(my_weird_list)



increased = list(map(increase, [1,2,3]))
# print(increased)

# increased = list(map(lambda x: x+1, [1,3,5]))
# print(increased)

def filter_list(fn, li):
    filtered_list = []
    for e in li:
        if fn(e):
            filtered_list.append(e)
    return filtered_list

def is_even(arg):
    return arg % 2 == 0

list_filter = filter_list(is_even, [1,2,3,4,5,6,7,8])
print(list_filter)

# list_filter = filter_list(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8])
# print(list_filter)

# list_filter = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8]))
# print(list_filter)

