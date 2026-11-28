
# apl-source:1
# مثال 897 — بحث فيبوناتشي
# apl-source:2
# Fibonacci search
# apl-source:3
# Demonstrates: تقسيم عند أعداد فيبوناتشي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/897-fibonacci-search.apl
# apl-source:6

# apl-source:7
# بحث فيبوناتشي: يقسم المصفوفة عند أعداد فيبوناتشي بدل النصف
# apl-source:8
# يفيد حين الوصول للعناصر غير متجانس الكلفة
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
def بحث_فيبوناتشي(مصفوفة, هدف):
  # apl-source:19
  ن = len(مصفوفة)
  # apl-source:20
  فيب2 = 0
  # apl-source:21
  فيب1 = 1
  # apl-source:22
  فيب = 1
  # apl-source:23
  while فيب < ن:
    # apl-source:24
    فيب2 = فيب1
    # apl-source:25
    فيب1 = فيب
    # apl-source:26
    فيب = فيب1 + فيب2
  # apl-source:27
  إزاحة = -1
  # apl-source:28
  while فيب > 1:
    # apl-source:29
    i = إزاحة + فيب2
    # apl-source:30
    if i > ن - 1:
      # apl-source:31
      i = ن - 1
    # apl-source:32
    if مصفوفة[i] < هدف:
      # apl-source:33
      فيب = فيب1
      # apl-source:34
      فيب1 = فيب2
      # apl-source:35
      فيب2 = فيب - فيب1
      # apl-source:36
      إزاحة = i
    # apl-source:37
    elif مصفوفة[i] > هدف:
      # apl-source:38
      فيب = فيب2
      # apl-source:39
      فيب1 = فيب1 - فيب2
      # apl-source:40
      فيب2 = فيب - فيب1
    # apl-source:41
    else:
      # apl-source:42
      return i
  # apl-source:43
  if (فيب1 == 1) and (إزاحة + 1 < ن) and (مصفوفة[إزاحة + 1] == هدف):
    # apl-source:44
    return إزاحة + 1
  # apl-source:45
  return -1
# apl-source:46

# apl-source:47
مصفوفة = [1, 3, 4, 6, 7, 8, 10, 13, 14]
# apl-source:48
print("موضع 10:", بحث_فيبوناتشي(مصفوفة, 10))
# apl-source:49
print("موضع 14:", بحث_فيبوناتشي(مصفوفة, 14))
# apl-source:50

# apl-source:51
تأكد_يساوي(بحث_فيبوناتشي(مصفوفة, 10), 6, "الهدف الأوسط")
# apl-source:52
تأكد_يساوي(بحث_فيبوناتشي(مصفوفة, 14), 8, "الأخير")
# apl-source:53
تأكد_يساوي(بحث_فيبوناتشي(مصفوفة, 1), 0, "الأول")
# apl-source:54
تأكد_يساوي(بحث_فيبوناتشي(مصفوفة, 5), -1, "غير موجود")
# apl-source:55
تأكد_يساوي(بحث_فيبوناتشي(مصفوفة, 100), -1, "أكبر من الكل")
# apl-source:56

# apl-source:57
# يطابق البحث الخطي على كل القيم الموجودة
# apl-source:58
for i in range(len(مصفوفة)):
  # apl-source:59
  تأكد_يساوي(بحث_فيبوناتشي(مصفوفة, مصفوفة[i]), i, "موضع " + str(مصفوفة[i]))
# apl-source:60
