import subprocess

data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
profiles=[i.split(":")[1][1:-1] for i in data if "All user profile" in i]
for i in profiles:
    res= subprocess.check_output(['netsh','wlan','show','profile' , i ,
'key=clear']).decode('utf-8').split('\n')
    res=[b.split(":")[1][1:-1] for b in res if "key Content" in b]
    try:
        print ("{:<30}| {:<}".format(i,res[0]))
    except IndexError:
        print ("{:<30}| {:<}".format(i,""))