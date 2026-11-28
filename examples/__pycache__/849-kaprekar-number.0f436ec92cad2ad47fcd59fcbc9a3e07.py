
# apl-source:1
# مثال 849 — روتين كابريكار
# apl-source:2
# Kaprekar routine
# apl-source:3
# Demonstrates: ترتيب وطرح متكرر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/849-kaprekar-number.apl
# apl-source:6

# apl-source:7
# روتين كابريكار: أي عدد رباعي غير متساوي الأرقام يصل إلى 6174
# apl-source:8
# رتّب الأرقام تنازلياً ناقص تصاعدياً، وكرر
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
def أرقام_مرتبة(ن, تنازلي):
  # apl-source:19
  أ = []
  # apl-source:20
  م = ن
  # apl-source:21
  for _ in range(4):
    # apl-source:22
    أ = أ + [م % 10]
    # apl-source:23
    م = م // 10
  # apl-source:24
  # فرز فقاعي لأربعة أرقام
  # apl-source:25
  for i in range(4):
    # apl-source:26
    for ج in range(3):
      # apl-source:27
      if أ[ج] > أ[ج + 1]:
        # apl-source:28
        مؤقت = أ[ج]
        # apl-source:29
        أ[ج] = أ[ج + 1]
        # apl-source:30
        أ[ج + 1] = مؤقت
  # apl-source:31
  # أ مرتبة تصاعدياً: التنازلي يبنى من النهاية والتصاعدي من البداية
  # apl-source:32
  ناتج = 0
  # apl-source:33
  if تنازلي:
    # apl-source:34
    for i in range(4):
      # apl-source:35
      ناتج = ناتج * 10 + أ[3 - i]
  # apl-source:36
  else:
    # apl-source:37
    for ق in أ:
      # apl-source:38
      ناتج = ناتج * 10 + ق
  # apl-source:39
  return ناتج
# apl-source:40

# apl-source:41
def خطوات_كابريكار(بداية):
  # apl-source:42
  ن = بداية
  # apl-source:43
  خطوات = []
  # apl-source:44
  while ن != 6174:
    # apl-source:45
    تنازلي = أرقام_مرتبة(ن, 1 == 1)
    # apl-source:46
    تصاعدي = أرقام_مرتبة(ن, False)
    # apl-source:47
    ن = تنازلي - تصاعدي
    # apl-source:48
    خطوات = خطوات + [ن]
  # apl-source:49
  return خطوات
# apl-source:50

# apl-source:51
مسار = خطوات_كابريكار(3524)
# apl-source:52
print("من 3524:", مسار)
# apl-source:53
تأكد_يساوي(مسار[0], 3087, "أول خطوة من 3524")
# apl-source:54
تأكد_يساوي(مسار[1], 8352, "ثاني خطوة")
# apl-source:55
تأكد_يساوي(مسار[2], 6174, "الوصول للثابت")
# apl-source:56

# apl-source:57
مسار2 = خطوات_كابريكار(1000)
# apl-source:58
print("من 1000:", مسار2)
# apl-source:59
تأكد_يساوي(len(مسار2), 5, "خمس خطوات من 1000")
# apl-source:60
تأكد_يساوي(مسار2[4], 6174, "ينتهي دائماً بـ 6174")
# apl-source:61
