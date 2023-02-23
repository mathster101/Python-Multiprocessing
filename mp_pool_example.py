import multiprocessing as mp


def bad_fib(elem_num):
    if elem_num <= 1:
        return 1
    else:
        return bad_fib(elem_num - 1) + bad_fib(elem_num - 2)
    


if __name__ == '__main__':

    vals = [40] * 12
    with mp.Pool(processes = 16) as pool:
        result =  pool.map(bad_fib,vals)
        print(result)