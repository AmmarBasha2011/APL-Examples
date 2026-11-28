
# apl-source:1
# مثال 1322 — مصفوفة توبليتز
# apl-source:2
# Toeplitz matrix check
# apl-source:3
# Demonstrates: شبكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1322-toeplitz-check.apl
# apl-source:6

# apl-source:7
# كل خلية تساوي الخلية القطرية العليا اليسرى
# apl-source:8
# نقارن كل خلية بما فوقها قطرياً
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
def توبليتز(م):
  # apl-source:19
  for ص in range(1, len(م)):
    # apl-source:20
    for ج in range(1, len(م[0])):
      # apl-source:21
      if م[ص][ج] != م[ص - 1][ج - 1]:
        # apl-source:22
        return False
  # apl-source:23
  return True
# apl-source:24

# apl-source:25
تأكد_يساوي(توبليتز([[1,2,3,4],[5,1,2,3],[9,5,1,2]]), True, "توبليتز")
# apl-source:26
تأكد_يساوي(توبليتز([[1,2],[2,2]]), False, "ليست توبليتز")
# apl-source:27
تأكد_يساوي(توبليتز([[1]]), True, "خلية")
# apl-source:28
