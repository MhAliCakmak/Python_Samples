result=int(input("please enter number :")) #ingilizce kullanmaya gayret gösterelim☺
is_prime=True#prime ing de asal demek
for i in range(2,result):
    if result ==2:
        print("sayi asal")
        break
    elif result%i==0:
        print("this number isn't prime")
        is_prime=False
        break
if is_prime:
    print("this number is prime")


