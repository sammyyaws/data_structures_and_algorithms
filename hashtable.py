class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]
        
    def hashfunction(self,key):
        return sum(ord(c) for c in key)% self.size
    
    def insert(self,key,value):
        index=self.hashfunction(key)
        bucket=self.table[index]
        
        for i,(k,v) in enumerate(bucket):
            if k==key:
                bucket[i]=(key,value)
                return
        bucket.append((key,value))
        
    #getting the value store with it key 
    def get(self,key):
        index=self.hashfunction(key)
        bucket=self.table[index]
        
        for k,v in bucket:
            if k==key:
                return v
        return None
    #deleting an item in the table
    def delete(self,key):
        index=self.hashfunction(key)
        bucket=self.table[index]
        
        for i,(k,v) in enumerate(bucket):
            if k==key:
                del bucket[i]
                return("Deleted item succesfuly")
        return("item not found")
    # display content of table
    
    def display(self):
        for i,bucket in enumerate(self.table):
            print(i,":",bucket)
            
            
students=Hashtable(30)
courses=Hashtable(50)
enrollment=Hashtable(50)


def add_student(student_Id, name):
    if students.get(student_Id) is not None:
        print("Already exists")
    else:
        students.insert(student_Id, {
            "name": name,
            "courses": set()
        })
        print("Student added")
        
        
        
def add_course(course_Id, name, capacity):
    if courses.get(course_Id) is not None:
        print("Course already exists")
    else:
        courses.insert(course_Id, {
            "name": name,
            "capacity": capacity,
            "students": set()
        })
        enrollment.insert(course_Id, set())  # optional
        print("Course added")
    
def enroll(student_Id, course_Id):
    student = students.get(student_Id)
    course = courses.get(course_Id)

    if student is None:
        print("Student not found")
        return

    if course is None:
        print("Course not found")
        return

    # check duplicate
    if course_Id in student["courses"]:
        print("Student already enrolled")
        return

    # check capacity
    if len(course["students"]) >= course["capacity"]:
        print("Course is full")
        return

    # enroll
    student["courses"].add(course_Id)
    course["students"].add(student_Id)

    print("Enrollment successful")