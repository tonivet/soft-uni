electron = int(input())

distributed=[]
i=0

while 0 < electron:

    i+=1
    shell=2*i**2

    if electron >= shell: 
        distributed.append(shell)
        electron -= shell
    else:
        distributed.append(electron)
        electron = 0

print(distributed)