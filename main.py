def main():
    original_str = "Python Programming"

    # Extract "Python" from original string with index slicing
    sub1 = original_str[:6]
    # Extract the first substring 'Python'

    # Extract "Programming" from original string with index slicing
    sub2 = original_str[7:]
    # Extract the second substring 'Programing'        
    
    # Using the string concatenation('+') merge the substrings sub1 and sub2 save it as "merged_str"
    merged_str = sub1 + sub2

    print(sub2)
    print(sub1)
    print(merged_str)

    #########################################
    # Do not delete the return statement
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
