import tkinter
import customtkinter
import time

def accountPage():
    loginButton.pack_forget()
    signUpButton.pack_forget()
    usernameLabel.pack_forget()
    usernameEntry.pack_forget()
    passwordLabel.pack_forget()
    passwordEntry.pack_forget()
    loginFinalButton.pack_forget()
    typeLabel.configure(text="Login Successful!", text_color="green")
    typeLabel.pack(pady="30")
    passwordLabel.configure(text="This is your account.")
    passwordLabel.pack(pady="20")


def logIn():
    file= open("accounts.txt","r")
    read= file.read()
    account=str(read)
    typedin= str(usrvar.get()+" "+pswdvar.get())
    import string

    def check(string_to_search):
        with open("accounts.txt", 'r') as read_obj:
            for line in read_obj:
                # List of words (without punctuation or list characters)
                if string_to_search.strip() == line.strip():
                    return True
                else:
                    typeLabel.pack()
                    typeLabel.configure(text="Incorrect username or password",text_color="red")
    if check(typedin):
        accountPage()

def writeToFile():
    usernameSignUpLabel.pack_forget()
    usernameSignUpEntry.pack_forget()
    passwordSignUpLabel.pack_forget()
    passwordSignUpEntry.pack_forget()
    signUpFinalButton.pack_forget()
    usr=usrtext.get()
    pswd=pswdtext.get()
    account= str(usr+" "+pswd)
    file = open("accounts.txt","a")
    file.write(account + "\n")
    file.close()
    loginButton.pack(pady="200")
    signUpButton.pack(pady="2")
def loginPageSetup():
    app.title("Log in")
    loginButton.pack_forget()
    signUpButton.pack_forget()
    usernameLabel.pack(pady="37")
    usernameEntry.pack(pady="75")
    passwordLabel.pack()
    passwordEntry.pack(pady="75")
    loginFinalButton.pack()

def signUpPageSetup():
    app.title("Sign Up")
    # hides buttons
    loginButton.pack_forget()
    signUpButton.pack_forget()
    #shows page
    usernameSignUpLabel.pack(pady="37")
    usernameSignUpEntry.pack(pady="75")
    passwordSignUpLabel.pack()
    passwordSignUpEntry.pack(pady="75")
    signUpFinalButton.pack()



#sys settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Log in or Sign up ")

# UI TIME!!!!

#Login button
loginButton= customtkinter.CTkButton(app,text="Log In",command=loginPageSetup)
loginButton.pack(pady="200")
#Sign up button
signUpButton= customtkinter.CTkButton(app,text="Sign Up",command=signUpPageSetup)
signUpButton.pack(pady="2")



#LOG IN PAGE
usrvar= tkinter.StringVar()
global usernameLabel
usernameLabel= customtkinter.CTkLabel(app,text="Username")
usernameLabel.pack_forget()
global usernameEntry
usernameEntry= customtkinter.CTkEntry(app,width=350,height=40,textvariable=usrvar)
usernameEntry.pack_forget()
pswdvar = tkinter.StringVar()
global passwordLabel
passwordLabel = customtkinter.CTkLabel(app, text="Password")
passwordLabel.pack_forget()
global passwordEntry
passwordEntry = customtkinter.CTkEntry(app, width=350, height=40, textvariable=pswdvar)
passwordEntry.pack_forget()
global loginFinalButton
loginFinalButton= customtkinter.CTkButton(app,text='Log In', command=logIn)
loginFinalButton.pack_forget()
global typeLabel
typeLabel= customtkinter.CTkLabel(app,text="")
typeLabel.pack_forget()
# Sign up page
global usernameSignUpLabel
usernameSignUpLabel= customtkinter.CTkLabel(app,text="Enter the Username for your New account")
usernameSignUpLabel.pack_forget()
global usrtext
usrtext= tkinter.StringVar()
usernameSignUpEntry= customtkinter.CTkEntry(app,width=350,height=40,textvariable=usrtext)
usernameSignUpEntry.pack_forget()
# password
global passwordSignUpLabel
passwordSignUpLabel = customtkinter.CTkLabel(app, text=" Enter your Password for your New account")
passwordSignUpLabel.pack_forget()
global pswdtext
pswdtext= tkinter.StringVar()
global passwordSignUpEntry
passwordSignUpEntry = customtkinter.CTkEntry(app, width=350, height=40,textvariable=pswdtext)
passwordSignUpEntry.pack_forget()
# Sign up button
global signUpFinalButton
signUpFinalButton = customtkinter.CTkButton(app, text='Sign up', command=writeToFile)
signUpFinalButton.pack_forget()
# run app
app.mainloop()