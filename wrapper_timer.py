import time


# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         print('start time', start)
#         target = func(*args)
#         end = time.time()
#         print('end time', end)
#         print('timer.Function execution time in seconds:', round(end - start, 6))
#         print('timer.Function executed')
#
#     return wrapper


def add_to_file(func):
    def wrapper():
        log_file = open(r"C:\\Users\OGornovych\Downloads\log_test.txt", 'w')
        result = func()
        for i in result:
            print(i, file=log_file)
        print(f'Data has been logged to the file {log_file}')

    return wrapper()


@add_to_file
# @timer
def test(n):
    l = []
    for i in range(n):
        if i % 100 == 0 and i % 5 == 0:
            l.append(i)
    print('function.Executed')
    return l


n = int(input("put num"))
demo = test(n)