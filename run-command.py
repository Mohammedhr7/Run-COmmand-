import subprocess

while True:
    try:
       command = input("Please enter system command >> >> ")
       if command.lower() == "exit":
        break
       if command.lower() == "stop":
        break
       if command.lower() == "0":
        break
    
       else:
        subprocess.run(command.lower(), shell=True)
    except Exception:
        print("put right command dont be xakhs ha99ir ")
        continue
print("!!!!")
print("URE ARE LEFT")
