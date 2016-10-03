def getHashed(shadow):
   for line in shadow:
      line = line.split(":")

      if line[0] == sys.argv[1]:
         if line[1] == "*":
            sys.exit("Warning: User Does Not Have A Password.")
         else:
            line[1] = sys.argv[2]
            return line[1]
   sys.exit("Warning: User Does Not Exist.")


def crackShadow(hash, dictPath, ctype, salt):
   insalt = '${}${}$'.format(ctype, salt)

   dict = openFile(dictPath)

   for pwd in dict:
      if crypt.crypt(pwd.strip(), insalt) == hash:
         sys.exit("Success: Password is " + pwd)
   sys.exit("Warning: Password Not Found In Dictionary.")


def openFile(file):
   if os.path.isfile(file):
      return open(file, 'r')
   else:
      sys.exit("Error: File Does Not Exist.")



### MAIN SCRIPT ###

if __name__ == '__main__':
   import crypt
   import sys

   if len(sys.argv) < 3:
      sys.exit("Error: Invalid Arguments.")
   else:

      # SELECT DICTIONARY FILE
      dictPath = "./dictionary.txt"

      if len(sys.argv) > 3:
         if sys.argv[3] == "-d" and len(sys.argv) > 4:
            dictPath = sys.argv[4]
      else:
         sys.exit("Error: Invalid Arguments.")


      shadow = openFile(sys.argv[2])     #opens shadow file
      hash = getHashed(shadow)             #gets password hash of file
      encrypt = hash.split("$")

      ctype = encrypt[1]       #hash properties
      salt = encrypt[2]        #hash properies

      crackShadow(hash, dictPath, ctype, salt)
