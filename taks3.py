class BMICalculator:
    def __init__(self, weight, height):
        self._weight = weight
        self._height = height
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def height(self):
        return self._height
    
    def BMI_Value(self):
        bmi = self._weight / (self._height ** 2)
        return bmi

# Contoh penggunaan
if __name__ == "__main__":
    weight = 70  #  kg
    height = 1.75  # m

    person = BMICalculator(weight, height)
    print("Menghitung BMI")
    print("Weight:", person.weight, "kg")
    print("Height:", person.height, "m")
    print("BMI:", person.BMI_Value())
