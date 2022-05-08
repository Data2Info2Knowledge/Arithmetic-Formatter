import re
from arithmetic_arranger import arithmetic_arranger

typedin = input('Enter a list of arithmetic operations: ')
typedin = typedin.replace("\'","\"") # tweak for single quotes
if not (typedin[0]=="[" and typedin[-1]=="]"):
  print("Error: please enter a list of strings")
  exit()
matchthis = '\"([^\"]*)\"'
mylist = re.findall(matchthis,typedin)
showres=False
yesorno = "A"
while yesorno not in ["Y","N"]:
  yesorno = input('Display answers (Y/N): ').upper()
if yesorno == "Y": showres=True
print(arithmetic_arranger(mylist, showres))
