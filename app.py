def foo(a):  # NonCompliant
    b = 12
    if a == 1:
        return b
    return b


class MyClass(object):
    def __init__(self):
        self.message = 'Hello'
        return self  # Noncompliant

print('Welcome to SonarQube Demo Project !') 
