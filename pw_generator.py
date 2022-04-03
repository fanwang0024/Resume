def pw_main():
    companyName = input("What the company's name? (Start with Capital letter)  ")
    
    position = input("What's the postion that you are applying for? (Start with Capital letter)  ")

    prt1="I’m writing this letter to express my desire of working at the company " + companyName
    prt2=" as a "+ position + "."
    s = prt1+prt2
   
    with open('coverletter_p1.txt','a+') as file:
        appender=file.writelines(s)

pw_main()
