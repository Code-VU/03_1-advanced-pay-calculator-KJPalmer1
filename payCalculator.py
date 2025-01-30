def calculatePay():
    # This first line is provided for you
    hrs = int(input("Enter Hours:"))
    rate = int(input("Enter Rate:"))

    total = hrs * rate
    if hrs > 40:
        base_hrs = 40
        OT_hrs = hrs - 40
        OT_rate = 10 * 1.5
        total = (base_hrs * rate) + (OT_hrs * OT_rate)

    print(total)
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
