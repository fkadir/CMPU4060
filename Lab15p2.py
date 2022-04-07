# Week 11 Lab 15 part 2
# Q3
class Gym(object):
    def __init__(self, name='', num_equipment=1, members=[]):
        self.name = name
        self.equipment = []
        for i in range(1, num_equipment + 1):
            self.equipment.append(Equipment(i))
        self.members = members

    def __str__(self):
        result = 'Gym name: ' + self.name + '\n'
        result += '\nEquipment: \n'
        for x in self.equipment:
            result += x.__str__() + '\n'
        result += '\nMembers: \n'
        for y in self.members:
            result += y.__str__() + '\n'
        return result


class Equipment(object):
    def __init__(self, equipment_id, equipment_type='treadmill'):
        self.equipment_id = equipment_id
        self.type = equipment_type

    def __str__(self):
        return '{} with ID: {}'.format(self.type, self.equipment_id)


class GymMember(object):
    def __init__(self, name, DOB, gender, member_id=0):
        self.name = name
        self.DOB = DOB
        self.gender = gender
        self.member_id = member_id

    def __str__(self):
        result = 'Member ' + str(self.member_id) + ': \n'
        result += 'name is ' + self.name + '\n'
        result += 'date of birth is ' + self.DOB + '\n'
        result += 'gender is ' + self.gender + '\n'
        return result


# main
m1 = GymMember('Charlotte', '1-1-1998', 'female', 1)
m2 = GymMember('Charlotte', '1-1-1999', 'female', 2)
m3 = GymMember('Fernanda', '1-1-1995', 'female', 3)
m_list = [m1, m2, m3]
gym = Gym("fefe's gym", 5, m_list)


# print(gym)

# Q4
class Student:
    """
   class to create instance of a student
   """

    POSTGRADUATE = 'Postgraduate'

    def __init__(self, study_type, f_name, l_name):
        self.study_type = study_type
        self.f_name = f_name
        self.l_name = l_name
        self.courses = []
        pass

    def set_courses(self, module):
        self.courses.append(module)

    def get_courses(self):
        return self.courses

    def __str__(self):
        result = 'Student: \n'
        result += 'name: ' + self.f_name + ' ' + self.l_name + '\n'
        result += 'student type: ' + self.study_type + '\n'
        result += 'Course List: ' + str(self.courses)
        return result


class RegistrationData:
    """
   Class to create instance of a student's registration information
   """

    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        self.student = Student(study_type, f_name, l_name)
        self.address = address
        self.fee = registration_fee
        self.ID = s_id
        pass

    def set_student_id_property(self, student_id):
        self.ID = student_id

    def get_student_object(self):
        return self.student

    def display_student_data(self):
        result = RegistrationData.__str__(self)
        print(result)

    def __str__(self):
        result = 'Student data:\n'
        result += 'Name: ' + self.student.f_name + ' ' + self.student.l_name + '\n'
        result += 'Student ID: ' + self.ID + '\n'
        result += 'Address: ' + self.address + '\n'
        result += 'Registration Fee: ' + str(self.fee) + '\n'
        result += 'Study type: ' + self.student.study_type + '\n'
        result += 'Course List: ' + str(self.student.get_courses()) + '\n'
        return result


# MAIN SCOPE - UNCOMMENT IT AND RUN AFTER IMPLEMENTING YOUR SOLUTION
# r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
#                      Student.POSTGRADUATE, "Lucas", "Rizzo")
# r.display_student_data()
# print()
# r.set_student_id_property("C12345")
# r.display_student_data()
# print()
# for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
#     r.get_student_object().set_courses(course)
#
# r.display_student_data()
# print()
# print(r.get_student_object())  # extra to match the __str__ additional function
# print()
# print(RegistrationData.__doc__)
