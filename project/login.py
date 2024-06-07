import customtkinter
from constants import PADDING_LARGE, PADDING_SMALL

class LoginButton(customtkinter.CTkFrame):
    def __init__(self, main_text, master, login, google, go_to_fn, go_to_txt,**kwargs):
        super().__init__(master, **kwargs);
       
        self.button = customtkinter.CTkButton(self, text=main_text, command=login)
        self.button.grid(column=1, row=0, padx=PADDING_SMALL, pady=PADDING_LARGE,)
        
        self.google = customtkinter.CTkButton(self, text="G", command=google, width=25, height=25,)
        self.google.grid(column=0, row=0, padx=PADDING_SMALL, pady=PADDING_LARGE)

        self.go_to = customtkinter.CTkButton(self, text=go_to_txt, command=go_to_fn, height=15)
        self.go_to.grid(column=1, row=1, padx=PADDING_SMALL, pady=PADDING_LARGE)

class LoginForm(customtkinter.CTkFrame):
    def __init__(self, master, email, password, **kwargs):
        super().__init__(master, **kwargs);
        
        self.email_entry = customtkinter.CTkEntry(self, textvariable=email, placeholder_text="Enter Email",);
        self.email_entry.pack(pady=PADDING_LARGE)
        self.password_entry = customtkinter.CTkEntry(self, textvariable=password, placeholder_text="Enter Email",);
        self.password_entry.pack(pady=PADDING_LARGE)

class LoginScreen(customtkinter.CTkFrame):
    def __init__(self, master, firebase, **kwargs):
        super().__init__(master, **kwargs);
        
        self.master = master
        
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        self.email = customtkinter.StringVar()
        self.email.set("Enter Email")

        self.password = customtkinter.StringVar()
        self.password.set("Enter Password")
        
        self.form = LoginForm(master=self, fg_color="transparent", email=self.email, password=self.password);
        self.form.grid(column=1, row=0)
        # self.form._set_scaling(3)
        
        self.buttons = LoginButton(master=self, fg_color="transparent" ,login=self.login, google=self.google, main_text="Login", go_to_fn=self.register_fn, go_to_txt="Maybe register?");
        self.buttons.grid(column=1, row=1)

    def google(self):
        self.master.on_chat()
    
    def login(self):
        pass
    
    def register_fn(self):
        self.master.on_register()


class RegisterForm(customtkinter.CTkFrame):
    def __init__(self, master, email, password, confirm,**kwargs):
        super().__init__(master, **kwargs);
        
        self.email_entry = customtkinter.CTkEntry(self, textvariable=email, placeholder_text="Enter Email",);
        self.email_entry.pack(pady=PADDING_LARGE)
        self.password_entry = customtkinter.CTkEntry(self, textvariable=password, placeholder_text="Enter Password",);
        self.password_entry.pack(pady=PADDING_LARGE)
        self.confirm_entry = customtkinter.CTkEntry(self, textvariable=confirm, placeholder_text="Confirm Password",);
        self.confirm_entry.pack(pady=PADDING_LARGE)

class RegisterScreen(customtkinter.CTkFrame):
    def __init__(self, master, firebase, **kwargs):
        super().__init__(master, **kwargs);
        
        self.master = master

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        self.email = customtkinter.StringVar()
        self.email.set("Enter Email")

        self.password = customtkinter.StringVar()
        self.password.set("Enter Password")
        
        self.confirm = customtkinter.StringVar()
        self.confirm.set("Confirm Password")
        
        self.form = RegisterForm(master=self, fg_color="transparent", email=self.email, password=self.password, confirm=self.confirm);
        self.form.grid(column=1, row=0)
        # self.form._set_scaling(3)
        
        self.buttons = LoginButton(master=self, fg_color="transparent" ,login=self.register_user, google=self.google, main_text="Register", go_to_txt="Maybe login?", go_to_fn=self.login_fn);
        self.buttons.grid(column=1, row=1)

    def google(self):
        pass
    
    def register_user(self):
        pass

    def login_fn(self):
        self.master.on_login()
