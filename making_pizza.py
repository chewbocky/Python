import pizza_def
pizza_def.make_pizza(16, 'mushrooms')
pizza_def.make_pizza(12, 'pepperoni','green peppers','extra cheese')

from pizza_def import make_pizza
make_pizza(16, 'mushrooms')
make_pizza(12, 'pepperoni','green peppers','extra cheese')

from pizza_def import make_pizza as mp 
mp(16, 'mushrooms')
mp(12, 'pepperoni','green peppers','extra cheese')

import pizza_def as p 
p.make_pizza(16, 'mushrooms')
p.make_pizza(12, 'pepperoni','green peppers','extra cheese')

from pizza_def import *
make_pizza(16, 'mushrooms')
make_pizza(12, 'pepperoni','green peppers','extra cheese')