#def admin():
   # print("admin of the system is called John Doe")
#def user():
    #print("The First user is called Olivier")
#admin()
#user()
#the First way
def student(fname):
    print(fname+"is awesome") 
    print(fname+"is intelligent") 
    print(fname+"is Handsome Boy")   
student("Olivier") 
# the Second way  
def student(lname):
    print(f"{lname} is awesome")  
student(233) 
#the Third way
def user(user1, user2):
    print("Hello {} and {}".format(user1, user2))
user("Lisaa","Lizza")  
#Thhe fourth
def client(name):
    return "Hello" + name
greet=client(input("Enter Your Full Name: "))
print(greet)   