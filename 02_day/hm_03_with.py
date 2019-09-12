# with open("./1.txt", "wb") as f:
#     f.write("hello flask")
#     f.write("hello flask")
#     f.write("hello flask")


class Foo(object):
    def __enter__(self):
        """进入with语句的时候被with调用"""
        print("enter called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with语句的时候被with调用"""
        print("exit called")
        print("exc_type: %s" % exc_type)
        print("exc_val: %s" % exc_val)
        print("exc_tb: %s" % exc_tb)


with Foo() as foo:
    print("hello python")
    a = 1 / 0
    print("hello end")
