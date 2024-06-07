import customtkinter as ctk
import time

class AnimatedLabel(ctk.CTkLabel):
    def __init__(self, master, text, interval=0.1, **kwargs):
        super().__init__(master, **kwargs)
        self.text = text
        self.interval = interval
        self.current_text = ""
        self.idx = 0
        self.animate()

    def animate(self):
        if self.idx < len(self.text):
            self.current_text += self.text[self.idx]
            self.config(text=self.current_text)
            self.idx += 1
            self.after(int(self.interval * 1000), self.animate)

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
        self.animate_response("This is a sample response.")  # Replace with actual response

    def animate_response(self, response_text):
        response_label = AnimatedLabel(self, text="", fg="black", font=("Arial", 12))
        response_label.pack()
        response_label.animate_text(response_text)

# Main Application
if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("800x600")
    chat_screen = ChatScreen(master=app)
    chat_screen.pack(fill="both", expand=True)
    app.mainloop()
