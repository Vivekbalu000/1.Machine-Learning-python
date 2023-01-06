class multipleFunctions():
    def Subfields():
        list1=["Subfields()Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural      Language Processing"]
        for temp in list1:
                print(temp)
                
    def OddEven():
        num=int(input("Enter a number: "))
        if (num%2)==0:
            print(("{0} is Even number").format(num))
        else:
            print(("{0} is Odd number").format(num))
            
    def Eligibile():
        Gender=input("Your Gender:")
        age=int(input("Your age:"))
        if (age<=18):
            print("NOT ELIGIBILE")
        else:
            print("ELIGIBILE")
            
    def Percentage():
        mar1=int(input("Subject1="))
        mar2=int(input("Subject2="))
        mar3=int(input("Subject3="))
        mar4=int(input("Subject4="))
        mar5=int(input("Subject5="))
        add=(mar1+mar2+mar3+mar4+mar5)
        print("Total:",add)
        print("Precentage:",add/5)
        
    def triangle():
        mes1=int(input("Height:"))
        mes2=int(input("Breadth:"))
        print("Area formula:(Height*Breadth)/2")
        area=(mes1*mes2)/2
        print("Area of Triange:",area)
        mes3=int(input("Height1:"))
        mes4=int(input("Height2:"))
        mes5=int(input("Breadth:"))
        print("Perimeter formula:Height1+Height2+Breadth")
        perimeter=(mes3+mes4+mes5)
        print("Perimeter of Triangle:",perimeter)