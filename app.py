from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository
from lib.application import Application


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/student_directory_2.sql")

# Retrieve all artists
repository = CohortRepository(connection)
cohort_id = 1

cohort = repository.find_with_students(cohort_id)

if cohort:
    print(f"Cohort: {cohort.name}")
    print("Students:")
    for student in cohort.students:
        print(f"- {student.name}")
    

connection.close()

if __name__ == '__main__':
    app = Application()
    app.run()
