import unittest
from hm_07_login import app
import json


class LoginTest(unittest.TestCase):
    """构造单元测试案例"""
    
    def setUp(self):
        """在执行具体的测试方法前，先被调用"""
        # 设置flask工作在测试模式下
        # app.config["TESTING"] = True
        app.testing = True

        # 创建进行web请求的客户端，使用flask提供的测试客户端进行测试
        self.client = app.test_client()

    # 测试函数要以test开头，不然不执行测试
    def test_empty_user_name_password(self):
        """测试用户名密码不完整的情况"""
        
        # 使用client客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        ret = self.client.post("/login", data={})

        # ret是视图返回的响应对象，data属性是响应体的数据
        resp = ret.data

        # 因为login视图返回的是json字符串，转化成python字典
        resp = json.loads(resp)

        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

        # 测试只传用户名
        ret = self.client.post("/login", data={"user_name": "admin"})
       
        # ret是视图返回的响应对象，data属性是响应体的数据
        resp = ret.data
       
        # 因为login视图返回的是json字符串，转化成python字典
        resp = json.loads(resp)
       
        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

        # 测试只传密码
        ret = self.client.post("/login", data={"password": "admin"})
       
        # ret是视图返回的响应对象，data属性是响应体的数据
        resp = ret.data
       
        # 因为login视图返回的是json字符串，转化成python字典
        resp = json.loads(resp)
       
        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)


    def test_wrong_user_name_password(self):
        """测试用户名或密码错误"""
        # 使用客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        ret = self.client.post("/login", data={"user_name": "itcast", "password": "itcast"})

        # respoonse.data是响应体数据
        resp = ret.data

        # 按照json解析
        resp = json.loads(resp)

        # 使用断言进行验证
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 2)


if __name__  == "__main__":
    unittest.main()

