
# apl-source:1
# مثال 2116 — الأولي الدائري
# apl-source:2
# Circular prime check v2
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2116-circular-prime-all-rotations-prime.apl
# apl-source:6

# apl-source:7
# # ندور الأرقام حرفا حرفا
# apl-source:8
# # 197 مثال
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
def اولي(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  د = 2
  # apl-source:22
  while د * د <= ن:
    # apl-source:23
    if ن % د == 0:
      # apl-source:24
      return False
    # apl-source:25
    د = د + 1
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
def دائري(ن):
  # apl-source:29
  س = str(ن)
  # apl-source:30
  for ك in range(len(س)):
    # apl-source:31
    if اولي(int(س[ك:] + س[:ك])) == False:
      # apl-source:32
      return False
  # apl-source:33
  return True
# apl-source:34

# apl-source:35
تأكد_يساوي(دائري(197), True, "١٩٧")
# apl-source:36
تأكد_يساوي(دائري(13), True, "١٣")
# apl-source:37
تأكد_يساوي(دائري(19), False, "١٩")
# apl-source:38
تأكد_يساوي(دائري(2), True, "٢")
# apl-source:39
تأكد_يساوي(دائري(11), True, "١١")
# apl-source:40
