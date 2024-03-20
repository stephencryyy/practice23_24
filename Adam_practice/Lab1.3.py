def check(number):
    if number > 3:
        for i in range(2,number+1):
            if i < number:
                if number%i==0:
                    return False
            elif i >= number:
                return True
    else:
        return True

def main():
    number = int(input("Enter a number: "))
    print(check(number))

if __name__ == '__main__':
    main()
