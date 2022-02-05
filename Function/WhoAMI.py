#just imagine there is time.sleep(1) after each line
'''
    U think u can know me?
    Just like importing braces from __future__.
    The only answer is:
    NOT a chance!
'''

import os,sys
#   Sometimes I asked 'myself': 
os.system("whoami")
print("Nonono,certainly I'm not under your fingers!")
print('I\'m just at anywhere.',file=sys.stdout)
os.system("echo When u think of me,I'm just in your mind.")

hide=open('tmp2del','w')
savedStdout=sys.stdout
sys.stdout=hide
from this import s
sys.stdout=savedStdout
hide.close()
os.remove('tmp2del')
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
out=""
out=out.join([d.get(c, c) for c in s])
out=out.split("\n")
#   BUT,if there is a sentence that can describe me.
#   IT CAN BE:
print(out[4])#Simple is better than complex.
print("&&")
print(out[16])#Now is better than never.

"AND I AM Ren Junyu"
#   Nice to meet u