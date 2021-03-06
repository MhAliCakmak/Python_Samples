from random import randint #Bize yarayanı alalım
points=0 #oyunumuz kuralı su 5 defa da sayiyi tahmin edecez her dogru 20 puan size kazandiracak yanlış puan ise -10
counts=1
def selection():
    print(30*"-")
    global counts
    counts=0
    global points    
    choose=int(input(30*"-"+"\n1)My points\n2)Game"))
    if choose==1:
        print(f"MY POİNT:{points} ")
        alt=input('geri cikmak icin b ye tiklayin')
        if alt=="b":
            selection()
    elif choose==2:
        number()
        print("-"*30)

def number():
    print("-"*30)
    global counts
    global points
    result=randint(1,100)
    for i in range(0,10):
        choose=int(input("Enter number"))
        if result==choose:
            points+=20
            print(f"congurlations, your points{points}")
            selection()
        elif choose<result:
            print("UP")
            counts+=1
            if counts==10:
                points-=10
                selection()
        elif choose>result:
            print("DOWN")
            counts+=1
            if counts==10:
                points-=10
                selection()
selection()

