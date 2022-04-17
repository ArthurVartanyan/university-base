import psycopg2

connection = psycopg2.connect(user="postgres", password="a7bgkKsr",
                              host="127.0.0.1", port="5432", database="student-base")
cursor = connection.cursor()


def add_student(name, lastname, patronymic, pass_seria, pass_number, faculty, student_number):
    try:
        print("PostgreSQL server information")
        cursor.execute("SELECT version();")

        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        query = "insert into " \
                "public.student(name, surname, patronymic, pass_seria, pass_number, faculty_id, student_number) " + \
                "values(" + '\'' + name + '\'' + ", " + '\'' + lastname + '\'' + ", " + '\'' + patronymic + '\'' + ", " + '\'' + pass_seria + '\'' + \
                ", " + '\'' + pass_number + '\'' + ", " + faculty + ", " + '\'' + student_number + '\''");"
        cursor.execute(query)
        connection.commit()
    except (Exception) as error:
        print("Error while connecting to PostgreSQL", error)
