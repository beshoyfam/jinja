# write_messages.py

from jinja2 import Environment, FileSystemLoader
import os

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
]

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("sample_template.txt")

# def opener(path, flags):
#     return os.open(path, flags, 0o777)

for student in students:
    filename = f"message_{student['name'].lower()}.txt"
    content = template.render(
        student,
        max_score=max_score,
        test_name=test_name
    )
    descriptor = os.open(
    path='filename',
    flags=(
        os.O_WRONLY  # access mode: write only
        | os.O_CREAT  # create if not exists
        | os.O_TRUNC  # truncate the file to zero
    ),
    mode=0o777
    )

    print(f"... not wrote {filename}")
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")