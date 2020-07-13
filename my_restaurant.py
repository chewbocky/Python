from restaurant import *

restaurant_info_0 = Restaurant('Olive Garden','Itilan')
restaurant_info_1 = Restaurant('Chipolite','Mexican')
restaurant_info_2 = Restaurant('Whataburger','Fast Food')

restaurant_info_0.describe_restaurant()
restaurant_info_0.increment_number_served(500)
restaurant_info_0.open_restaurant()
restaurant_info_0.set_numbered_served()

restaurant_info_1.describe_restaurant()
restaurant_info_1.increment_number_served(150)
restaurant_info_1.open_restaurant()
restaurant_info_1.set_numbered_served()

restaurant_info_2.describe_restaurant()
restaurant_info_2.increment_number_served(200)
restaurant_info_2.open_restaurant()
restaurant_info_2.set_numbered_served()

restaurant_info_3 = IceCreamStand('Basken Robins','IceCream')
restaurant_info_3.describe_restaurant()
restaurant_info_3.get_flavors()