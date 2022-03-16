# Using random module
import random





# Main Function
def generate_pass(length):

    # To save pass chars as list
    result_list = []
    #To save pass result as STR
    result_string = ""


    # To convert length variable to intiger
    length =int(length)

    # looping for choose a char and save 
    for i in range(length):

        # Password must contains these chars
        chars = [
                '0','1','2','3','4','5','6','7','8','9',
                '!','@','#','$','%','^','&','*','(',')','-','_','=','+',
                'a','b','c','d','e','f','g','h','i','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R',
                'S','T','U','V','W','X','Y','Z',
                ]

        # shuflle the chars list
        random.shuffle(chars)

        # select a list char
        x_chance = random.choice(chars)
        # save selected char to list
        result_list.append(x_chance)

    
    # convert generated pass list chars to string
    for x in result_list:
        result_string += x

    # return result value as string
    return(result_string)


# using generate password function - arguments is the length of password that you need
print(generate_pass(20))
