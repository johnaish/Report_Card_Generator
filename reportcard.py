import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name, admission_number):
        self.name = name
        self.admission_number = admission_number
        self.subjects = {}

    def add_subject(self, subject, marks):
        self.subjects[subject] = marks

    def get_report_card(self):
        total_marks = 0
        max_marks = len(self.subjects) * 100  # Assuming each subject is out of 100 marks

        report = f"Report Card for {self.name} (Admission No: {self.admission_number})\n"
        report += "-" * 30 + "\n"
        for subject, marks in self.subjects.items():
            report += f"{subject}: {marks}/100\n"
            total_marks += marks

        percentage = (total_marks / max_marks) * 100
        report += "-" * 30 + "\n"
        report += f"Total: {total_marks}/{max_marks}\n"
        report += f"Percentage: {percentage:.2f}%\n"

        return report

class SchoolPortalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("School Portal")
        self.root.configure(bg="#e0f7fa")  # Set background color
        self.root.attributes('-fullscreen', True)  # Make the window full screen
        self.students = []

        # Create main frame
        self.main_frame = tk.Frame(root, bg="#e0f7fa", padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create student input frame
        self.student_frame = tk.LabelFrame(self.main_frame, text="Student Information", bg="#80deea", fg="#00796b", padx=10, pady=10)
        self.student_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.name_label = tk.Label(self.student_frame, text="Student Name:", bg="#80deea", fg="#004d40")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.student_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.admission_number_label = tk.Label(self.student_frame, text="Admission Number:", bg="#80deea", fg="#004d40")
        self.admission_number_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.admission_number_entry = tk.Entry(self.student_frame)
        self.admission_number_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Create subject input frame
        self.subject_frame = tk.LabelFrame(self.main_frame, text="Subject Information", bg="#80deea", fg="#00796b", padx=10, pady=10)
        self.subject_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.subject_label = tk.Label(self.subject_frame, text="Subject:", bg="#80deea", fg="#004d40")
        self.subject_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.subject_entry = tk.Entry(self.subject_frame)
        self.subject_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.marks_label = tk.Label(self.subject_frame, text="Marks:", bg="#80deea", fg="#004d40")
        self.marks_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.marks_entry = tk.Entry(self.subject_frame)
        self.marks_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.add_subject_button = tk.Button(self.subject_frame, text="Add Subject", bg="#26c6da", fg="#ffffff", command=self.add_subject)
        self.add_subject_button.grid(row=2, column=1, pady=5, sticky="ew")

        # Create buttons frame
        self.button_frame = tk.Frame(self.main_frame, bg="#e0f7fa", padx=10, pady=10)
        self.button_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.generate_report_button = tk.Button(self.button_frame, text="Generate Report Card", bg="#26c6da", fg="#ffffff", command=self.generate_report_card)
        self.generate_report_button.pack(fill=tk.X)

        self.current_student = None

    def add_subject(self):
        name = self.name_entry.get()
        admission_number = self.admission_number_entry.get()
        subject = self.subject_entry.get()
        marks = self.marks_entry.get()

        if not name or not admission_number or not subject or not marks:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return

        if not self.current_student or self.current_student.name != name or self.current_student.admission_number != admission_number:
            self.current_student = Student(name, admission_number)
            self.students.append(self.current_student)

        try:
            marks = int(marks)
        except ValueError:
            messagebox.showwarning("Input Error", "Marks should be an integer")
            return

        self.current_student.add_subject(subject, marks)
        self.subject_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Added {subject} with {marks} marks")

    def generate_report_card(self):
        if not self.current_student:
            messagebox.showwarning("Input Error", "No student data available")
            return

        report_card = self.current_student.get_report_card()
        messagebox.showinfo("Report Card", report_card)
        self.name_entry.delete(0, tk.END)
        self.admission_number_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)
        self.current_student = None

def main():
    root = tk.Tk()
    app = SchoolPortalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
