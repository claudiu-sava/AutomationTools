import subprocess
import os

try:
  i = open("cont.txt", "x")
except:
  pass

try:
  i = open("pass.txt", "x")
except:
  pass

try:
  i = open("good.txt", "x")
except:
  pass

try:
  i = open("good.txt", "x")
except:
  pass

veracryptPath = r"C:\Program Files\VeraCrypt\VeraCrypt.exe"
# -----------------------
start = 0
passwLines = 0
containers = 0
goodValue = 0
badValue = 0

with open("pass.txt", "r") as lines:
  for line in lines:
    passwLines = passwLines + 1
lines.close()

with open("cont.txt", "r") as lines:
  for line in lines:
    containers = containers + 1
lines.close()

if containers == passwLines:
  print("Total login: %s" % containers)
  while start < containers:
    with open("pass.txt", "r") as fp:
      for i, line in enumerate(fp):
        if i == start:
          password = line.rstrip()
    fp.close()

    with open("cont.txt", "r") as fp:
      for i, line in enumerate(fp):
        if i == start:
          volume = line.rstrip()
    fp.close()
    print("%s:%s" % (volume, password))
    mounter = veracryptPath + " /volume " + volume + " /letter S /password " + password + " /quit /silent"
    subprocess.call(mounter)
    if os.path.exists("S:\\"):
      print("%s works!" % volume)
      with open("good.txt", "a") as good:
        good.write(volume + "\n")
        goodValue = goodValue + 1
      good.close()
      dmounter = veracryptPath + " /dismount S /quit /silent /force"
      subprocess.call(dmounter)
    else:
      print("Error %s" % volume)
      with open("bad.txt","a") as bad:
        bad.write(volume + "\n")
        badValue = badValue + 1
      bad.close()
    start = start + 1
  print("From %s logins: %s were good and %s were bad" % (containers, goodValue, badValue))
exit()