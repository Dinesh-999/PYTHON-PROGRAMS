# cacheing the program
# without @cache or @lru_cache(maxsize=10), it might take seconds to minutes to run this program
# with @cache or @lru_cache(maxsize=10), it will run within nano seconds
# cache is used to run program faster

from functools import cache, lru_cache

# @cache
@lru_cache(maxsize=10)  # you can use maxsize with ur number
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))
