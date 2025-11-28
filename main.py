class Admin:
    def init(self, name, age, phone, password):
        self.name = name
        self.age = age
        self.phone = phone
        self.password = password
        self.admins = []

    def add_admin(self):
        name = input("What is your name? ")
        age = int(input("What is your age? "))
        phone = input("What is your phone? ")
        password = input("What is your password? ")
        self.admins.append(Admin(name, age, phone, password))

    def remove_admin(self):
        name = input("What is the name to remove? ")
        for admin in self.admins:
            if admin.name == name:
                self.admins.remove(admin)
                print('admin removed successfully')


    def auth(self):
        password = input("What is your password? ")
        if password == self.password:
            print(' u are authenticated')
        else:
            print(' u are not authenticated')

    def view_admins(self):
        for admin in self.admins:
            print(f'name: {admin.name}, age: {admin.age}, phone: {admin.phone}, password: {admin.password}')

class Workers:
    def init(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
        self.workers = []
        self.busy_workers = []
        self.free_workers = []

    def add_worker(self):
        name = input("What is your name? ")
        age = int(input("What is your age? "))
        phone = input("What is your phone? ")
        self.workers.append(Workers(name, age, phone))

    def remove_worker(self):
        name = input("What is your name? ")
        for worker in self.workers:
            if worker.name == name:
                self.workers.remove(worker)
                print('deleted worker successfully')

    def check_worker(self):
        name = input("What is your name? ")
        if name == self.name:
            print(' did u get a car?')
            code = input(" 1. Yes \n 2. No ")
            if code == '1':
                self.busy_workers.append(name)
            else:
                self.free_workers.append(name)

    def view_workers(self):
        for worker in self.workers:
            print(f'name: {worker.name} age: {worker.age} phone: {worker.phone}')

    def view_busy_workers(self):
        for worker in self.busy_workers:
            print(f'name: {worker.name} age: {worker.age} phone: {worker.phone}')

    def view_free_workers(self):
        for worker in self.free_workers:
            print(f'name: {worker.name} age: {worker.age} phone: {worker.phone}')




class Cars:
    def init(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
        self.cars = []
        self.busy_cars = []
        self.free_cars = []

    def add_cars(self):
        model = input("What is your model? ")
        year = int(input("What is your year? "))
        price = int(input("What is your price? "))
        self.cars.append(Cars(model, year, price))

    def remove_cars(self):
        model = input("What is your model? ")
        for car in self.cars:
            if car.model == model:
                self.cars.remove(car)
                print('deleted car successfully')

    def view_cars(self):
        for car in self.cars:
            print(f'Model: {car.model}, Year: {car.year}, Price: {car.price}')

    def view_busy_cars(self):
        for car in self.busy_cars:
            print(f'Model: {car.model}, Year: {car.year}, Price: {car.price}')

    def view_free_cars(self):
        for car in self.free_cars:
            print(f'Model: {car.model}, Year: {car.year}, Price: {car.price}')

    def check_cars(self):
        model = input("What is the model? ")
        if model == self.model:
            print(' did u get this car?')
            code = input(" 1. Yes \n 2. No ")
            if code == '1':
                self.busy_cars.append(model)
            else:
                self.free_cars.append(model)
def view_manger(admin:Admin, worker:Workers, car:Cars):

    print('*** View Manager ***')
    while True:
        print('1. view admins \n 2. view workers \n 3. view cars \n 4. busy workers \n 5. free workers \n 6. busy cars \n 7. free cars  \n 8. return')
        code = input(' Enter your choice: ')
        if code == '1':
            admin.view_admins()
        elif code == '2':
            worker.view_workers()
        elif code == '3':
            car.view_cars()
        elif code == '4':
            worker.view_busy_workers()
        elif code == '5':
            worker.view_free_workers()
        elif code == '6':
            car.view_busy_cars()
        elif code == '7':
            car.view_free_cars()
        elif code == '8':
            break
        else:
            print('Invalid code')


def add_manager(admin:Admin, worker:Workers, car:Cars):
    print('*** Add Manager ***')
    while True:
        print('1. add manager \n 2. add workers \n 3. add cars \n 4. return')
        code = input(' Enter your choice: ')
        if code == '1':
            admin.add_admin()
        elif code == '2':
            worker.add_worker()
        elif code == '3':
            car.add_cars()
        elif code == '4':
             break
        else:
            print('Invalid code')

def remove_manager(admin:Admin, worker:Workers, car:Cars):
    print('*** Remove Manager ***')
    while True:
        print(' 1. remove manager \n 2. remove workers \n 3. remove cars \n 4. return')
        code = input(' Enter your choice: ')
        if code == '1':
            admin.remove_admin()
        elif code == '2':
            worker.remove_worker()
        elif code == '3':
            car.remove_cars()
        elif code == '4':
            break
        else:
            print('Invalid code')

def manager_taxi_park():
    print('*** Taxi Park ***')
    admin = Admin("ju", 11, "12121", "1234")
    worker = Workers("1", 0, "")
    car = Cars("", 0, 0)
    while True:
        print( '1. view panel \n 2. add panel \n 3. remove panel \n 4. exit ')
        code = input(' Enter your choice: ')
        if code == '1':
            view_manger(admin, worker, car)
        elif code == '2':
            add_manager(admin, worker, car)
        elif code == '3':
            remove_manager(admin, worker, car)
        elif code == '4':
            print('Exiting...')
            break
        else:
            print('Invalid code')

if __name__ == '__main__':
    manager_taxi_park()