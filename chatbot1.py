# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:41:25 2019

@author: hp
"""

import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("custom.aiml")


# Press CTRL-C to break this loop
while True:
    userinput = input("Enter your message >> ")
    output = kernel.respond(userinput)
    print(output)