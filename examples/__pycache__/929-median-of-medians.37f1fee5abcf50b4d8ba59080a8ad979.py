
# apl-source:1
# مثال 929 — وسيط الوسائط
# apl-source:2
# Median of medians
# apl-source:3
# Demonstrates: محور مضمون الجودة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/929-median-of-medians.apl
# apl-source:6

# apl-source:7
# وسيط الوسائط: اختيار العنصر k بضمان خطي في أسوأ حالة
# apl-source:8
# يقسم حول وسيط وسائط مجموعات الخمسات
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
def رتب(قيم):
  # apl-source:19
  م = []
  # apl-source:20
  for x in قيم:
    # apl-source:21
    م = م + [x]
  # apl-source:22
  ن = len(م)
  # apl-source:23
  for i in range(ن):
    # apl-source:24
    for ج in range(i + 1, ن):
      # apl-source:25
      if م[ج] < م[i]:
        # apl-source:26
        مؤقت = م[i]
        # apl-source:27
        م[i] = م[ج]
        # apl-source:28
        م[ج] = مؤقت
  # apl-source:29
  return م
# apl-source:30

# apl-source:31
def اختر(قيم, ك):
  # apl-source:32
  if len(قيم) <= 5:
    # apl-source:33
    return رتب(قيم)[ك]
  # apl-source:34
  وسائط = []
  # apl-source:35
  i = 0
  # apl-source:36
  while i < len(قيم):
    # apl-source:37
    نهاية = i + 5
    # apl-source:38
    if نهاية > len(قيم):
      # apl-source:39
      نهاية = len(قيم)
    # apl-source:40
    مجموعة = رتب(قيم[i:نهاية])
    # apl-source:41
    وسائط = وسائط + [مجموعة[len(مجموعة) // 2]]
    # apl-source:42
    i = i + 5
  # apl-source:43
  محور = اختر(وسائط, len(وسائط) // 2)
  # apl-source:44
  أصغر = []
  # apl-source:45
  مساو = []
  # apl-source:46
  أكبر = []
  # apl-source:47
  for x in قيم:
    # apl-source:48
    if x < محور:
      # apl-source:49
      أصغر = أصغر + [x]
    # apl-source:50
    elif x == محور:
      # apl-source:51
      مساو = مساو + [x]
    # apl-source:52
    else:
      # apl-source:53
      أكبر = أكبر + [x]
  # apl-source:54
  if ك < len(أصغر):
    # apl-source:55
    return اختر(أصغر, ك)
  # apl-source:56
  if ك < len(أصغر) + len(مساو):
    # apl-source:57
    return محور
  # apl-source:58
  return اختر(أكبر, ك - len(أصغر) - len(مساو))
# apl-source:59

# apl-source:60
قيم = [7, 2, 1, 6, 8, 5, 3, 4]
# apl-source:61
print("الخامس تصاعدياً:", اختر(قيم, 4))
# apl-source:62

# apl-source:63
# المرتبة تصاعدياً: [1,2,3,4,5,6,7,8] والموضع 4 هو 5
# apl-source:64
تأكد_يساوي(اختر(قيم, 4), 5, "الوسيط")
# apl-source:65
تأكد_يساوي(اختر(قيم, 0), 1, "الأصغر")
# apl-source:66
تأكد_يساوي(اختر(قيم, 7), 8, "الأكبر")
# apl-source:67

# apl-source:68
# يطابق الفرز على كل المواضع
# apl-source:69
مرتبة = رتب(قيم)
# apl-source:70
for i in range(len(قيم)):
  # apl-source:71
  تأكد_يساوي(اختر(قيم, i), مرتبة[i], "موضع " + str(i))
# apl-source:72

# apl-source:73
# مع تكرارات
# apl-source:74
مكررة = [3, 1, 3, 3, 1]
# apl-source:75
تأكد_يساوي(اختر(مكررة, 2), 3, "وسيط مكررة")
# apl-source:76
