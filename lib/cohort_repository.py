from student import Student
from cohort import Cohort

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def find_with_students(self, cohort_id):
        query = """
        SELECT stodents.id, students.name, students.cohort_id
        FROM students
        JOIN cohorts ON students.cohort_id = cohorts.id
        WHERE cohorts.id = %s
        """
        cursor = self._connection.cursor()
        cursor.execute(query, [cohort_id])
        rows = cursor.fetchall()
        cursor.close()
        
        cohort = None
        if rows:
            cohort = Cohort(rows[0]['cohort_id'], rows[0]['cohort_name'])
            for row in rows:
                student = Student(row['id'], row['name'], row['cohort_id'])
                cohort.students.append(student)
                
        return cohort