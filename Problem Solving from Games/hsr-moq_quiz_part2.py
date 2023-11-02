def split_number(num):
    #Checking for double digit number
    if num>=10 and num<100:
        numArray = str(num)
        num1,num2 = int(numArray[0]), int(numArray[1])
        return num1 * num2
    else:
        return num

def split_and_multiply():
    
    #Given numbers based on image
    f_snow = [split_number(58),0]
    ss_bamboo = [split_number(39),14]
    b_peony = [split_number(99), 8]
    sunshine = [split_number(27),4]
    
    #Given choices based on image
    results = [162,42,365]
    
    #Loop given numbers to check if there's only one answer
    for num1 in f_snow:
        for num2 in ss_bamboo:
            for num3 in b_peony:
                for num4 in sunshine:
                    res = num1 + num2 + num3 + num4
                    for result in results:
                        if(result == res):
                            print("Combination found:",num1,num2,num3,num4,"\n Result: ",res)
                            break

split_and_multiply()