def division(x):
    def dividend(y):
        return y/x
    return dividend

divide = division(2)
print(divide(10))