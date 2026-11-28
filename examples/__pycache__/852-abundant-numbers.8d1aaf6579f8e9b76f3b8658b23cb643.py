
# apl-source:1
# مثال 852 — الأعداد الوفيرة
# apl-source:2
# Abundant numbers
# apl-source:3
# Demonstrates: قواسم تفوق العدد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/852-abundant-numbers.apl
# apl-source:6

# apl-source:7
# الأعداد الوفيرة: مجموع قواسمها الذاتية أكبر منها
# apl-source:8
# 12 هو أولها: 1+2+3+4+6 = 16 > 12
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
def مجموع_القواسم(ن):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ق in range(1, ن):
    # apl-source:21
    if ن % ق == 0:
      # apl-source:22
      مجموع = مجموع + ق
  # apl-source:23
  return مجموع
# apl-source:24

# apl-source:25
وفيرة = []
# apl-source:26
for ن in range(2, 31):
  # apl-source:27
  if مجموع_القواسم(ن) > ن:
    # apl-source:28
    وفيرة = وفيرة + [ن]
# apl-source:29

# apl-source:30
print("الوفيرة حتى 30:", وفيرة)
# apl-source:31

# apl-source:32
تأكد_يساوي(len(وفيرة), 5, "خمسة حتى 30")
# apl-source:33
تأكد_يساوي(وفيرة[0], 12, "الأول")
# apl-source:34
تأكد_يساوي(وفيرة[4], 30, "الخامس")
# apl-source:35

# apl-source:36
# كل الوفيرة تحت 100 زوجية: أول وفيرة فردية هي 945
# apl-source:37
أول_فردية = 0
# apl-source:38
for ن in range(3, 946):
  # apl-source:39
  if ن % 2 == 1 and مجموع_القواسم(ن) > ن:
    # apl-source:40
    if أول_فردية == 0:
      # apl-source:41
      أول_فردية = ن
# apl-source:42
تأكد_يساوي(أول_فردية, 945, "أول وفيرة فردية هي 945")
# apl-source:43
