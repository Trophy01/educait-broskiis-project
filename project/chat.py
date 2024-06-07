import customtkinter
from constants import PADDING_LARGE, PADDING_SMALL
from llm import input_message, add_to_messages_and_gen, messages_chat

class Message(customtkinter.CTkFrame):
    def __init__(self, master, title, text,**kwargs):
        super().__init__(master, **kwargs);

        self.title = customtkinter.CTkLabel(self, text=title)
        self.title.pack(padx=0, pady=0)
        
        self.text = MessageText(self, text)
        self.title.pack(padx=PADDING_SMALL, pady=PADDING_SMALL)


class MessageText(customtkinter.CTkFrame):
    def __init__(self, master, text,**kwargs):
        super().__init__(master, **kwargs);
        self.text = customtkinter.CTkLabel(self, text=text)
        self.text.pack(padx=PADDING_SMALL, pady=PADDING_SMALL)

class Chat(customtkinter.CTkFrame):
    def __init__(self, master, messages,**kwargs):
        super().__init__(master, **kwargs);

        self.messages = []

        for i, x in enumerate(messages):
            self.messages.append(Message(master=self, title=x["title"], text=x["text"], fg_color="red"));
            self.messages[i].pack(padx=PADDING_SMALL, pady=PADDING_SMALL);
#

# class Chat(customtkinter.CTkFrame):
#     def __init__(self, master, messages,**kwargs):
#         super().__init__(master, **kwargs);
#
#         self.messages = customtkinter.CTkLabel(master=self, textvariable=messages,)
#         self.messages.pack(padx=PADDING_SMALL, pady=PADDING_SMALL)

class ChatInput(customtkinter.CTkFrame):
    def __init__(self, master, inp, input_fn,**kwargs):
        super().__init__(master, **kwargs);

        self.input = customtkinter.CTkEntry(self, textvariable=inp)
        self.input.grid(column=0, row=0, padx=PADDING_SMALL, pady=PADDING_LARGE)

        self.enter = customtkinter.CTkButton(self, text="Go", command=input_fn)
        self.enter.grid(column=1, row=0, padx=PADDING_SMALL, pady=PADDING_LARGE, )

class ChatScreen(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs);
        self.inp = customtkinter.StringVar();
        self.inp.set("");

        self.input = ChatInput(master=self, inp=self.inp, input_fn=self.enter)
        self.input.grid(row=2)


    def enter(self):
        add_to_messages_and_gen(self.inp.get())
        self.chat = Chat(master=self, messages=messages_chat, fg_color="transparent");
        self.chat.grid(row=1)

