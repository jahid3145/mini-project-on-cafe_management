
#PyChat -Simple chat App
#users can regidter and send messages to each other.
#Example:
       
#        Register : Alice,Bob
#        Message : Alice --> Bob:Hello!
#        Chat History:
#        ALice --> Bob :HEllo!


users = []
chat_history = []
    

def show_menu():
    print("====PyChat====")
    print("1. Register User")
    print("2. Send Message")
    print("3. Show Chat History")
    print("4. Exit")
    

    
def register_user():
    global users
    
    name = input("Enter Your Username : ")
    if name in users:
        print("Usernmae already existed")
    else:
        users.append(name)
        print(f'{name} Register successfully.')
        
        
def send_message():
    global users,chat_history
    
    sender = input("Enter The Username : ")
    
    if sender not in users:
        print('User not Registered!')
        return
    receiver = input ("Enter Receiver Username : ")
    
    if receiver not in users:
        print("Reciever not Registered!")
        return
    message = input("Enter Your message:")
    
    chat = f'{sender} ---> {receiver} : {message}'
    chat_history.append(chat)
    print("Message Sent")
    
def show_history():
    global chat_history
    
    print('====Chat History====')
    if not chat_history:
        print('No Message Yet. ')
    else:
        for msg in chat_history:
            print(msg)
    
    
def menu():
    while True:
        show_menu()
        
        choice = input("Enter Your Choice(1-4) : ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            send_message()
        elif choice == '3':
            show_history()
        elif choice == '4':
            print("Exiting The Chat.>> Bye!")
            break
        else:
            print("Invaild input")
            
            
menu()
        
        
    
    



