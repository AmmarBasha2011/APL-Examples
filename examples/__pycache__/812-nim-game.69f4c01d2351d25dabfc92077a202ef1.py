
# apl-source:1
# مثال 812 — لعبة نيم
# apl-source:2
# Nim game
# apl-source:3
# Demonstrates: nim-sum بXOR، نقلة فائزة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/812-nim-game.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# لعبة نيم: المجموع الصفري بXOR يحدد الوضعية الخاسرة والنقلة الفائزة
# apl-source:25
# Demonstrates: nim-sum بالحصر الثنائي, استراتيجية برتراند, محاكاة نقلات
# apl-source:26

# apl-source:27
def مجموع_نيم(أكوام):
  # apl-source:28
  س = 0
  # apl-source:29
  for كومة in أكوام:
    # apl-source:30
    س = س ^ كومة
  # apl-source:31
  return س
# apl-source:32

# apl-source:33
def نقلة_فائزة(أكوام):
  # apl-source:34
  س = مجموع_نيم(أكوام)
  # apl-source:35
  if س == 0:
    # apl-source:36
    return [-1, -1]
  # apl-source:37
  for ي in range(len(أكوام)):
    # apl-source:38
    هدف = أكوام[ي] ^ س
    # apl-source:39
    if هدف < أكوام[ي]:
      # apl-source:40
      return [ي, هدف]
  # apl-source:41
  return [-1, -1]
# apl-source:42

# apl-source:43
تأكد_يساوي(مجموع_نيم([3, 4, 5]), 2, "مجموع 3 4 5")
# apl-source:44
تأكد_يساوي(مجموع_نيم([1, 2, 3]), 0, "وضعية خاسرة")
# apl-source:45
تأكد_يساوي(نقلة_فائزة([3, 4, 5]), [0, 1], "الكومة الأولى إلى واحد")
# apl-source:46
تأكد_يساوي(نقلة_فائزة([1, 2, 3]), [-1, -1], "لا نقلة فائزة")
# apl-source:47
أكوام = [3, 4, 5]
# apl-source:48
نقلة = نقلة_فائزة(أكوام)
# apl-source:49
أكوام[نقلة[0]] = نقلة[1]
# apl-source:50
تأكد_يساوي(مجموع_نيم(أكوام), 0, "النقلة تصفي المجموع")
# apl-source:51
تأكد_يساوي(مجموع_نيم([7, 7, 7]), 7, "ثلاثة متساوية")
# apl-source:52
