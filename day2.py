text = '874324-1096487,6106748-6273465,1751-4283,294380-348021,5217788-5252660,828815656-828846474,66486-157652,477-1035,20185-55252,17-47,375278481-375470130,141-453,33680490-33821359,88845663-88931344,621298-752726,21764551-21780350,58537958-58673847,9983248-10042949,4457-9048,9292891448-9292952618,4382577-4494092,199525-259728,9934981035-9935011120,6738255458-6738272752,8275916-8338174,1-15,68-128,7366340343-7366538971,82803431-82838224,72410788-72501583'

import math

def digits(n):
  return int(math.log10(n)) + 1

pairs = []
for i in text.split(','):
  #print(i)
  a, b = [int(j) for j in i.split('-')]
  if digits(a) != digits(b):
    pairs.append((a, int('9' * digits(a))))
    pairs.append((int('1' + '0' * (digits(b) - 1)), b))
    #print(f'{pairs[-2]} {pairs[-1]}')
  else:
    pairs.append((a, b))
    #print(f'{pairs[-1]}')

# part 1
count = 0
for a, b in pairs:
  #print(a, b)
  if digits(a) % 2 == 1:
    continue
  left_a = int(str(a)[:len(str(a)) // 2])
  left_b = int(str(b)[:len(str(b)) // 2])
  for i in range(left_a, left_b + 1):
    if a <= int(2 * str(i)) <= b:
      #print(f'  {2 * str(i)}')
      count += int(2 * str(i)) 
print(count)

# part 2
def is_bad(n):
  n = str(n)
  for length in range(1, len(n)):
    if len(n) % length == 0 and n[:length] * (len(n) // length) == n:
      print(n[:length], len(n) // length)
      return True
  return False

patterns = []
count = 0
for a, b in pairs:
  lengths = []
  for i in range(1, len(str(a))):
    if len(str(a)) % i == 0:
      lengths.append(i)
  print(a, b, lengths)
  used = set()
  for length in lengths:
    left = int(str(a)[:length])
    right = int(str(b)[:length])
    for prefix in range(left, right + 1):
      if a <= int(str(prefix) * (len(str(a)) // length)) <= b:
        if int(str(prefix) * (len(str(a)) // length)) not in used:
          count += int(str(prefix) * (len(str(a)) // length)) 
          used.add(int(str(prefix) * (len(str(a)) // length)))
          print(' ', int(str(prefix) * (len(str(a)) // length)))
          if not is_bad(int(str(prefix) * (len(str(a)) // length))):
            print('  NOT BAD')
          patterns.append(int(str(prefix) * (len(str(a)) // length))) 
print(count)

'''
patterns2 = []
for a, b in pairs:
  for i in range(a, b + 1):
    for length in range(1, len(str(a))):

      if len(str(a)) % length == 0 and int(str(i)[:length] * (len(str(a)) // length)) == i:
        patterns2.append(int(str(i)[:length] * (len(str(a)) // length)))
        break
print([i for i in zip(sorted(patterns), sorted(patterns2))])
'''
