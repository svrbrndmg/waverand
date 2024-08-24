import time, random
chars = input(r"Choose some characters (no spaces between them, unless you want a space) ")
limit = 1
while limit != 300:
   print(random.choice(chars) * random.randint(1, 20), end='')
   time.sleep(0.05)
   limit += 1
print("That should be enough :)")
   
