#! /usr/bin/python3

import subprocess
# first, we must go through and make a disctionary of all the defined symbols
symbol_outputs = subprocess.run(['nm', '--defined-only', './prof_example'], stdout=subprocess.PIPE).stdout.decode('utf-8').split("\n")

symbols = {}

for symbol_output in symbol_outputs:
    symbol = symbol_output.split(" ")
    if(len(symbol)!=3): continue
    # we must trim our addresses and remove beginning 0s
    #print(symbol[0])
    address = str(hex(int(symbol[0], 16)))
    name = symbol[2]
    symbols[address] = name


# now that we have our dictionary, lets run our program and fix its output
program_output = subprocess.run(['./prof_example'], stdout=subprocess.PIPE).stdout.decode('utf-8')

#simply iterate over our dictionary and replace everything in our output that is found in our dicitonary
for address in symbols:
    replacement = symbols[address] + " (" + address + ")"
    program_output = program_output.replace(address, replacement)

print(program_output)
