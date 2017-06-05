# Singleton/SingletonPattern.py

class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)
		
class OnlyMe:
    pass

x = OnlyMe()

y = OnlyOne('eggs')

z = OnlyOne('spam')
print('---z---')
print(z)
print('---x---')
print(x)
print('---y---')
print(y)
print('---x---')
print(x)
print('---y---')
print(y)
print('---z---')
print(z)

print("------------------------------------------------------------------")

class Singleton2(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton2, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    s1 = Singleton2()
    s2 = Singleton2()
    print(s1)
    print(s2)
    if (id(s1) == id(s2)):
        print("Same")
    else:
        print("Different")
		

print("------------------------------------------------------------------")

class Singleton3(object):
   def __new__(cls):
       if not hasattr(cls, 'instance'):
           cls.instance = super(Singleton3, cls).__new__(cls)
       return cls.instance

singleton = Singleton3()
another_singleton = Singleton3()
print(singleton)
print(another_singleton)
print(singleton is another_singleton)
