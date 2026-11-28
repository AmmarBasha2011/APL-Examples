
# apl-source:1
# مثال 653 — اختيار عشوائي موزون
# apl-source:2
# Weighted random choice
# apl-source:3
# Demonstrates: أوزان، مجاميع تراكمية، اختيار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/653-weighted-random.apl
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
# اختيار عشوائي موزون
# apl-source:25
# Demonstrates: مجاميع تراكمية, بحث أول تجاوز, بذرة ثابتة
# apl-source:26
# اختيار عنصر باحتمال يتناسب مع وزنه
# apl-source:27

# apl-source:28
أوزان = [10, 20, 30, 40]
# apl-source:29
تراكمي = []
# apl-source:30
حاصل = 0
# apl-source:31
for و in أوزان:
  # apl-source:32
  حاصل = حاصل + و
  # apl-source:33
  تراكمي.append(حاصل)
# apl-source:34

# apl-source:35
def اختر(ر):
  # apl-source:36
  for ي in range(len(تراكمي)):
    # apl-source:37
    if ر < تراكمي[ي]:
      # apl-source:38
      return ي
  # apl-source:39
  return len(تراكمي) - 1
# apl-source:40

# apl-source:41
تأكد_يساوي(اختر(0), 0, "حد أدنى")
# apl-source:42
تأكد_يساوي(اختر(9), 0, "نهاية الشريحة الأولى")
# apl-source:43
تأكد_يساوي(اختر(10), 1, "بداية الشريحة الثانية")
# apl-source:44
تأكد_يساوي(اختر(29), 1, "نهاية الثانية")
# apl-source:45
تأكد_يساوي(اختر(30), 2, "بداية الثالثة")
# apl-source:46
تأكد_يساوي(اختر(59), 2, "نهاية الثالثة")
# apl-source:47
تأكد_يساوي(اختر(60), 3, "بداية الرابعة")
# apl-source:48
تأكد_يساوي(اختر(99), 3, "آخر قيمة")
# apl-source:49

# apl-source:50
بذرة = [7]
# apl-source:51
def تالي(ب):
  # apl-source:52
  ب[0] = (ب[0] * 1103515245 + 12345) % 2147483648
  # apl-source:53
  return ب[0]
# apl-source:54

# apl-source:55
تكرار = [0, 0, 0, 0]
# apl-source:56
for سحبة in range(200):
  # apl-source:57
  ي = اختر(تالي(بذرة) % 100)
  # apl-source:58
  تكرار[ي] = تكرار[ي] + 1
# apl-source:59
تأكد_يساوي(تكرار[3] > تكرار[0], True, "الأثقل يتكرر أكثر")
# apl-source:60
print("التكرارات:", تكرار)
# apl-source:61
