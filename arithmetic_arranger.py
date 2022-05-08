import re
def arithmetic_arranger(problems, showres=False):
    if not isinstance(problems, list):
      return "Error: argument must be a list."
    else:
      numprobs = len(problems)
      for prob in problems:
        unwntd = re.findall("[^\d\+\-\/\*\s]", prob)
        if len(unwntd)>0:
          return"Error: Numbers must only contain digits."
      if numprobs > 5:
        return "Error: Too many problems."
      matchthis = '(\S+)\s*(\S+)\s*(\S+)'
      opnd1row = ""
      opnd2row = ""
      dashzrow = ""
      resltrow = ""
      for prob in problems:
        opnd1 = re.sub(matchthis, r"\1", prob)
        oprtr = re.sub(matchthis, r"\2", prob)
        opnd2 = re.sub(matchthis, r"\3", prob)
        if not oprtr in "+-":
          return "Error: Operator must be \'+\' or \'-\'."
        nbr1 = int(opnd1)
        nbr2 = int(opnd2)
        if max(nbr1,nbr2) > 9999:
          return "Error: Numbers cannot be more than four digits."
# Calculate answer depending on operator          
        if oprtr == "+":
          ans = nbr1+nbr2
        else:
          ans = nbr1-nbr2
# Calculate width of current operation          
        numpos = 2 + max(len(str(opnd1)), len(str(opnd2)))
# Build strings for: answer, operand 1,
#     operand 2 (preceded by operator), 
#     row of dashes, and answer if displayed;
# append each string to its "row string"
        anstr = f'{ans : >{numpos}}' if showres==True else ""
        opnd1row = opnd1row + f'{opnd1 : >{numpos}}' + " "*4
        opnd2row = opnd2row + oprtr + " " + f'{opnd2 : >{numpos-2}}' + " "*4
        dashzrow = dashzrow + "-"*numpos + " "*4
        resltrow = resltrow + f'{anstr : >{numpos}}' + " "*4
# Stack all row strings on top of one another
      arranged_problems = opnd1row.rstrip() + "\n" + opnd2row.rstrip() + "\n" + dashzrow.rstrip()
      if showres==True:
        arranged_problems = arranged_problems + "\n" + resltrow.rstrip()

    return arranged_problems