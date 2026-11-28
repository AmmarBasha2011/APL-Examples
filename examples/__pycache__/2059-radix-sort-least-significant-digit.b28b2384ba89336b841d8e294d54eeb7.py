
# apl-source:1
# مثال 2059 — الفرز الجذري بالخانة الأقل أهمية
# apl-source:2
# Radix sort LSD
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2059-radix-sort-least-significant-digit.apl
# apl-source:6

# apl-source:7
# # نبدأ من خانة الآحاد
# apl-source:8
# # كل جولة مستقرة
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
def جذري(ق):
  # apl-source:19
  if len(ق) == 0:
    # apl-source:20
    return []
  # apl-source:21
  اقصى = max(ق)
  # apl-source:22
  خانة = 1
  # apl-source:23
  while اقصى // خانة > 0:
    # apl-source:24
    سلال = []
    # apl-source:25
    for ك in range(10):
      # apl-source:26
      سلال = سلال + [[]]
    # apl-source:27
    for ع in ق:
      # apl-source:28
      سلال[(ع // خانة) % 10].append(ع)
    # apl-source:29
    ق = []
    # apl-source:30
    for س in سلال:
      # apl-source:31
      ق = ق + س
    # apl-source:32
    خانة = خانة * 10
  # apl-source:33
  return ق
# apl-source:34

# apl-source:35
تأكد_يساوي(جذري([170, 45, 75, 90, 802, 24, 2, 66]), [2, 24, 45, 66, 75, 90, 170, 802], "كلاسيكي")
# apl-source:36
تأكد_يساوي(جذري([]), [], "فارغة")
# apl-source:37
تأكد_يساوي(جذري([5]), [5], "واحد")
# apl-source:38
