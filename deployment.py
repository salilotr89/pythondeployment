import sys
import subprocess
import deploymentconfig
from changedirectory import CD

# enter the directory like this:
print(deploymentconfig.projectDirectory)


def execute_command(command):
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
    p.wait()
    print(p.returncode)
    if p.returncode == 0:
        pass


def change_dir_and_exec_cmd(directory, command):
    with CD(directory):
        execute_command(command)

change_dir_and_exec_cmd(deploymentconfig.projectDirectory, "git pull origin master ")
change_dir_and_exec_cmd(deploymentconfig.projectDirectory, "mvn clean install -DskipTests")
change_dir_and_exec_cmd(deploymentconfig.tomcatBin, "sh shutdown.sh")
change_dir_and_exec_cmd(deploymentconfig.tomcatWebapps, "cp ~/kycengine/target/PrimeID.war .")
change_dir_and_exec_cmd(deploymentconfig.tomcatBin, "sh startup.sh")
sys.exit()
