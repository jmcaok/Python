def main():
    # accept a word as input
    word = input('please enter a word.:\t')
    # call the count() function on the word
    cou = count(word) 
    # print the number of vowels
    print(f'number of vowels is {cou}')
    return 0
def count(word):
    counter = 0
    # count number of vowels in word here
    liss = ['a', 'e', 'i', 'o', 'u']
    # you can use a for loop or a while loop
    # if you use a for loop, you can say: for letter in word:
    for i in range():
    # this will loop through the word tracking each letter until the end of the word
    # you can then compare each letter to a list of vowels using the in operator 
    # if you use a while loop, you will have to use a counter which you increase after every
    # iteration until the end of the word
    # you can get the length of the word using len(word)
    return #return the number of vowels in the word

if __name__ == "__main__":
    main()