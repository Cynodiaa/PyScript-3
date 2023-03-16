tax = 5
studentDiscount = 15
professorDiscountLow = 5
professorDiscountHigh = 10

studentType = 1
professorType = 0


def start():
    purchase = input("Please enter the amount of purchase ")

    if not purchase.isdecimal():
        return print("Given purchase is not an decimal.")
    firstPurchase = float(purchase)
    discountAmount: float
    discountedPurchase: float
    saleTax: float
    lastPrice: float

    customerType = input(
        "Please enter the customer type (0) for professor - (1) for student ")

    if not customerType.isdigit():
        return print("Given customer type should be 0 or 1.")
    customerInt = int(customerType)
    if customerInt != studentType and customerInt != professorType:
        return print("Given customer type should be 0 or 1.")

    if customerInt == professorType:
        if firstPurchase < 100:
            discountAmount = firstPurchase * professorDiscountLow/100
            discountedPurchase = firstPurchase - discountAmount
        else:
            discountAmount = firstPurchase * professorDiscountHigh/100
            discountedPurchase = firstPurchase - discountAmount
    else:
        discountAmount = firstPurchase * studentDiscount/100
        discountedPurchase = firstPurchase - discountAmount

    saleTax = discountedPurchase * tax/100
    lastPrice = discountedPurchase + saleTax

    print(f"Total purchase is {firstPurchase}")
    print(f"Amount of discount is {discountAmount}")
    print(f"Discounted total is {discountedPurchase}")
    print(f"Sale tax is {saleTax}")
    print(f"Total amount of payment is {lastPrice}")


start()