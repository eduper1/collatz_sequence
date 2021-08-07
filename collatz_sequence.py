# function for collatz sequence
def collatz_sequence():
    # take an input from the user
    z = int(input("Select a number: "))
    # add the input to the list of sequence
    sequence = [z]
    # check if the input is less than 1
    # if that true return an empty list
    if z < 1:
        return []
    # confirm the input is greater than 1
    while z > 1:
        # check if the input even number
        # if that true divide with 2 and add it to the sequence
        if z % 2 == 0:
            z = z / 2
            print("even z: ", z)
            sequence.append(z)
        # else number is odd and add it to the sequence
        else:
            z = 3 * z + 1
            print("odd z: ", z)
    # Return the list of sequence
    return sequence           
            

print(collatz_sequence())