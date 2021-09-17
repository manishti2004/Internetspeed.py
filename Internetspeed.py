import speedtest  

st = speedtest.Speedtest()

option = int(input('''What speed do you want to test in Megabits:  

1) Download Speed  

2) Upload Speed  

Your Choice: '''))

if option == 1:   

    print(st.download())    

elif option == 2:   

    print(st.upload())  

else:  

    print("Please enter the correct choice !")