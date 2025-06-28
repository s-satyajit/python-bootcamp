def convFar(c):
    return print((9/5)*c+32)
c = input("Enter the temperature in cel")
c = int(c)
convFar(c)

def convHour(m, s):
    return print(int(m)/60 + int(s)/3600)

m = input("Enter time in min")
s = input("Enter time in sec")
convHour(m, s)