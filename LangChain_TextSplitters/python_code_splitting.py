from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


def calculate_average(numbers):

    total = sum(numbers)
    avg = total / len(numbers)

    return avg


students = [
    Student("Abhijeet", 90),
    Student("Rahul", 85),
    Student("Priya", 95)
]

marks = [90, 85, 95]

average_marks = calculate_average(marks)

print("Average Marks:", average_marks)

for student in students:
    student.display()
"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks[0])