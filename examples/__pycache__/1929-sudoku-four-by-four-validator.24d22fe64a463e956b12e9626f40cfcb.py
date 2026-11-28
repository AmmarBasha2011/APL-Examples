
# apl-source:1
# مثال 1929 — التحقق من سودوكو ٤ في ٤
# apl-source:2
# Validate a four by four sudoku
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1929-sudoku-four-by-four-validator.apl
# apl-source:6

# apl-source:7
# نجمع كل مجموعة من أربع خلايا
# apl-source:8
# نتأكد أنها تحوي أربع قيم مختلفة
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def مجموعة_صحيحة(قيم):
  # apl-source:19
  for ف in [1, 2, 3, 4]:
    # apl-source:20
    if (ف in قيم) == False:
      # apl-source:21
      return False
  # apl-source:22
  return True
# apl-source:23

# apl-source:24
def صحيح(ش):
  # apl-source:25
  for ص in range(4):
    # apl-source:26
    if مجموعة_صحيحة(ش[ص]) == False:
      # apl-source:27
      return False
    # apl-source:28
    عمود = []
    # apl-source:29
    for ج in range(4):
      # apl-source:30
      عمود = عمود + [ش[ج][ص]]
    # apl-source:31
    if مجموعة_صحيحة(عمود) == False:
      # apl-source:32
      return False
  # apl-source:33
  for ب in [0, 2]:
    # apl-source:34
    for ت in [0, 2]:
      # apl-source:35
      مربع = [ش[ب][ت], ش[ب][ت + 1], ش[ب + 1][ت], ش[ب + 1][ت + 1]]
      # apl-source:36
      if مجموعة_صحيحة(مربع) == False:
        # apl-source:37
        return False
  # apl-source:38
  return True
# apl-source:39

# apl-source:40
جيد = [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]
# apl-source:41
سيئ = [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 1, 2]]
# apl-source:42
مربع_خاطئ = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]
# apl-source:43
تأكد_يساوي(صحيح(جيد), True, "صحيح")
# apl-source:44
تأكد_يساوي(صحيح(سيئ), False, "عمود مكرر")
# apl-source:45
تأكد_يساوي(صحيح(مربع_خاطئ), False, "مربع مكرر")
# apl-source:46
