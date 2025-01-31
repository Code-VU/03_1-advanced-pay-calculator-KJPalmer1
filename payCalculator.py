def calculatePay():
    # This first line is provided for you
    hrs = input("Enter Hours:")
    try: 
        hrs = int(hrs)
    except:
        print('Error, please enter numeric input')
        quit()

    rate = input("Enter Rate:")
    try:
        rate = int(rate)
    except:
        print('Error, please enter numeric input')
        quit()
        

    total = hrs * rate
    if hrs > 40:
        base_hrs = 40
        OT_hrs = hrs - 40
        OT_rate = rate * 1.5
        total = (base_hrs * rate) + (OT_hrs * OT_rate)

    print("Pay:", total)
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
