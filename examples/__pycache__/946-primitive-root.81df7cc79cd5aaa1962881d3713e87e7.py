
# apl-source:1
# مثال 946 — الجذر البدائي
# apl-source:2
# Primitive root
# apl-source:3
# Demonstrates: قوى تغطي الزمرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/946-primitive-root.apl
# apl-source:6

# apl-source:7
# الجذر البدائي: مولد الزمرة الدائرية مودولو أولي
# apl-source:8
# ج هو جذر بدائي إن كانت قواه تغطي كل غير الأصفار
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
def قوة(أساس, أس, مقام):
  # apl-source:19
  ناتج = 1
  # apl-source:20
  ب = أساس % مقام
  # apl-source:21
  ه = أس
  # apl-source:22
  while ه > 0:
    # apl-source:23
    if ه % 2 == 1:
      # apl-source:24
      ناتج = (ناتج * ب) % مقام
    # apl-source:25
    ب = (ب * ب) % مقام
    # apl-source:26
    ه = ه // 2
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
def جذر_بدائي(أولي):
  # apl-source:30
  فاي = أولي - 1
  # apl-source:31
  # عوامل فاي الأولية
  # apl-source:32
  عوامل = []
  # apl-source:33
  م = فاي
  # apl-source:34
  د = 2
  # apl-source:35
  while د * د <= م:
    # apl-source:36
    while م % د == 0:
      # apl-source:37
      if (len(عوامل) == 0) or (عوامل[len(عوامل) - 1] != د):
        # apl-source:38
        عوامل = عوامل + [د]
      # apl-source:39
      م = م // د
    # apl-source:40
    د = د + 1
  # apl-source:41
  if م > 1:
    # apl-source:42
    if (len(عوامل) == 0) or (عوامل[len(عوامل) - 1] != م):
      # apl-source:43
      عوامل = عوامل + [م]
  # apl-source:44
  # أول ج يحقق ج^(في/ق) != 1 لكل ق
  # apl-source:45
  for ج in range(2, أولي):
    # apl-source:46
    صالح = 1
    # apl-source:47
    for ق in عوامل:
      # apl-source:48
      if قوة(ج, فاي // ق, أولي) == 1:
        # apl-source:49
        صالح = 0
    # apl-source:50
    if صالح == 1:
      # apl-source:51
      return ج
  # apl-source:52
  return -1
# apl-source:53

# apl-source:54
print("جذر بدائي لـ 7:", جذر_بدائي(7))
# apl-source:55
print("جذر بدائي لـ 23:", جذر_بدائي(23))
# apl-source:56
print("جذر بدائي لـ 41:", جذر_بدائي(41))
# apl-source:57

# apl-source:58
تأكد_يساوي(جذر_بدائي(7), 3, "الجذر البدائي لسبعة")
# apl-source:59
تأكد_يساوي(جذر_بدائي(23), 5, "الجذر البدائي لـ 23")
# apl-source:60
تأكد_يساوي(جذر_بدائي(41), 6, "الجذر البدائي لـ 41")
# apl-source:61

# apl-source:62
# التحقق: قوى 3 مودولو 7 تغطي 1..6 كلها
# apl-source:63
مشاهد = [0, 0, 0, 0, 0, 0, 0]
# apl-source:64
قوة_جارية = 1
# apl-source:65
for i in range(6):
  # apl-source:66
  قوة_جارية = (قوة_جارية * 3) % 7
  # apl-source:67
  مشاهد[قوة_جارية] = 1
# apl-source:68
مجموع = 0
# apl-source:69
for i in range(1, 7):
  # apl-source:70
  مجموع = مجموع + مشاهد[i]
# apl-source:71
تأكد_يساوي(مجموع, 6, "القوى تغطي الكل")
# apl-source:72
