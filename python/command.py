from subprocess import call

now = call(['ls','-1','/tmp'])
print now

	
import subprocess
p = subprocess.Popen(["ping", "-c", "2", "www.cyberciti.biz"], stdout=subprocess.PIPE)
output, err = p.communicate()
print  output
