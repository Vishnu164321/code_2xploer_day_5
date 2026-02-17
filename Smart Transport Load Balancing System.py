weights=[4,80,70,-2,30,55,0]
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid=[]
valid=0
aff_count=0
for weight in weights:
    if weight<0:
        invalid.append(weight)
    elif weight>=0 and weight<=5:
        very_light.append(weight)
        valid+=1
    elif weight>=6 and weight<=25:
        normal_load.append(weight)
        valid+=1
    elif weight>=26 and weight<=60:
        heavy_load.append(weight)
        valid+=1
    else:
        overload.append(weight)
        valid+=1

name="Vishnu Mattakoyya"
L=len(name.replace(" ", ""))
PLI=L%3
if PLI==0:
    for item in overload:
        invalid.append(item)
        aff_count+=1
    overload=[]
elif PLI==1:
        aff_count=len(very_light)
        very_light=[]
elif PLI==2:
    aff_count=len(very_light)+len(overload)
    very_light=[]
    overload=[]

print("Final plan is :")
print("Very light:",very_light)
print("Normal load:",normal_load)
print("Heavy load:",heavy_load)
print("Overload:",overload)
print("invalid:",invalid)


print("Valid Weights:",valid)
print("Affected items due to PLI:",aff_count)


