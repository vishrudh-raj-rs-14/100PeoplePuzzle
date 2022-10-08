#Creating a list of [1,2,3,...,98,99,100]
people = [i for i in range(1,101)]; 

killer = False;
i=0;
while (len(people)>1):
    if killer:
        # Killing the person
        del people[i];
    else:
        # If there are only 5 people 
        # and i is at 4 then at next 
        # iteration i should start from 0
        i=(i+1)%len(people) 
    
    killer = not killer;
print(people[0])