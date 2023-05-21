class Romantointeger:
    roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    total = 0
    def convertRomanToInteger (self,romanstr:str) :
        for i in range(len(romanstr)):
            if i > 0 and self.roman[romanstr[i]] > self.roman[romanstr[i-1]]:
               self.total += self.roman[romanstr[i]] - 2 *self.roman[romanstr[i-1]]
            else:
               self.total += self.roman[romanstr[i]]
        return self.total
obj = Romantointeger()
romanstr = input("Enter Roman string \n")
print("Final Output ", obj.convertRomanToInteger(romanstr))


