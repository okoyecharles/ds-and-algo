# Difference between two strings

# Find the steps to create target from source using the lowest edits possible
# source = "ABCDEFG"
# target = "ABDFFGH"
# return: ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"
from pprint import pprint

def split_prepend (str, pre):
    chars = [pre + c for c in str]
    return chars

def diff_between_two_strings(source, target):
  def diff(i, j, res, ops):
    if i == len(source) and j == len(target): return (res, ops)
    elif i >= len(source): return (res + split_prepend(target[j:], "+"), ops + (len(target) - j))
    elif j >= len(target): return (res + split_prepend(source[i:], "-"), ops + (len(source) - i))

    if source[i] == target[j]:
      return diff(i + 1, j + 1, res + [source[i]], ops)
    else:
      add = diff(i, j + 1, res + ['+' + target[j]], ops + 1)
      delete = diff(i + 1, j, res + ['-' + source[i]], ops + 1)
      return add if add[1] < delete[1] else delete
      
  chars, operations = diff(0, 0, [], 0)
  return chars

def diff_between_two_strings_tabular(source, target):
  ROWS, COLS = len(source) + 1, len(target) + 1
  table = [[(list(), float('inf')) for col in range(COLS)] for row in range(ROWS)]
  table[0][0] = ([], 0)

  def valid_pos(i, j): return i < ROWS and j < COLS
  
  for i in range(ROWS):
    for j in range(COLS):
      diff, ops = table[i][j]
      if i == ROWS - 1:
        if len(diff) and table[-1][-1][1] >= (ops + (len(target) - j)):
          table[-1][-1] = (diff + split_prepend(target[j:], '+'), ops + (len(target) - j))
        continue
      if j == COLS - 1:
        if len(diff) and table[-1][-1][1] >= (ops + (len(source) - i)):
          table[-1][-1] = (diff + split_prepend(source[i:], '-'), ops + (len(source) - i))
        continue
    
      if source[i] == target[j]:
        table[i + 1][j + 1] = (diff + [source[i]], ops) # same
      else:
        if table[i][j + 1][1] > ops:
          table[i][j + 1] = (diff + ['+' + target[j]], ops + 1) # add
        if table[i + 1][j][1] > ops:
          table[i + 1][j] = (diff + ['-' + source[i]], ops + 1) # remove
  pprint(table)
  return (table[-1][-1][0])
 
['H', '-M', '-X', '+L', '+Z', 'P', '-H', '-H', '+L', 'U', '-M', '+P', '+H']
['H', '-M', '-X', '+L', '+Z', 'P', '+L', '+U', '+P', 'H', '-H', '-U', '-M']

print(diff_between_two_strings_tabular("HMXPHHUM", "HLZPLUPH"))

