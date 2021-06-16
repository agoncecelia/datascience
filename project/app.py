import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="datasciencebootcamp",
    user="datasciencebootcamp",
    password="datasciencebootcamp",
    port=5432
)

def return_users(return_average, greater = 6):
  cursor = conn.cursor()
  cursor.execute("select * from users where average > '%d';" % greater)
  records = cursor.fetchall()
  if return_average == False:
    for row in records:
      print("{},  {},  {},  {}, {:%Y-%m-%d %H:%M}".format(row[0], row[1], row[2], row[3], row[4]))
    cursor.close()
  return records

def return_class_average():
  rows = return_users(True)
  sum = 0
  for row in rows:
    sum += row[3]
  average = sum / len(rows)
  print("Class average is: {:.2f}".format(average))

def insert_users(name, lastname, average, who):
  if average < 6:
    print("This average is not allowed.")
    return
  cursor = conn.cursor()
  sql = 'insert into users (firstname, lastname, average, who) values (%s, %s, %s, %s)'
  val = (name, lastname, average, who)
  cursor.execute(sql, val)
  conn.commit()
  cursor.close()
  print("New user added successfully.")

def delete_user(id):
  cursor = conn.cursor()
  sql = "delete from users where user_id = '%d'" % (id)
  cursor.execute(sql)
  conn.commit()
  cursor.close()
  print("User deleted successfully.")

def print_help():
  print("Press q to exit, press a to add student, press l to list students, press d to delete student, press h for help, avg for class average, gavg for finding students with greater average, cd will give class details")

def number_of_top_students():
  cursor = conn.cursor()
  cursor.execute("select * from users where average = 10;")
  records = cursor.fetchall()
  print("We have {} top students.".format(len(records)))
  for row in records:
    print("{},  {},  {},  {}, {:%Y-%m-%d %H:%M}".format(row[0], row[1], row[2], row[3], row[4]))


inp = ''
who = input("Please provide your name: ")
print_help()
while inp != 'q':
  inp = input("Please provide your next command: ")
  if inp == 'a':
    firstname = input("Please provide firstname: ")
    lastname = input("Please provide lastname: ")
    average = float(input("Please provide average: "))
    insert_users(firstname, lastname, average, who)
  elif inp == 'l':
    return_users(False)
  elif inp == 'd':
    id = input("Please provide user id to delete: ")
    delete_user(int(id))
  elif inp == 'avg':
    return_class_average()
  elif inp == 'h':
    print_help()
  elif inp == 'cd':
    number_of_top_students()
  elif inp == 'gavg':
    val = float(input("Please provide average for greater than: "))
    return_users(False, val)
  else:
    print("Command not known: ", inp)


