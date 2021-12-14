How this works (part b, part a is the brute force stupid version), described with shitty grammar, but I think it is reasonably understandable:

We do not really need to know the string itself, the only thing we need to keep track of is the pairs of letters in the string.
Hence, we start by generating the pairs in the seed string. Then we iterate over the list of pairs and replace the pairs in it according to the rules.
Each pair in a rule will generate two new pairs e.g. AB->C generates AC, CB. We store the pairs in a dict which maps pair name ("AB") to the number of occurences.

This is done 40 times and is done in more or less linear memory space since we count the occurences instead of storing the actual string.
Then, we count the letters in the pairs, multiply with the number of pairs, done, we have a list with letters and a count per letter equal to twice the number of that letter in the string. Except for the ones on the outside of the seed - those letters are only present ONCE (for the boundary instance of the letter), hence, we need to add one to those letters.

Divide by two, sort, subtract, done.
