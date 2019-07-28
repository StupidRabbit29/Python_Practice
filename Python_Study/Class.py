class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Restaurant\'s name is: ' + self.restaurant_name + '\nCuisine_type is: ' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open!')

    def set_number_served(self, number_served):
        if(number_served >= self.number_served):
            self.number_served = number_served
        else:
            print('You can`t decrease number of people been served')

    def increment_number_served(self, inc_number_served):
        if(inc_number_served > 0):
            self.number_served += inc_number_served
        else:
            print('You can`t decrease number of people been served')

    def get_number_served(self):
        print('Restaurant has served ' + str(self.number_served) + ' peoples!')


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)


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