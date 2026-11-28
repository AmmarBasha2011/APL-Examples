
# apl-source:1
# مثال 922 — روتين كابريكار
# apl-source:2
# Kaprekar routine
# apl-source:3
# Demonstrates: فرق ترتيبي الأرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/922-kaprekar.apl
# apl-source:6

# apl-source:7
# روتين كابريكار: أي عدد رباعي (بأرقام غير متماثلة) يبلغ 6174
# apl-source:8
# رتب الأرقام تنازلياً ناقص تصاعدياً، وكرر
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
def خطوة_كابريكار(ن):
  # apl-source:19
  # استخرج 4 أرقام (مع أصفار بادئة)
  # apl-source:20
  أرقام = []
  # apl-source:21
  م = ن
  # apl-source:22
  for _ in range(4):
    # apl-source:23
    أرقام = أرقام + [م % 10]
    # apl-source:24
    م = م // 10
  # apl-source:25
  # فرز فقاعي تصاعدي
  # apl-source:26
  for i in range(4):
    # apl-source:27
    for ج in range(i + 1, 4):
      # apl-source:28
      if أرقام[ج] < أرقام[i]:
        # apl-source:29
        مؤقت = أرقام[i]
        # apl-source:30
        أرقام[i] = أرقام[ج]
        # apl-source:31
        أرقام[ج] = مؤقت
  # apl-source:32
  صاعد = 0
  # apl-source:33
  هابط = 0
  # apl-source:34
  for i in range(4):
    # apl-source:35
    صاعد = صاعد * 10 + أرقام[i]
    # apl-source:36
    هابط = هابط * 10 + أرقام[3 - i]
  # apl-source:37
  return هابط - صاعد
# apl-source:38

# apl-source:39
def خطوات_كابريكار(ن):
  # apl-source:40
  م = ن
  # apl-source:41
  عد = 0
  # apl-source:42
  while م != 6174:
    # apl-source:43
    م = خطوة_كابريكار(م)
    # apl-source:44
    عد = عد + 1
  # apl-source:45
  return عد
# apl-source:46

# apl-source:47
print("3524 ->", خطوات_كابريكار(3524), "خطوات")
# apl-source:48
print("1234 ->", خطوات_كابريكار(1234), "خطوات")
# apl-source:49

# apl-source:50
تأكد_يساوي(خطوة_كابريكار(3524), 3087, "خطوة أولى: 5432-2345")
# apl-source:51
تأكد_يساوي(خطوات_كابريكار(3524), 3, "ثلاث خطوات من 3524")
# apl-source:52
تأكد_يساوي(خطوات_كابريكار(1234), 3, "ثلاث خطوات من 1234")
# apl-source:53
تأكد_يساوي(خطوات_كابريكار(6174), 0, "الثابتة بلا خطوات")
# apl-source:54
# كل الأعداد الرباعية ذات الأرقام المختلطة تصل خلال 7 خطوات
# apl-source:55
تأكد_يساوي(خطوات_كابريكار(1000) <= 7, 1 == 1, "1000 تصل بسرعة")
# apl-source:56
