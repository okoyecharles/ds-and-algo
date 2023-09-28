# Difference between two strings

def diffBetweenTwoStrings(source, target):
  """
  @param source: str
  @param target: str
  @return: str[]
  """
  
  # diff(index, str[], ops)
  # table -> table
  # recursion -> call stack, memo
  
  def diff(i, j, res, ops):
    if i == len(source) and j == len(target):
      return (res, ops)
    else:
      if i >= len(source):
        chars = target[j:].split()
        chars = list(map(lambda char: "+" + char, chars))
        return (res + chars, ops + (len(target) - j))
      if j >= len(target):
        chars = source[i:].split()
        chars = list(map(lambda char: "-" + char, chars))
        return (res + chars, ops + (len(source) - i))     
    
    if source[i] == target[j]:
      return diff(i + 1, j + 1, res + [source[i]], ops)
    else:
      # add a char
      add = diff(i, j + 1, res + ['+' + target[j]], ops + 1)
      # delete a char
      delete = diff(i + 1, j, res + ['-' + source[i]], ops + 1)
      
      if add[1] < delete[1]:
        return add
      else:
        return delete
      
  print(diff(0, 0, [], 0))
    
diffBetweenTwoStrings("ABCDEFG", "ABDFFGH")