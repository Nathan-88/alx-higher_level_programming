#A function that prints a string in uppercase
def uppercase(str):
        for i in str:
                    if ord(i) >= 97 and ord(i) <= 122:
                                    i = chr(ord(i)-32)
                                            print("{}".format(i), end="")
                                                print("\n")


                                                uppercase("best")
                                                uppercase("Best School 98 Battery street")
