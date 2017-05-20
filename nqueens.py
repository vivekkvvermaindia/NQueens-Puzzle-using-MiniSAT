import sys,string,os,linecache

n = input("Enter n: ")
if n < 4:
  print "UNSATISFIABLE"
  exit()
count=0
filen="qin.cnf"
filem="qout.txt"
file1= open(filen,"w");
file2= open(filem,"w");

#generator rule
for i in range(0,n):
 str0='';
 for j in range(1,n+1):
  number=str(j+n*i);
  str0=str0+number+" "
 str0=str0+" 0\n"
 file1.write(str0);
 count+=1

#constraints on rows
for i in range(0,n):
 for j in range(1,n):
   number=j+n*i;
   for l in range(1,n-j+1):
    str0="-"+str(number)+" -"+str(number+l)+" 0\n"
    file1.write(str0);
    count+=1

#constraints on columns
for j in range(1,n+1):
 for i in range(0,n):
   number=j+n*i;
   for l in range(1,n-i):
    str0="-"+str(number)+" -"+str(number+n*l)+" 0\n"
    file1.write(str0);
    count+=1 

#constraints on l->r diagonal
# part 1, upper bound triangle
for i in range(0,n-1):
 for j in range(i,n-1):
  number=j+1+n*i;
  for l in range(1,n-j):
    str0="-"+str(number)+" -"+str(number+l*(n+1))+" 0\n"
    file1.write(str0);
    count+=1 

# part 2, lower bound triangle
for i in range(0,n-1):
 for j in range(0,i):
  number=j+1+n*i;
  for l in range(1,n-i):
   str0="-"+str(number)+" -"+str(number+l*(n+1))+" 0\n"
   file1.write(str0);
   count+=1

#constraints on r->l diagonal
# part 1, upper bound triangle
for i in range(0,n):
 for j in range(0,n-i):
  number=j+1+n*i;
  for l in range(1,j+1):
   str0="-"+str(number)+" -"+str(number+l*(n-1))+" 0\n"
   file1.write(str0);
   count+=1

# part 2, lower bound triangle
for i in range(0,n):
 for j in range(n-i,n):
  number=j+1+n*i;
  if (number != n*n ):
   for l in range(1,n-i):
    str0="-"+str(number)+" -"+str(number+l*(n-1))+" 0\n"
    file1.write(str0);
    count+=1

file1.close()
file2.close()
f = open('qin.cnf','r')
temp = f.read()
f.close()

f = open('qin.cnf', 'w')
f.write("p cnf "+str(n*n) +" "+ str(count) + "\n")

f.write(temp)
f.close()

exe="./minisat "+ filen + " " + filem

os.system(exe)

line = linecache.getline("qout.txt",2)
line = map(int ,line.split(' '))
for i in range(len(line)-1):
	if int(line[i]) < 0:
		line[i] = 0
	else:
		line[i] = 1
def chunks(l, n):
    for i in range(0, len(l)-1, n):
        yield l[i:i + n]
l = (list(chunks(line, n)))
file3 = open("ans.txt", 'w')
for i in range(len(l)):
	file3.write(str(l[i]))
	file3.write("\n")


