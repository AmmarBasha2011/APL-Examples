
# apl-source:1
# مثال 853 — أصفار المضروب
# apl-source:2
# Trailing zeros of n!
# apl-source:3
# Demonstrates: عد قوى الخمسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/853-trailing-zeros-factorial.apl
# apl-source:6

# apl-source:7
# أصفار المضروب اللاحقة: عد أزواج (2×5) في التحليل
# apl-source:8
# يكفي عد عوامل الخمسة لأن الاثنينات أكثر
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
def أصفار_المضروب(ن):
  # apl-source:19
  أصفار = 0
  # apl-source:20
  قوة = 5
  # apl-source:21
  while قوة <= ن:
    # apl-source:22
    أصفار = أصفار + ن // قوة
    # apl-source:23
    قوة = قوة * 5
  # apl-source:24
  return أصفار
# apl-source:25

# apl-source:26
print("أصفار 100!:", أصفار_المضروب(100))
# apl-source:27
print("أصفار 1000!:", أصفار_المضروب(1000))
# apl-source:28

# apl-source:29
تأكد_يساوي(أصفار_المضروب(5), 1, "5! = 120 صفر واحد")
# apl-source:30
تأكد_يساوي(أصفار_المضروب(24), 4, "24! أربعة أصفار")
# apl-source:31
تأكد_يساوي(أصفار_المضروب(25), 6, "25! قفزة مزدوجة لأن 25 = 5²")
# apl-source:32
تأكد_يساوي(أصفار_المضروب(100), 24, "100! = 20+4")
# apl-source:33
تأكد_يساوي(أصفار_المضروب(1000), 249, "1000! = 200+40+8+1")
# apl-source:34

# apl-source:35
# تحقق مباشر: اقسم المضروب الفعلي على 10 حتى يفشل
# apl-source:36
مضروب = 1
# apl-source:37
for i in range(1, 26):
  # apl-source:38
  مضروب = مضروب * i
# apl-source:39
عد = 0
# apl-source:40
while مضروب % 10 == 0:
  # apl-source:41
  عد = عد + 1
  # apl-source:42
  مضروب = مضروب // 10
# apl-source:43
تأكد_يساوي(عد, 6, "تحقق مباشر من 25!")
# apl-source:44
