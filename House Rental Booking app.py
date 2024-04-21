users=[]
owners=[]
class User:
    def __init__(self,user_id,user_name,email,phone_no,password):
        self.user_id=user_id
        self.user_name=user_name
        self.email=email
        self.phone_no=phone_no
        self.password=password
    
    def view_details(self):
        print(f'user_id : {self.user_id}')
        print(f'user_name : {self.user_name}')
        print(f'email : {self.email}')
        print(f'phone_no : {self.phone_no}')

    def validate_login(self,user_id,password):
        for user in users:
            if user.user_id==user_id and user.password==password:
                return user
    
class Owner(User): #simple inheritance
    def __init__(self,owner_id,user_id,user_name,email,phone_no,password):
        super().__init__(user_id,user_name,email,phone_no,password)
        self.owner_id=owner_id
    
    def validate_login(self, owner_id, password):
        for owner in owners:
            if owner.owner_id==owner_id and owner.password==password:
                return owner

class Admin:
    def __init__(self,name,password):
        self.name=name
        self.password=password

    def login(self,username,password):
        return self.name==username and self.password==password 

class House:
    def __init__(self,house_id,locality,city,sqr_feet,type_name,rent,owner_id):
        self.house_id=house_id
        self.locality=locality
        self.city=city
        self.sqr_feet=sqr_feet
        self.type_name=type_name
        self.rent=rent
        self.owner_id=owner_id
    
    def view_details(self):
        print(f'house_id : {self.house_id}')
        print(f'locality : {self.locality}')
        print(f'city {self.city}')
        print(f' sqr_feet {self.sqr_feet}')
        print(f' type_name : {self.type_name}')
        print(f' rent : {self.rent}')

class Booking :
    def __init__(self,booking_id,house_id,user_id,owner_id,check_in_data,payment_method):
        self.booking_id=booking_id
        self.house_id=house_id
        self.user_id=user_id
        self.owner_id=owner_id
        self.check_in_data=check_in_data
        self.payment_method=payment_method
    
    def view_details(self,houses,users,owners):
        house = next((h for h in houses if h.house_id == self.house_id), None)
        user = next((u for u in users if u.user_id == self.user_id), None)
        owner = next((o for o in owners if o.owner_id == self.owner_id), None)

        if house and user and owner:
            print(f"Booking ID: {self.booking_id}")
            print("House Details:")
            house.view_details()
            print("User Details:")
            user.view_details()
            print("Owner Details:")
            owner.view_details()
            print(f"Check-in Date: {self.check_in_date}")
            print(f"Payment Method: {self.payment_method}")
        else:
            print("Booking details not found.")



class App:
    def __init__(self):
        self.stay_in=True
        self.houses=[]
        self.bookings=[]
        self.admin=Admin('thor','thor123')

        self.houses.append(House(1, "T Nagar Colony", "Chennai", "1000", "Apartment", 5000, 1))
        self.houses.append(House(2, "Tambaram Colony", "Chennai", "1500", "Villa", 10000, 2))



    
    def run(self):
        while self.stay_in==True:
            print("Welcome to the House Rental App")
            print("1. Register")
            print("2. Login")
            print("3. Owner Login")
            print('4.Admin Login ')
            print("5. Exit")
            choice =int(input("Enter your choice: "))
            if choice==1:
                self.register()
            elif choice==2:
                self.login()
            elif choice==3:
                self.owner_login()
            elif choice==4:
                self.admin_login()
            elif choice==5:
                break
            else:
                print("Invalid input please try again")
        print("Thank you for using the app")

    def register(self):
        name=input("Enter your name : ")
        email=input("Enter your mail id : ")
        phone_no=input("Enter your mobile no :")
        password=input('Set your password : ')
        user_id=len(users)+1
        new_user=User(user_id,name,email,phone_no,password)
        users.append(new_user)
        print('Registration Successfull')
    def login(self):
            user_id=int(input("Enter your user_id : "))
            password=input('Enter your password : ')
            user=User.validate_login(self,user_id,password)
            if user:
                print('Login Succeesful')
                self.user_menu(user)
                self.stay_in=False
            else:
                print("Invalid input please Try again")
    def owner_login(self):
        owner_id=int(input('Enter the owner id :'))
        password=input('Enter the password : ')
        owner=Owner.validate_login(self,owner_id,password)
        if owner:
            print('Login successful')
            self.owner_menu(owner)
            self.stay_in=False
        else:
            print('Invalid id or pssword')
    def owner_menu(self,owner):
        while True:
            print('Owner menu : ')
            print('1.add house ')
            print('2.View details ')
            print("3.Logout")
            choice=int(input("Enter your choice :"))
            if choice==1:
                self.add_house(owner)
            elif choice==2:
                owner.view_details()
            elif choice==3:
                break
            else:
                print('Invalid choice please try again' )
    def add_house(self,owner):
        house_id=len(self.houses)+1
        locality=input('Enter the locality : ')
        city=input('Enter the city :')
        sqr_feet=input('Enter the square feet : ')
        type_name=input('Enter the type of home  : ')
        rent=int(input('Enter the rent amunt : '))
        new_house=House(house_id,locality,city,sqr_feet,type_name,rent,owner.owner_id)
        self.houses.append(new_house)
        print('House added successfully')

                
    def user_menu(self,user):
        while True:
            print("User menu")
            print("1.Search Houses")
            print("2.Book Houses")
            print("3.Log out")
            choice=int(input("Enter your choice : "))
            if choice==1:
                self.search_houses()
            elif choice==2:
                self.book_house(user)
            
    def admin_login(self):
        user_name=input('Enter theusername :')
        password=input('Enter the password :')
        if self.admin.login(user_name,password):
            print('Admin login succesful')
            self.admin_menu()
        else:
            print('Invalid admin id or password')
    def admin_menu(self):
        while True:
            print('Admin menu : ')
            print('1.View Booking History ')
            print("2.Logout")
            choice=int(input("Enter your choice : "))
            if choice==1:
                self.view_booking_history()
            elif choice==2:
                break
            else:
                print('Invalid input please try again')
    def view_booking_history(self):
        if self.bookings:
            print('Booking History :')
            for booking in self.bookings:
                booking.view_deatils(self.houses,users,owners)    
                print()
        else:
            print('No Booking History found')   



    
    def search_houses(self):
        keyword=input("Enter a keyword to foun house : ")
        found_houses=[]
        for house in self.houses:
            if keyword.lower() in house.city.lower() or keyword.lower() in house.locality.lower() :
                found_houses.append(house)
        
        if found_houses:
            print('Search results : ')
            for house in found_houses:
                house.view_details()
                print()
        else:
            print('no houses found')
    def book_house(self,user):

        house_id=input('Enter house id :' )
        owner_id=input("Enter the owner id : ")
        check_in_date=input('enter check in date : ')
        payment_method=input('enter the payment method : ')
        booking_id=len(self.bookings)+1
        new_booking=Booking(booking_id,house_id,user.user_id,owner_id,check_in_date,payment_method)
        self.bookings.append(new_booking)
        print('Booking succesful ')
        print('Thank you for using the app')

        

if __name__=='__main__':
    user1=User(1,'vishnu','vishnu@gmail',987,"vishnu123")
    user2=User(2,'prasath','prasath@gmail',789,"prasath123")
    users.append(user1)
    users.append(user2)

    owner1=Owner(1,3,'owner','owner@gmail',786,'owner123')
    owners.append(owner1)

work=App()
work.run()

