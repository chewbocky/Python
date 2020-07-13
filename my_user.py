from users import Users
from admin_class import Admin

'''user_0 = Users('garrett','bock','gbock','IT')
user_1 = Users('fred','bock','fbock','Maintenance')

user_0.describe_user()
user_0.increment_login_attempts(1)
user_0.increment_login_attempts(1)
user_0.increment_login_attempts(1)
user_0.increment_login_attempts(1)
user_0.reset_login_attempts()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()'''

admin_0 = Admin('garrett','bock','gbock','office')
admin_0.describe_user()
admin_0.privilege.show_privileges()