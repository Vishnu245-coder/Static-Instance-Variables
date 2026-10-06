class Hospital:

    hospital_name = "Apollo Hospital"   # Class / Static variable

    def patient_details(self, patient_name, age, disease): 
        self.patient_name = patient_name
        self.age = age
        self.disease = disease

    def display(self):
        print("Hospital Name :", Hospital.hospital_name)
        print("Patient Name  :", self.patient_name)
        print("Age           :", self.age)
        print("Disease       :", self.disease)


p1 = Hospital()
p1.patient_details("Ravi", 25, "Fever")
p1.display()

print()

p2 = Hospital()
p2.patient_details("Suresh", 30, "Cold")
p2.display()



# EXAMPLE - 2


class Mobile:

    Brand_name = "Apple"   # Class / Static variable
    Storage=256

    def mobile_details(self, Model_name, Price): 
        self.Model_name = Model_name
        self.Price = Price
        

    def display(self):
        print("Brand Name :", Mobile.Brand_name)
        print("Model Name :", self.Model_name)
        print("Price      :", self.Price)
        print("Storage    :", Mobile.Storage)
        
print()

p1 = Mobile()
p1.mobile_details("iphone 18 pro","1,64,000")
p1.display()

print()

p2 = Mobile()
p2.mobile_details("iphone 18 pro Max","1,89,000")
p2.display()

# EXAMPLE - 3

class Restaurent:

    Restaurent_name = "Mehfil"   # Class / Static variable
    

    def Item_details(self, Item, Price,location): 
        self.Item = Item
        self.Price = Price
        self.location=location
        

    def display(self):
        print("Restaurent Name :", Restaurent.Restaurent_name)
        print("Item Name :", self.Item)
        print("Price      :", self.Price)
        print("Location   :",self.location)

print()
        
p1 = Restaurent()
p1.Item_details("Chicken Biryani",250,"Kukatpally")
p1.display()

print()

p2 = Restaurent()
p2.Item_details("Mutton Biryani",300,"Dilsukhnagar")
p2.display()

# EXAMPLE - 4


class Hotel:

    Brand_name = "Taj Hotel"   # Class / Static variable
    

    def Customer_details(self, Customer_name, Room_No,Room_Type): 
        self.Customer_name = Customer_name
        self.Room_No = Room_No
        self.Room_Type=Room_Type
        

    def display(self):
        print("Hotel Name :", Hotel.Brand_name)
        print("Customer Name :", self.Customer_name)
        print("Room No      :", self.Room_No)
        print("Room Type    :", self.Room_Type)
        
print()

p1 = Hotel()
p1.Customer_details("Adam",24,"Deluxe")
p1.display()

print()

p2 = Hotel()
p2.Customer_details("Charlie",45,"Executive")
p2.display()

print()

p3 = Hotel()
p3.Customer_details("Srinu",31,"Suite")
p3.display()


# EXAMPLE - 5


class Store:

    Store_name = "Reliance Digital"   # Class / Static variable
    

    def Item_details(self, Item, Price): 
        self.Item = Item
        self.Price = Price
    

    def display(self):
        print("Brand Name :", Store.Store_name)
        print("Item Name  :", self.Item)
        print("Price      :", self.Price)
        
        
print()

p1 = Store()
p1.Item_details("Laptop","68,999")
p1.display()

print()

p2 = Store()
p2.Item_details("Mobile","30,000")
p2.display()
