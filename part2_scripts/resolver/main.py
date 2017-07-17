from resolver import Resolver
resolve = Resolver()
print(resolve('google.com'))
print(resolve('apple.com'))


# Note that everytime we are calling object
# we're appending it to cache, hence if we call it 
# twice with the same argument the result will be much faster


# Checking the speed with time it 

from timeit import timeit
first_time = timeit(setup="from __main__ import resolve",
                    stmt="resolve('python.org')",
                    number=1)

second_time = timeit(setup="from __main__ import resolve",
                     stmt="resolve('python.org')",
                     number=1)


print("the first time was {:f} and the second was {:f} ".format(first_time, second_time))

# Managing the cache

print(resolve.has_host("plurasight.com"))
print(resolve("plurasight.com"))
print(resolve.has_host("plurasight.com"))
resolve.clear()
print(resolve.has_host("plurasight.com"))
