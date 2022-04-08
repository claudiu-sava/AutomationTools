import subprocess
import os
import sqlite3

try:
  i = open("good.txt", "x")
except:
  pass

try:
  i = open("bad.txt", "x")
except:
  pass


conn = sqlite3.connect("A:\database.db")
cursor = conn.cursor()

veracryptPath = r"C:\Program Files\VeraCrypt\VeraCrypt.exe"

# -----------------------

start = 0
passwLines = 0
goodValue = 0
badValue = 0

choice = input("Enter the location or leave empty to scan everything :>> ")

containerList = str(cursor.execute("SELECT Name FROM Containers WHERE Place like '%" + choice + "%' ORDER BY Name ASC").fetchall()).lower().replace("'", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(",","").split(" ")
totalContainerNumber = len(containerList)

passwordList = str(cursor.execute("SELECT Password FROM Containers WHERE Place like '%" + choice + "%' ORDER BY Name ASC").fetchall()).replace("'", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(",","").split(" ")
totalPasswordNumber = len(passwordList)

if totalContainerNumber == totalPasswordNumber:
  print("%s containers loaded" % totalContainerNumber)
  while start < totalContainerNumber:
    print("%s:%s" % (containerList[start], passwordList[start]))
    mounter = veracryptPath + " /volume " + containerList[start] + " /letter S /password " + passwordList[start] + " /quit /silent"
    subprocess.call(mounter)
    if os.path.exists("S:\\"):
      print("%s works!" % containerList[start])
      with open("good.txt", "a") as good:
        good.write(containerList[start] + "\n")
        goodValue = goodValue + 1
      good.close()
      dmounter = veracryptPath + " /dismount S /quit /silent /force"
      subprocess.call(dmounter)
    else:
      print("Error %s" % containerList[start])
      with open("bad.txt","a") as bad:
        bad.write(containerList[start] + "\n")
        badValue = badValue + 1
      bad.close()
    start = start + 1
  print("From %s logins: %s were good and %s were bad" % (len(containerList), goodValue, badValue))

exit()