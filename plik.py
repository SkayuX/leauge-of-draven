import subprocess
import sys

call = 'TASKLIST /FI "imagename eq LeagueClient.exe"'

output = subprocess.check_output(call, shell=True).decode(encoding="437")
    # check in last line for process name
last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
cos = last_line.lower().startswith("LeagueClient.exe".lower())

print(cos)

if output:
    print("ta")
else:
    print("nie")