__author__ = 'tcato'


def main():
    my_list = []
    # Get a list of integers
    try:
        my_list = [int(i) for i in input("Enter a list of integers: ").split()]
        min_value, max_value, average_value = list_info(my_list)
        print(len(my_list), "elements:", my_list)
        print("min=", min_value, "max=", max_value, "average=", average_value)

    except ValueError:
        if len(my_list) == 0:
            print("You entered nothing")
        else:
            print("You entered something that was not an integer")


def list_info(arg):
    arg.sort()
    return min(arg), max(arg), sum(arg) / len(arg)

main()
