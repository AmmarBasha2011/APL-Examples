
# apl-source:1
# مثال 1697 — من الأرقام الرومانية إلى عدد
# apl-source:2
# Roman numeral to integer
# apl-source:3
# Demonstrates: ترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1697-roman-numeral-to-integer.apl
# apl-source:6

# apl-source:7
# نقارن كل رمز بالتالي
# apl-source:8
# الأصغر قبل الأكبر يُطرح
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
def روماني_لعدد(س):
  # apl-source:19
  قيم = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  # apl-source:20
  مجموع = 0
  # apl-source:21
  for ك in range(len(س)):
    # apl-source:22
    ق = قيم[س[ك]]
    # apl-source:23
    if ك + 1 < len(س):
      # apl-source:24
      if ق < قيم[س[ك + 1]]:
        # apl-source:25
        ق = -ق
    # apl-source:26
    مجموع = مجموع + ق
  # apl-source:27
  return مجموع
# apl-source:28

# apl-source:29
تأكد_يساوي(روماني_لعدد("III"), 3, "ثلاثة")
# apl-source:30
تأكد_يساوي(روماني_لعدد("IV"), 4, "أربعة")
# apl-source:31
تأكد_يساوي(روماني_لعدد("MCMXCIV"), 1994, "1994")
# apl-source:32
