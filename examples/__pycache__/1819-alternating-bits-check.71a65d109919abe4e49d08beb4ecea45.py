
# apl-source:1
# مثال 1819 — بتات متناوبة
# apl-source:2
# Alternating bits check
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1819-alternating-bits-check.apl
# apl-source:6

# apl-source:7
# نقارن البت بالذي قبله
# apl-source:8
# نزيح العدد في كل خطوة
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
def متناوبة(ن):
  # apl-source:19
  سابق = ن & 1
  # apl-source:20
  ن = ن >> 1
  # apl-source:21
  while ن > 0:
    # apl-source:22
    حالي = ن & 1
    # apl-source:23
    if حالي == سابق:
      # apl-source:24
      return False
    # apl-source:25
    سابق = حالي
    # apl-source:26
    ن = ن >> 1
  # apl-source:27
  return True
# apl-source:28

# apl-source:29
تأكد_يساوي(متناوبة(5), True, "101")
# apl-source:30
تأكد_يساوي(متناوبة(7), False, "111")
# apl-source:31
تأكد_يساوي(متناوبة(10), True, "1010")
# apl-source:32
تأكد_يساوي(متناوبة(11), False, "1011")
# apl-source:33
