#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A simple script to act as a crystal ball

import random, time

def crystal_ball():
    answers = ['It is certain.',
               'It is decidedly so.',
               'Without a doubt', 
               'Yes, definately!',
               'You may rely on it.',
               'As I see it, yes.',
               'Most likely.',
               'Outlook good.',
               'Yes!',
               'Signs point to yes.',
               'Reply hazy, try again.',
               'Ask again later.',
               'Better not tell you now.',
               'Cannot predict now.',
               'Concentrate and ask again',
               "Don't count on it.",
               'My reply is no.',
               'My sources say no',
               'Outlook not so good.'
               'Very doubtful.']
    
    time.sleep(random.randint(1,5))
    return random.choice(answers)

def main():
    print crystal_ball()
    return

if __name__ == '__main__':
    main()
