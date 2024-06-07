import customtkinter
from login import RegisterScreen, LoginScreen
from chat import ChatScreen

from constants import PADDING_LARGE, PADDING_SMALL, WINDOW_SIZE
from llm import setup_chat 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Parcel")
        self.geometry(f"{WINDOW_SIZE['x']}x{WINDOW_SIZE['y']}")
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1);

        customtkinter.DrawEngine.preferred_drawing_method = "circle_shapes";
        customtkinter.set_widget_scaling(2);
        customtkinter.set_appearance_mode("dark");
        customtkinter.set_default_color_theme("dark-blue");

        ## Widgets

        # self.chat = customtkinter.StringVar();
        # self.chat.set("");

        self.login = LoginScreen(master=self, fg_color="transparent", firebase="");
        self.login.grid(column=1, row=2, padx=PADDING_LARGE, pady=PADDING_LARGE)
    
    def button_callbck(self):
        self.count.set(self.count.get() + 1);
        print("button clicked")

    def on_login(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.login = LoginScreen(master=self, fg_color="transparent", firebase="");
        self.login.grid(column=1, row=2, padx=PADDING_LARGE, pady=PADDING_LARGE)


    def on_register(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.register = RegisterScreen(master=self, fg_color="transparent", firebase="");
        self.register.grid(column=1, row=2, padx=PADDING_LARGE, pady=PADDING_LARGE)

    def on_chat(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.chat = ChatScreen(master=self, fg_color="transparent");
        self.chat.grid(column=1, row=2, padx=PADDING_LARGE, pady=PADDING_LARGE)

if __name__ == "__main__":
    setup_chat()
    app = App()
    app.mainloop()
