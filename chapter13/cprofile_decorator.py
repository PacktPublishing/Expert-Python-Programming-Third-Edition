import time
import tempfile
import cProfile
import pstats


def profile(column='time', list=3):
    def parametrized_decorator(function):
        def decorated(*args, **kw):
            s = tempfile.mktemp()

            profiler = cProfile.Profile()
            profiler.runcall(function, *args, **kw)
            profiler.dump_stats(s)

            p = pstats.Stats(s)
            print("=" * 5, f"{function.__name__}() profile", "=" * 5)
            p.sort_stats(column).print_stats(list)
        return decorated

    return parametrized_decorator


def medium():
    time.sleep(0.01)


@profile('time')
def heavy():
    for i in range(100):
        medium()
        medium()
    time.sleep(2)


@profile('time')
def main():
    for i in range(2):
        heavy()


if __name__ == '__main__':
    main()


"""
$ python3 cprofile_decorator.py
===== heavy() profile =====
Wed Apr 10 03:08:18 2019    /var/folders/jy/wy13kx0s7sb1dx2rfsqdvzdw0000gq/T/tmpwh6lb0y1

         603 function calls in 4.462 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      301    4.456    0.015    4.456    0.015 {built-in method time.sleep}
      200    0.002    0.000    2.327    0.012 cprofile_decorator.py:25(medium)
        1    0.002    0.002    4.462    4.462 cprofile_decorator.py:33(heavy)
      100    0.001    0.000    0.129    0.001 cprofile_decorator.py:29(light)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


===== heavy() profile =====
Wed Apr 10 03:08:23 2019    /var/folders/jy/wy13kx0s7sb1dx2rfsqdvzdw0000gq/T/tmpsp6h0mb5

         603 function calls in 4.430 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      301    4.425    0.015    4.425    0.015 {built-in method time.sleep}
        1    0.002    0.002    4.430    4.430 cprofile_decorator.py:33(heavy)
      200    0.002    0.000    2.295    0.011 cprofile_decorator.py:25(medium)
      100    0.001    0.000    0.129    0.001 cprofile_decorator.py:29(light)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


===== main() profile =====
Wed Apr 10 03:08:23 2019    /var/folders/jy/wy13kx0s7sb1dx2rfsqdvzdw0000gq/T/tmpenh1xtz7

         64 function calls in 8.896 seconds

   Ordered by: internal time
   List reduced from 27 to 5 due to restriction <5>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    8.896    8.896    8.896    8.896 {method 'enable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method posix.lstat}
        8    0.000    0.000    0.000    0.000 /usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/random.py:224(_randbelow)
        1    0.000    0.000    8.896    8.896 cprofile_decorator.py:42(main)
        8    0.000    0.000    0.000    0.000 /usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/random.py:256(choice)

"""
