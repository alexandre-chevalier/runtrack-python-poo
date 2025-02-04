class Student:
    def __init__(self, nom, prenom, idStud):
        self.__nom = nom 
        self.__prenom = prenom
        self.__id_student = idStud
        self.__credit = 0
        self.__level = self._studentEval(self.get_credit())

    def get_nom(self):
        return self.__nom
    
    def get_Prenom(self):
        return self.__prenom
    
    def get_id(self):
        return self.__id_student
    
    def get_credit(self):
        return self.__credit
    
    def add_credits(self, nombre):
        if nombre <=0:
            print("veuillez entrez un nombre superieur a 0")
        elif nombre > 0:
            self.__credit = self.__credit + nombre
    
    def _studentEval(self, credit):
        avis = ""
        if credit >=90:
            avis = "excellent"
        elif credit >=80 and credit < 90:
            avis = "tres bien"
        elif credit >=70 and credit < 80:
            avis = "Bien"
        elif credit >=60 and credit < 70:
            avis = "insuffisant"
        return avis
        
    def student_info(self, nom, prenom, id,niveau):
        print(f"Nom :{nom} ")
        print(f"prenom : {prenom} ")
        print(f"id : {id} ")
        print(f"Niveau : {niveau}")

student = Student("bros", "mario", 175)

print(f"le nombre de credits de {student.get_Prenom()} {student.get_nom()} est de {student.get_credit()}")

student.add_credits(-12)
student.add_credits(50)
student.add_credits(100)
student.add_credits(75)

print(f"le nombre de credits de {student.get_Prenom()} {student.get_nom()} est de {student.get_credit()}")

student.student_info(student.get_nom(), student.get_Prenom(), student.get_id(), student._studentEval(student.get_credit()))