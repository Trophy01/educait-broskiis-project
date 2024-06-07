import customtkinter as ctk
from constants import PADDING_LARGE, PADDING_SMALL
from llm import add_to_messages_and_gen, messages_chat

class Message(ctk.CTkFrame):
    def __init__(self, master, title, text, fg_color="white", **kwargs):
        super().__init__(master, **kwargs)
        self.title = ctk.CTkLabel(self, text=title, fg_color=fg_color)
        self.text = ctk.CTkLabel(self, text=text)
        self.title.pack(padx=PADDING_SMALL, pady=PADDING_SMALL)
        self.text.pack(padx=PADDING_SMALL, pady=PADDING_SMALL)

class MessageText(ctk.CTkFrame):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, **kwargs)
        self.text = ctk.CTkLabel(self, text=text)
        self.text.pack(padx=PADDING_SMALL, pady=PADDING_SMALL)

class Chat(ctk.CTkFrame):
    def __init__(self, master, messages, **kwargs):
        super().__init__(master, **kwargs)
        self.message_widgets = []
        self.update_messages(messages)

    def update_messages(self, messages):
        # Clear existing messages
        for widget in self.message_widgets:
            widget.destroy()
        self.message_widgets = []
        
        # Add new messages
        for msg in messages:
            message = Message(master=self, title=msg["title"], text=msg["text"], fg_color="red")
            message.pack(padx=PADDING_SMALL, pady=PADDING_SMALL)
            self.message_widgets.append(message)

class ChatInput(ctk.CTkFrame):
    def __init__(self, master, inp, input_fn, **kwargs):
        super().__init__(master, **kwargs)
        self.input = ctk.CTkEntry(self, textvariable=inp)
        self.input.grid(column=0, row=0, padx=PADDING_SMALL, pady=PADDING_LARGE)
        self.enter = ctk.CTkButton(self, text="Go", command=input_fn)
        self.enter.grid(column=1, row=0, padx=PADDING_SMALL, pady=PADDING_LARGE)

class ChatScreen(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.messages = messages_chat
        self.inp = ctk.StringVar()
        self.inp.set("")

        self.input = ChatInput(master=self, inp=self.inp, input_fn=self.enter)
        self.input.grid(row=2)

    def enter(self):
        add_to_messages_and_gen(self.inp.get())
        self.chat.update_messages(messages_chat)
        self.chat.grid(row=1)

# Main Application
if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("800x600")
    chat_screen = ChatScreen(master=app)
    chat_screen.pack(fill="both", expand=True)
    app.mainloop()
