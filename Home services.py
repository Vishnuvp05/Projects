from datetime import datetime
class UsersData:
    users=[]
    def __init__(self, user_id:int, user_name:str, mail_id:str, phone_no:str, password:str):
        # Constructor for initializing user data
        self.user_id = user_id
        self.user_name = user_name
        self.mail_id = mail_id
        self.phone_no = phone_no
        self.password = password

class UserFunctionality():
    # Method Overloading based on the type and number of parameters.
    def validate(self, mail_id, password=None):
        # Validate user based on mail_id and password
        registered_mail_id = [user.mail_id for user in UsersData.users if user.mail_id == mail_id]

        if registered_mail_id==[] and password==None:
            # If mail_id is not registered and no password provided, return True
            return True
        else:
            verified_password = [user.password for user in UsersData.users if user.password == password]
            if registered_mail_id and verified_password:
                # If mail_id is registered and password is verified, return True
                return True
        
    def signup(self):
        # User signup functionality
        user_id = (UsersData.users[-1].user_id)+1
        user_name = input("Enter User name:\n").lower()
        mail_id = input("Enter Mail Id:\n").lower()
        phone_no = input("Enter a Mobile number:\n")
        password = input("Enter a password:\n")

        if self.validate(mail_id):
            new_user = UsersData(user_id, user_name, mail_id, phone_no,password)
            UsersData.users.append(new_user)
            return mail_id

    def login(self):
        # User login functionality
        input_id = input("Enter your registered mail id:\n").lower()
        input_password = input("\nEnter your password:\n")

        if self.validate(input_id, input_password):
            return input_id   
class ServicesData():
    services=[]
    def __init__(self,service_id,service_name,cost):
        self.service_id=service_id
        self.service=service_name
        self.cost=cost
            
class SerivesFunctionality():
    def display_info(self):
        for service in ServicesData.services():
                print(service.service_id,'\t',service.service_name,'\t',service.cost)
    def select_service(self):
        service_id=int(input("Enetr Movie id : \n"))
        for service in ServicesData.services:
            if service.service_id==service_id:
                return service.service_name 
    
class ExecutiveData():
    executives=[]
    def __init__(self,executive_id,executive_name,location,rating):
        self.executive_id=executive_id
        self.excutive_name=executive_name
        self.location=location
        self.rating=rating

class ExcutiveFunctionality():
    def display_info(self,service):
        for executive in ExecutiveData.executives:
            if service in executive.executives:
                print(executive.executive_id,'\t',executive.executive_name,'\t',executive.location,'\t',executive.rating)
    def select_theatre(self,selected_service):
        executive_id=int(input("\n Enter executive id: \n"))
        for executive in ExecutiveData.executives:
            if executive.executive_id==executive_id and selected_service in executive.services:
                return executive.executive_name
    def display_showtime(self, selected_executive):
        
        print("--------------------------------------------------------\n")
        for executive in ExecutiveData.executives:
            if executive.executive_name == selected_executive:
                [print(show_id, show_time) for show_id, show_time in executive.show_time.items()]
        return [executive.show_time for theatre in executive.executives if executive.executive_name == selected_executive]

    def select_showtime(self, selected_executive):
        # Select a showtime based on user input
        show_time = self.display_showtime(selected_executive)
        show_id = int(input("\nEnter the Show_id:\n"))
        print("--------------------------------------------------------\n")
        if show_id > 0 and show_id <= 4: 
            return show_time[0][show_id] 
                

class BookingsData:
    bookings = []
    def __init__(self, mail_id, selected_service, selected_executive, selected_show_time, total_price, payment_mode,booked_time):
        # Constructor for initializing booking data
        self.mail_id = mail_id
        self.service = selected_service
        self.executive = selected_executive
        self.show_time = selected_show_time
        self.price = total_price
        self.payment_mode = payment_mode
        self.booked_time = booked_time

class BookingFunctionality():
    def booking_preview(self, mail_id, selected_service, selected_executive, selected_show_time, total_price):
        print("--------------------------------------------------------\n")
        print("Booking Preview:\n")
        print(f'Service Details: {selected_service}')
        print(f'Executive Name: {selected_executive}')
        print(f'Show Details: {selected_show_time}')
        print(f'Total amount: {total_price}')
        print("--------------------------------------------------------\n")
        print("Payment Options:\n1. Card\n2. UPI")
        payment_choice = int(input("\nChoose a payment option:\n"))
        print("--------------------------------------------------------\n")
        if payment_choice != 1 and payment_choice != 2:
            print("Invalid Payment method")
            return False
        
        else:
            if payment_choice == 1:
                payment_mode = "Card"
                print("Booked Successfully")
            elif payment_choice == 2:
                payment_mode = "UPI"
                print("Booked Successfully")
            booked_time = datetime.now().strftime("%y/%m/%d,%H:%M:%S")    
            new_booking = BookingsData(mail_id, selected_service, selected_executive, selected_show_time, total_price, payment_mode, booked_time)
            BookingsData.bookings.append(new_booking)
            return True
        
    def display_history(self):
        # Display booking history
        if len(BookingsData.bookings) == 0:
            print("Booking history is empty.")
        else:
            print("--------------------------------------------------------\n")
            for booking in BookingsData.bookings:
                    print(booking.service, booking.executive, booking.show_time, booking.price, booking.payment_mode, booking.booked_time, sep=' -- ')
    
    def delete_history(self):
        # Delete booking history
        if len(BookingsData.bookings) == 0:
            print("Booking history is empty.")
        else:
            BookingsData.bookings.pop()
            print("Your last history has been deleted")
            choice = input("\nDo you want to clear your all history? (y - to clear):\n")
            if choice.lower() ==  'y':
                BookingsData.bookings.clear()
                print("Booking history deleted successfully")
            else:
                print("Thank you")


class HomeServices(UserFunctionality):

    def __init__(self):
        # Constructor for initializing Movie Booking System
        self.service = SerivesFunctionality()
        self.executive = ExcutiveFunctionality()
        self.booking = BookingFunctionality()
        self.stay_in = True
        self.mail_id = None

    def signup_or_login(self):
        # Prompt user to signup or login
        choice = input("Enter a valid input(Signup/Login): \n").title()
        if choice == 'Signup':
            self.mail_id = self.signup()
            if not self.mail_id:
                print("User already exists.")
                self.stay_in = False

        elif choice == 'Login':
            self.mail_id = self.login()
            if not self.mail_id:
                print('Invalid mail id or password.')
                self.stay_in = False
    def run(self):
        # Main loop for Movie Booking System
        while self.stay_in:
            print("--------------------------------------------------------\n")
            print("Menu:")
            print("1. Book service")
            print("2. Display Booking history")
            print("3. Delete Booking history")
            print("4. Logout")
            choice = int(input("\nEnter your choice:\n"))
            if choice == 1:
                self.book_service()
            elif choice == 2:
                self.display_booking_history()
            elif choice == 3:
                self.delete_booking_history()
            elif choice == 4:
                self.logout()
            else:
                print("Invalid Choice")

    def book_service (self):
        # Book a movie and initiate the booking process
        self.service.display_info()
        selected_service = self.service.select_service()
        if not selected_service:
            print("Invalid movie id.")
            return
        self.service.display_info(selected_service)
        selected_executive = self.executive.select_executive(selected_service)
        if not selected_executive:
            print("Invalid theatre id.")
            return
        
        selected_show_time = self.executive.select_showtime(selected_executive)
        if not selected_show_time:
            print("Invalid show id.")
            return
        
        total_price = len(selected_executive) * 200
        if not self.booking.booking_preview(self.mail_id, selected_service, selected_executive, selected_show_time, total_price):
            self.stay_in = False
        
    def display_booking_history(self):
        # Display booking history
        self.booking.display_history()
    def delete_booking_history(self):
        # Delete booking history
        self.booking.delete_history()

    def logout(self):
        # Logout the user from the system
        print("Logout Successfully.")
        self.stay_in = False  
            

  
                
                
    


if __name__ == '__main__':
    user1 = UsersData(1, 'vishnu', 'vishnu123@gmail.com','9876543210', 'vishnu123')
    user2 = UsersData(2, 'arun', 'arun123@gmail.com', '1234567890', 'arun123')
    user3 = UsersData(3, 'varun', 'varun123@gmail.com', '0987654321', 'varun123')
    UsersData.users.append(user1)
    UsersData.users.append(user2)
    UsersData.users.append(user3) 

    movie1 = ServicesData(1, 'electrical','$500')
    movie2 = ServicesData(2, 'Carpeting','$1000')
    movie3 = ServicesData(3, 'Beauty','$1500')
    ServicesData.services.append(movie1)
    ServicesData.services.append(movie2)
    ServicesData.services.append(movie3) 


    executive1=ExecutiveData(1,'adolf','chennai','5.0')
    executive2=ExecutiveData(2,'vignesh','coimbatore','4.5')
    executive3=ExecutiveData(3,'dhanush','bangalore','4.9')
    ExecutiveData.executives.append(executive1)
    ExecutiveData.executives.append(executive2)
    ExecutiveData.executives.append(executive3)



    booking_system = HomeServices()
    booking_system.signup_or_login()
    booking_system.run()
