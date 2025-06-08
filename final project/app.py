import tkinter as tk
import random

# Questions, Options, and Answers
quiz = [
    {"question": "Who wrote 'Romeo and Juliet'?", "choices": ["Shakespeare", "Chaucer", "Wordsworth", "Milton"], "answer": "Shakespeare", "hint": "Famous English playwright"},
    {"question": "What is the capital of France?", "choices": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris", "hint": "City of Love"},
    {"question": "Which planet is known as the Red Planet?", "choices": ["Mars", "Earth", "Jupiter", "Venus"], "answer": "Mars", "hint": "Fourth from the Sun"},
    {"question": "What is 9 * 9?", "choices": ["81", "72", "99", "90"], "answer": "81", "hint": "Square of 9"},
    {"question": "Which animal is known as the King of the Jungle?", "choices": ["Lion", "Tiger", "Elephant", "Bear"], "answer": "Lion", "hint": "It roars"},
    {"question": "What gas do plants breathe in?", "choices": ["CO2", "O2", "Hydrogen", "Nitrogen"], "answer": "CO2", "hint": "Carbon based"},
    {"question": "What is H2O?", "choices": ["Water", "Oxygen", "Hydrogen", "Salt"], "answer": "Water", "hint": "Covers 71% of Earth"},
    {"question": "Fastest land animal?", "choices": ["Cheetah", "Horse", "Leopard", "Lion"], "answer": "Cheetah", "hint": "Spots and speed"},
    {"question": "Who invented the telephone?", "choices": ["Bell", "Newton", "Edison", "Tesla"], "answer": "Bell", "hint": "Alexander Graham"},
    {"question": "Largest ocean on Earth?", "choices": ["Pacific", "Atlantic", "Indian", "Arctic"], "answer": "Pacific", "hint": "It's calm by name"}
]

# Shuffle questions
random.shuffle(quiz)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.configure(bg="#2B2B2B")  # Dark Charcoal Gray background
        self.current_q = 0
        self.score = 0

        self.question_label = tk.Label(
            root, text="", font=("Arial", 16, "bold"),
            fg="#E0E0E0", bg="#2B2B2B", wraplength=500
        )
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for _ in range(4):
            btn = tk.Button(
                root, text="", font=("Arial", 12),
                bg="#424242", fg="#E0E0E0", relief="flat",
                activebackground="#616161", bd=0, width=30, height=2,
                cursor="hand2"
            )
            btn.config(highlightthickness=0, borderwidth=0)
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.score_label = tk.Label(
            root, text="Score: 0", font=("Arial", 12),
            fg="#FFFFFF", bg="#2B2B2B"
        )
        self.score_label.pack(pady=10)

        self.feedback_label = tk.Label(
            root, text="", font=("Arial", 12),
            fg="#6EC1E4", bg="#2B2B2B"
        )
        self.feedback_label.pack()

        self.hint_button = tk.Button(
            root, text="Show Hint", command=self.show_hint,
            font=("Arial", 10), bg="#37474F", fg="#E0E0E0",
            activebackground="#78909C", relief="flat"
        )
        self.hint_button.pack(pady=5)

        self.next_button = tk.Button(
            root, text="Next", command=self.next_question,
            font=("Arial", 12, "bold"), bg="#546E7A", fg="#E0E0E0",
            activebackground="#78909C", relief="flat"
        )
        self.next_button.pack(pady=10)
        self.next_button.pack_forget()

        self.load_question()

    def load_question(self):
        self.feedback_label.config(text="", fg="#6EC1E4")
        self.hint_button.config(state="normal")
        self.next_button.pack_forget()

        q_data = quiz[self.current_q]
        self.correct_answer = q_data["answer"]
        self.hint = q_data.get("hint", "Think logically!")

        self.question_label.config(text=f"Q{self.current_q+1}: {q_data['question']}")
        options = q_data["choices"]
        random.shuffle(options)

        for i, btn in enumerate(self.option_buttons):
            btn.config(
                text=options[i], state="normal",
                command=lambda idx=i: self.check_answer(idx),
                bg="#424242", fg="#E0E0E0"
            )

    def check_answer(self, index):
        selected = self.option_buttons[index].cget("text")
        if selected == self.correct_answer:
            self.feedback_label.config(text="✅ Correct!", fg="#4CAF50")  # Medium Green
            self.option_buttons[index].config(bg="#4CAF50")
            self.score += 1
        else:
            self.feedback_label.config(
                text=f"❌ Wrong! Correct: {self.correct_answer}", fg="#E57373"  # Soft Red
            )
            self.option_buttons[index].config(bg="#E57373")
            for btn in self.option_buttons:
                if btn.cget("text") == self.correct_answer:
                    btn.config(bg="#4CAF50")

        for btn in self.option_buttons:
            btn.config(state="disabled")

        self.score_label.config(text=f"Score: {self.score}")
        self.next_button.pack(pady=10)

    def show_hint(self):
        self.feedback_label.config(text=f"💡 Hint: {self.hint}", fg="#6EC1E4")  # Soft Sky Blue
        self.hint_button.config(state="disabled")

    def next_question(self):
        self.current_q += 1
        if self.current_q < len(quiz):
            self.load_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(
            self.root, text="🎉 Quiz Completed!", font=("Arial", 20, "bold"),
            fg="#FFEB3B", bg="#2B2B2B"  # Warm Yellow
        ).pack(pady=20)
        tk.Label(
            self.root, text=f"Your Final Score: {self.score} / {len(quiz)}",
            font=("Arial", 16), fg="#90CAF9", bg="#2B2B2B"  # Light Blue
        ).pack(pady=10)
        tk.Button(
            self.root, text="Restart", command=self.restart,
            font=("Arial", 12), bg="#546E7A", fg="#E0E0E0", activebackground="#78909C",
            relief="flat"
        ).pack(pady=20)

    def restart(self):
        random.shuffle(quiz)
        self.current_q = 0
        self.score = 0
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500")
    app = QuizApp(root)
    root.mainloop()
