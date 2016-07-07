import subprocess
import os
this_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(this_dir)
print os.listdir(this_dir)
p = subprocess.Popen(['soffice', '-headless', '-nofirststartwizard', '-accept=socket,host=localhost,port=2002;urp;'])
