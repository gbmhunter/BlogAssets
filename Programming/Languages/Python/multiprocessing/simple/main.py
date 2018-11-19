#!/usr/bin/env python3

import multiprocessing

def worker(num):
    return num*num

def main():
    pool = multiprocessing.Pool()
    results = pool.map(worker, range(10))
    pool.close()
    pool.join()
    print(f'results = {results}')
    # results = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

if __name__ == '__main__':
    main()
