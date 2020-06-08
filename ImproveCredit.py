def improvecredit():
    MyBalance = float(input('Your current Credit Limit:'))
    mycurrentbalance= float(input( 'Your present balance:'))
    mygoodcreditamt = int(MyBalance * .3000)
    whatisneeded = round(mycurrentbalance - mygoodcreditamt)
    print ('Your required balance to improve your credit will be $', mygoodcreditamt)
    print ('You need to pay', '$', whatisneeded, 'to improve your credit')
improvecredit()