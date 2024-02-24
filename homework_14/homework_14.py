"""
Створіть class SiteUser() для представлення користувача в системі.
Кожен користувач має ім'я, електронну пошту та рівень доступу (admin, moderator, user).
Також користувач має лічильник кількість логінів - logcount (int)
Реалізуйте необхідні методи та атрибути, використовуючи магічні методи для поліпшення
функціональності.

Вимоги:

    Клас Користувач має мати атрибути: ім'я, електронна_пошта, рівень_доступу, кількість логінів (logcount).
    Реалізуйте методи для отримання та встановлення значень атрибутів (гетери та сетери).
    Перевизначте метод __str__, щоб при виведенні об'єкта на екран
    виводилася інформація про користувача.
    Реалізуйте метод __eq__, який дозволяє порівнювати два об'єкта за рівнем доступу.
    Реалізуйте щоб SiteUser.logcount можна було збільшувати

Приклад використання:

user1 = Користувач("John Doe", "john.doe@example.com", "user")
user2 = Користувач("Jane Smith", "jane.smith@example.com", "admin")

print(user1)
# Виведе: Користувач: John Doe, Електронна пошта: john.doe@example.com, Рівень доступу: user

# Порівняння користувачів
if user1 == user2:
    print("Користувачі однакові")
else:
    print("Користувачі різні")

Написати на це все тести


Create a SiteUser() class to represent the user in the system.
Each user has a name, email and access level (admin, moderator, user).
The user also has a counter for the number of logins - logcount (int)
Implement the necessary methods and attributes using magical methods to improve
functionality.

Requirements:

    The User class must have the following attributes: name, e-mail, access_level, number of logins (logcount).
    Implement methods to get and set attribute values (getters and setters).
    Override the __str__ method so that when the object is displayed
    information about the user was displayed.
    Implement the __eq__ method that allows you to compare two objects by access level.
    Implement that SiteUser.logcount can be incremented

Example of use:

user1 = User("John Doe", "john.doe@example.com", "user")
user2 = User("Jane Smith", "jane.smith@example.com", "admin")

print(user1)
# Outputs: User: John Doe, Email: john.doe@example.com, Access Level: user

# Comparison of users
if user1 == user2:
    print("Users are the same")
otherwise:
    print("Users are different")

Write all the tests for it
"""


class AccessLevelException(Exception):
    pass


class SiteUser:
    def __init__(self, name, email, access_level):
        self._name = name
        self._email = email
        self._access_level = access_level
        self._logcount = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, value):
        if value not in ("admin", "moderator", "user"):
            raise AccessLevelException
        self._access_level = value

    @property
    def logcount(self):
        return self._logcount

    def increase_logcount(self):
        self._logcount += 1

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}, Access Level: {self.access_level}, Log Count: {self.logcount}"

    def __eq__(self, other):
        return self.access_level == other.access_level


user1 = SiteUser("Oleg Petrov", "oleg.petrov@test.com", "user")
user2 = SiteUser("Ira Bila", "ira.bila@test.com", "admin")
user3 = SiteUser("Inna Tyma", "inna.tyma@test.com", "moderator")

print(user1)
print(user2)
print(user3)

user1.increase_logcount()
print(f"Log Count for {user1.name}: {user1.logcount}")

# Порівняння за рівнем доступу
if user1 == user2:
    print("Users have the same access level.")
else:
    print("Users have different access levels.")
