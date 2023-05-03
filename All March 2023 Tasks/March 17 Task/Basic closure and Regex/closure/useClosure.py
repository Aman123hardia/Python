# Closures can be used to avoid global values and provide data hiding, 
# and can be an elegant solution for simple cases with one or few methods


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)


print(times3(2))
print(times5(3))

print(times5(times3(2)))