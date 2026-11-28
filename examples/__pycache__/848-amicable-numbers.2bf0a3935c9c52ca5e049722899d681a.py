
# apl-source:1
# مثال 848 — الأعداد المتحابة
# apl-source:2
# Amicable numbers
# apl-source:3
# Demonstrates: قواسم كل يجمع للآخر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/848-amicable-numbers.apl
# apl-source:6

# apl-source:7
# الأعداد المتحابة: زوج مجموع قواسم كل منهما يساوي الآخر
# apl-source:8
# أشهرها (220, 284) المعروف منذ فيثاغورس
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
متحابة = []
# apl-source:26
for أ in range(2, 1500):
  # apl-source:27
  ب = مجموع_القواسم(أ)
  # apl-source:28
  if ب > أ:
    # apl-source:29
    if مجموع_القواسم(ب) == أ:
      # apl-source:30
      متحابة = متحابة + [[أ, ب]]
# apl-source:31

# apl-source:32
print("متحابة تحت 1500:", متحابة)
# apl-source:33

# apl-source:34
تأكد_يساوي(len(متحابة), 2, "زوجان تحت 1500")
# apl-source:35
تأكد_يساوي(متحابة[0][0], 220, "الزوج الأول أصغره 220")
# apl-source:36
تأكد_يساوي(متحابة[0][1], 284, "الزوج الأول أكبره 284")
# apl-source:37
تأكد_يساوي(متحابة[1][0], 1184, "الزوج الثاني أصغره 1184")
# apl-source:38
تأكد_يساوي(متحابة[1][1], 1210, "الزوج الثاني أكبره 1210")
# apl-source:39

# apl-source:40
# تحقق مباشر: قواسم 220 هي 1,2,4,5,10,11,20,22,44,55,110
# apl-source:41
تأكد_يساوي(مجموع_القواسم(220), 284, "مجموع قواسم 220")
# apl-source:42
تأكد_يساوي(مجموع_القواسم(284), 220, "مجموع قواسم 284")
# apl-source:43
