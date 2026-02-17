def stationary(*item,**prices):
    print("items are ",item)
    print("prices are",prices)
    total =0
    for i in item:
        if i in prices:
            total = total +prices[i]
        else:
            print(item,"is not available")
    return f"total amount is {total}"
stationary("pen","pencil","bag","pad",pen=10,pencil=5,bag=400,pad=30)