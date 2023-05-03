high, low = [], []
se1=[1,2,3,4,5]             
se2=[2,4,4,5,5]

[high.append(x) if x==y  else low.append(x) for x,y in zip(se1,se2)] # if else in generator expression

print(high,low)