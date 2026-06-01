import tkinter as tk
from tkinter import scrolledtext
import threading
import time

# ---------------- RESPONSES ----------------
responses = {
   "hello": "Hehe! Shinchan says hiiii 🤪✨",
    "hi": "Yo yo! Shinchan here 🕺",
    "how are you": "I’m super-duper awesome, just ate choco chips 🍫",
    "who are you": "I’m Shinchan, the cutest AI chatbot ever 😎",
    "bye": "Bye bye! Don’t forget to bring snacks next time 🍟",
    "joke": "Why did Shinchan bring a ladder to school? Because he wanted to go to high school! 😂",
    "love": "Awww, Shinchan loves you too 💖",
    "sing": "🎶 La la la… Shinchan’s singing is better than karaoke!",
    "dance": "🕺 Shinchan is dancing like a superstar!",
    "food": "I want pudding, pizza, and choco chips NOW 🍕🍮",
    "school": "School is boring… let’s play instead! 😜",
    "mom": "Mooooom! I didn’t do anything… maybe 😇",
    "dad": "Dad is cool but Shinchan is cooler 😎",
    "play": "Let’s play hide and seek… but I’ll hide forever 🤭",
    "funny": "I’m the funniest cartoon ever, don’t you agree? 🤡",
    "cartoon": "Cartoon life is the best life! 📺",
    "ai": "AI means Awesome Intelligence… just like Shinchan!",
    "exit": "Exiting… but Shinchan will miss you 😢",
    "default": "Hehe, Shinchan doesn’t know that… but sounds funny!"
}


# ---------------- CHATBOT ----------------
class ShinchanChatbot:

    def __init__(self, root):

        self.root = root
        self.root.title("Shinchan AI Chatbot")

        # FIXED WINDOW SIZE
        self.root.geometry("900x450")
        self.root.configure(bg="yellow")

        self.dark_mode = False

        # ---------------- TITLE ----------------
        self.banner = tk.Label(
            root,
            text="🎉 Shinchan AI Chatbot 🎉",
            font=("Comic Sans MS", 22, "bold"),
            bg="red",
            fg="white",
            pady=10
        )

        self.banner.pack(fill="x")

        # ---------------- CHAT AREA ----------------
        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Comic Sans MS", 12),
            bg="white",
            fg="black"
        )

        self.chat_area.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

        self.chat_area.config(state="disabled")

        # ---------------- BOTTOM FRAME ----------------
        self.bottom_frame = tk.Frame(
            root,
            bg="yellow",
            height=80
        )

        self.bottom_frame.pack(
            side="bottom",
            fill="x"
        )

        # ---------------- ENTRY ----------------
        self.entry = tk.Entry(
            self.bottom_frame,
            font=("Comic Sans MS", 14),
            bg="lightblue"
        )

        self.entry.pack(
            side="left",
            padx=10,
            pady=10,
            fill="x",
            expand=True
        )

        self.entry.bind("<Return>", self.send_message)

        # ---------------- RIGHT BUTTON FRAME ----------------
        self.button_frame = tk.Frame(
            self.bottom_frame,
            bg="yellow"
        )

        self.button_frame.pack(
            side="right",
            padx=10
        )

        # ---------------- BUTTONS ----------------
        self.send_btn = self.create_button(
            "Send",
            self.send_message
        )

        self.clear_btn = self.create_button(
            "Clear",
            self.clear_chat
        )

        self.restart_btn = self.create_button(
            "Restart",
            self.restart_chat
        )

        self.dark_btn = self.create_button(
            "Dark",
            self.toggle_dark_mode
        )

    # ---------------- BUTTON DESIGN ----------------
    def create_button(self, text, command):

        btn = tk.Button(
            self.button_frame,
            text=text,
            command=command,
            font=("Comic Sans MS", 11, "bold"),
            bg="blue",
            fg="white",
            padx=10,
            pady=5,
            width=10
        )

        btn.pack(
            side="left",
            padx=5
        )

        return btn

    # ---------------- BOT TYPING ----------------
    def bot_typing(self, response):

        self.chat_area.config(state="normal")

        self.chat_area.insert(
            tk.END,
            "🤔 Shinchan is thinking...\n"
        )

        self.chat_area.see(tk.END)

        self.chat_area.config(state="disabled")

        time.sleep(1)

        self.chat_area.config(state="normal")

        self.chat_area.insert(
            tk.END,
            f"🤖 Shinchan: {response}\n\n"
        )

        self.chat_area.see(tk.END)

        self.chat_area.config(state="disabled")

    # ---------------- SEND MESSAGE ----------------
    def send_message(self, event=None):

        user_msg = self.entry.get().lower().strip()

        if user_msg == "":
            return

        self.chat_area.config(state="normal")

        self.chat_area.insert(
            tk.END,
            f"👤 You: {user_msg}\n"
        )

        self.chat_area.config(state="disabled")

        self.chat_area.see(tk.END)

        self.entry.delete(0, tk.END)

        response = responses.get(
            user_msg,
            responses["default"]
        )

        threading.Thread(
            target=self.bot_typing,
            args=(response,),
            daemon=True
        ).start()

    # ---------------- CLEAR CHAT ----------------
    def clear_chat(self):

        self.chat_area.config(state="normal")

        self.chat_area.delete(
            1.0,
            tk.END
        )

        self.chat_area.config(state="disabled")

    # ---------------- RESTART CHAT ----------------
    def restart_chat(self):

        self.clear_chat()

        self.chat_area.config(state="normal")

        self.chat_area.insert(
            tk.END,
            "🔄 Chat Restarted!\n\n"
        )

        self.chat_area.config(state="disabled")

    # ---------------- DARK MODE ----------------
    def toggle_dark_mode(self):

        if not self.dark_mode:

            self.root.configure(bg="black")
            self.bottom_frame.configure(bg="black")
            self.button_frame.configure(bg="black")

            self.banner.config(
                bg="white",
                fg="black"
            )

            self.chat_area.config(
                bg="gray20",
                fg="white"
            )

            self.entry.config(
                bg="gray30",
                fg="white",
                insertbackground="white"
            )

            self.dark_mode = True

        else:

            self.root.configure(bg="yellow")
            self.bottom_frame.configure(bg="yellow")
            self.button_frame.configure(bg="yellow")

            self.banner.config(
                bg="red",
                fg="white"
            )

            self.chat_area.config(
                bg="white",
                fg="black"
            )

            self.entry.config(
                bg="lightblue",
                fg="black",
                insertbackground="black"
            )

            self.dark_mode = False


# ---------------- RUN APP ----------------
if __name__ == "__main__":

    root = tk.Tk()

    app = ShinchanChatbot(root)

    root.mainloop()