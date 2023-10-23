class Employee:
  name=None
  salary=None
  def show(self):
    print(self.name,self.salary)
name = "Ksyusha"
salary = 15000

Employee.show(name, str(salary))
