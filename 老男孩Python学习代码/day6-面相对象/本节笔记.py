# __author__ = "Alex Li"
#
# 面向对象介绍
#
# 世界万物，皆可分类
# 世界万物，皆为对象
#
# 只要是对象， 就肯定属于某种品类
# 只要是对象，就肯定有属性
#
#
# 你是上帝
#
# 地球
#
# 山川，河流，大海，森林，
#
# 飞禽  飞， 吃虫子，下蛋，
# 布谷鸟    唱歌
# 乌鸦
#
# 几百种鸟
#
#
#
# 走兽，
#
# 狮子 森林之王
# 老虎  百兽之王
#
#
#
#
# 臭鱼烂虾，
#
# 人，思考，说话， 吃喝拉撒睡，
#
#
#
#
#
# 特性
# class
# object
#
# 封装
# 继承
# 多态
#
# 语法
#
# 调用函数  --》 执行 --》返回结果
#
# r1 = Role.__init__() return x342423
#
# r1 = Role(r1,"Alex","Police","15000")
# r1.name = "Alex"
# r1.role = "Poice"
# r1.money = 15000
# r1.buy_gun() # Role.buy_gun(r1)
#


# 属性
# 方法
# 类变量的用途? 大家共用的属性 ,节省开销
# class Person:
#     cn = "中国"
#     def __init__(self,name,age,addr,cn="china")
#         self.name = name
#         self.cn = cn
# p1 = Person(name,age ,addr)
# #
# 构造函数

#析构函数： 在实例释放、销毁的时候自动执行的，通常用于做一些收尾工作， 如关闭一些数据库连接，关闭打开的临时文件

# 私有方法，私有属性
#
# 类变量
# 实例变量


# 封装

#继承
#py2 经典类是按深度优先来继承的，新式类是按广度优先来继承的
#py3 经典类和新式类都是统一按广度优先来继承的

#多态
#一种接口，多种实现

