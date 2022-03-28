#display system information
print ("system information:")

#import module
from multiprocessing.sharedctypes import Value
import platform

#display operating system
print ('operating system:',platform.system())
#display system information
print ('system host:',platform.node())
#display operating system version
print('os version:',platform.version())
#display machine type
print ('machine type:',platform.machine())
#display processor type
print ('Processor type:',platform.processor())

#importing os module
import os
#importing shutil & math Module
import shutil,math
#display statement as disk space information
print("disk space information")
#path
path="/home/"
#using shutil.disk_usage ()method
disk_usage = shutil.disk_usage(path)
#print result
print(disk_usage)

#printing datas from disk_usage tuple
a=used= disk_usage[1]
b=total=disk_usage[0]
c=free=disk_usage[2]
#printing used disk%
print('used disk :',int((a/b)*100),'%')
#printing available disk percentage
print ('available disk :',int((c/b)*100),'%')
#printing alerting statement 
if ((a/b)*100)>=90:
    print("disk running space is low")
else:
    print ("disk running space is safe" )

#imprt subprcess
import subprocess
#subprocess and shell commands
df = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
output = df.stdout.decode()
#listing the filesystem
print(output)

usage=dict()
threshold =int(input("enter threshold value"))
for line in output.strip().split('\n')[0:]:  #getting the lines with actual data
    fields=line.split()#cbreak line into fields
    usage[fields[5]]=fields[4]#mapping usage with mount

usage.pop("Mounted")#removing header from the dictionary

file_systems = {k:v for k,v in usage.items() if int(v.strip('%'))>threshold}
print("files systems beyond threshold limit:",threshold)
print(file_systems)



