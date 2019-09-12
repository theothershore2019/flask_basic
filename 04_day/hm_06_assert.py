def num_div(num1, num2):
    """除法"""
    # assert断言就是判断一个函数或对象的一个方法所产生的结果是否符合你期望的那个结果。 
    # 如果表达式为真，断言成功，程序继续执行，如果表达式为假会发生异常AssertionError，终止程序的执行
    assert isinstance(num1, int)
    assert isinstance(num2, int)
    assert num2 != 0

    print(num1 / num2)


if __name__ == "__main__":
    num_div(100, 50)
    num_div("a", 50)

