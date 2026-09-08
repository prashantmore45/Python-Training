# Python Programming Training

This repository contains the programs, exercises, and projects completed during a seven-day Python Programming training program.

## Training Details

| Detail | Information |
| --- | --- |
| Institute | Sinhgad Institute of Lonavala |
| Training | Python Programming |
| Duration | 7 days |
| Dates | 2 September 2026 to 8 September 2026 |
| Organized by | Training and Placement Office (TPO) |
| TPO Professor | Prof. Mayur Raut Sir |
| Training partner | Rubicon Skill Development |
| Trainer | Yogesh Gend Sir |
| Trainer LinkedIn | [Yogesh Gend](https://www.linkedin.com/in/yogesh-gend/) |

The training combined Python fundamentals, object-oriented programming, file handling, exception handling, data analysis, databases, Django web development, Git, and coding standards.

## Additional Concepts Learned

The training also covered concepts that are not included as separate programs in this repository:

### Python Background and Development

- Python history, Guido van Rossum, and the first public release.
- Python features including readability, interpreted execution, dynamic typing, portability, and its library ecosystem.
- Python applications in web development, automation, data science, artificial intelligence, machine learning, scripting, and cybersecurity.
- Python installation, editors, terminals, interpreter execution, comments, naming rules, keywords, and code indentation.
- Pre-assessment concepts such as programming, programming languages, variables, data types, conditions, loops, and functions.

### Problem-Solving Practice

- Predicting program output before execution.
- Modifying values and statements to observe program behavior.
- Homework and classroom exercises for area calculation, simple interest, palindrome checking, vowel counting, word counting, and student records.

### Django Concepts

- Web development fundamentals and the request-response flow.
- Django installation, project creation, app creation, settings, middleware, static files, and templates.
- MVT architecture and its relationship to the broader MVC pattern.
- Django ORM concepts, querysets, filtering, creating, updating, and deleting model records.
- Database migrations, development-server workflow, and application configuration.

### Git and Version Control

- Git versus GitHub and the purpose of distributed version control.
- Repositories, working files, staging, commits, branches, remotes, and project history.
- `git init`, `git status`, `git add`, `git commit`, `git log`, `git branch`, `git switch`, `git merge`, `git clone`, `git fetch`, `git pull`, and `git push`.
- `.gitignore`, remote repositories, feature branches, merge conflicts, and collaboration workflow.

### Professional Coding Practices

- Readable naming, consistent formatting, indentation, comments, and modular program structure.
- Code review, testing, debugging, error diagnosis, and documentation.
- Avoiding secrets, passwords, virtual environments, generated files, and unnecessary database files in version control.
- Writing maintainable code that is easier to understand, test, and extend.

## Repository Structure

| Folder | Topics Covered |
| --- | --- |
| `day_01_fundamentals` | Python syntax, variables, data types, input/output, operators, conditions, loops, functions, and strings |
| `day_02_data_structures` | Lists, tuples, sets, dictionaries, collection operations, and the Student Marks System mini-project |
| `day_03_oop` | Classes, objects, constructors, methods, inheritance, method overriding, polymorphism, encapsulation, rectangles, and student records |
| `day_04_files_modules_exceptions` | File handling, modules/imports, reusable functions, and exception handling practice |
| `day_05_libraries` | NumPy arrays, Pandas Series/DataFrames, Matplotlib charts, and basic data analysis |
| `day_06_sql_django_intro` | SQL statements, parameterized queries, SQLite CRUD operations, and Django introduction concepts |
| `day_07_django_git` | `college_portal` Django project, student records, marks, highest-score dashboard, Git, and GitHub/version control |

## Programs and Projects

### Python Fundamentals

The fundamentals exercises include Hello World, student details, arithmetic operations, area calculation, number comparisons, pass/fail and grade logic, loops, multiplication tables, string operations, and reusable functions.

### Data Structures and Mini-Project

The collection exercises demonstrate list manipulation, list calculations, tuple access, set union/intersection/difference, dictionary updates and iteration, and removal of duplicate values. The `miniproject1.py` program implements a Student Marks System with grades, highest-scorer reporting, and class-average calculation.

### Object-Oriented Programming

The OOP examples demonstrate classes and objects, constructors, multiple objects, inheritance, method overriding, polymorphism, encapsulation, a `Rectangle` class, and student records.

### Files, Modules, and Exceptions

The Day 4 examples demonstrate persistent text storage, reading and writing modes, appending, file metadata, reusable modules, imports, counting file lines, common runtime errors, safe division, validation, raised errors, and custom exception classes.

### Python Libraries

The Day 5 programs use:

- **NumPy** for arrays, indexing, slicing, reshaping, arithmetic, and statistics.
- **Pandas** for Series, DataFrames, CSV files, filtering, sorting, calculated columns, and grouping.
- **Matplotlib** for line, bar, scatter, histogram, pie, and multi-chart visualizations.

The library practice includes array dimensions, shape, size, data types, indexing, slicing, basic array operations, Series, DataFrames, indexing, and basic data handling and analysis.

### SQL and CRUD

The Day 6 programs demonstrate SQL and SQLite table creation, `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`, aggregate functions, parameterized queries, inserts, updates, deletes, transactions, and CRUD workflows.

The integrated analysis program combines SQLite, Pandas, and Matplotlib to calculate and visualize average marks by department.

Day 6 also introduced Django installation, the MVT architecture, Django files, and project structure before the complete project work on Day 7.

### Django, College Portal, and Version Control

The Day 7 `college_portal` project is a Django student portal containing:

- A Django project named `studentportal`
- A `students` application
- Student models and database migrations
- URL routing and views
- HTML templates for home, student listing, search, add, edit, and high-scorer pages
- Admin and test modules
- SQLite database support

The project practices student details, marks, student records, and a highest-score dashboard. Day 7 also covered Git, GitHub, repositories, staging, commits, branches, remotes, and version-control workflow.

## Setup

Create or activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the Django project:

```powershell
cd day_07_django_git\college_portal
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.

## Learning Outcome

This training established a practical foundation in Python Programming, moving from basic syntax and problem solving to object-oriented design, data analysis, database operations, web application development, Git workflow, and professional coding practices.