# Difference between two strings

# Find the steps to create target from source using the lowest edits possible
# source = "ABCDEFG"
# target = "ABDFFGH"
# return: ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"

def diff_between_two_strings(source, target):
  def split_prepend (str, pre):
    chars = [c for c in str]
    chars = list(map(lambda char: pre + char, chars))
    return chars

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
  pass

    
diff_between_two_strings("ABCDEFG", "ABDFFGH")