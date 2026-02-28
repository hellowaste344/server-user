import sqlite3

from rich.console import Console

console = Console()

conn = sqlite3.connect("students.db")
conn.execute("""
CREATE TABLE students(
    id TEXT,
    name TEXT,
    department TEXT
    );
""")
conn.execute("""INSERT INTO students VALUES('077', 'x-ashe', 'CS')""")
conn.execute("""INSERT INTO students VALUES('078', 'Lucie', 'IT')""")
conn.execute("""INSERT INTO students VALUES('079', 'Louis', 'Art')""")

conn.commit()

for row in conn.execute("SELECT * FROM students"):
    print(row)

conn.close()

console.print("[bold green]Database created successfully[/bold green]...")
