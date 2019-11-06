class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Restaurant\'s name is: ' + self.restaurant_name + '\nCuisine_type is: ' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open!')

    def set_number_served(self, number_served):
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print('You can`t decrease number of people been served')

    def increment_number_served(self, inc_number_served):
        if inc_number_served > 0:
            self.number_served += inc_number_served
        else:
            print('You can`t decrease number of people been served')

    def get_number_served(self):
        print('Restaurant has served ' + str(self.number_served) + ' peoples!')


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)     # 父类初始化必须显式调用
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)


class Teacher:
    """定义一个老师类"""
    profession = 'education'        # 类的属性

    # 先__new__,再__init__;前者是有默认实现的
    def __init__(self, name):
        self.__name = name            # 实例的属性

    def show_info(self):
        return 'This is a teacher'


print(Teacher.__doc__)
print(Teacher.profession)
print(Teacher.show_info)        # 类的方法返回函数的地址：<function Teacher.show_info at 0x000002452CEA2950>
# print(Teacher.show_info())      # 报错，不能用实例的方法

wang = Teacher('Wang')
# print(wang.name)
print(wang.__name)          # 对私有属性有保护，会说没有该属性，外界被屏蔽
print(wang._Teacher__name)  # 绕过对私有属性的保护

my_restaurant = Restaurant('qianye', 'yun')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(20)
my_restaurant.get_number_served()
my_restaurant.increment_number_served(10)
my_restaurant.get_number_served()

flavors = ['Apple', 'Orange']
my_icecreamr = IceCreamStand('qianye', 'yun', *flavors)
my_icecreamr.show_flavors()