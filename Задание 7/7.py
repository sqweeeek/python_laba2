class Employee:
  name=None
  zarplata=None

  def show(self):
    print(self.name,self.zarplata)
    myEmployee=Employee()
    myEmployee.name='Ksyusha'
    myEmployee.zarplata='13000'
    myEmployee.show()
