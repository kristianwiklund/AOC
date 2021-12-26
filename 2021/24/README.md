How I did it:

Split the compiled code into functions.
Stagger those in a set of nested loops that generate the number to be tested. Reuse the previous values for efficiency

Check what the input limitations are that will satisfy a z=0 at the end - start with the final function, find the restrictions, continue with the next (example in the 25b.py file)
