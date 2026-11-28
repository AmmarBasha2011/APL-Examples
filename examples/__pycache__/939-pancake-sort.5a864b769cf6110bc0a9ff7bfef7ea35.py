
# apl-source:1
# مثال 939 — فرز الفطائر
# apl-source:2
# Pancake sort
# apl-source:3
# Demonstrates: قلب البوادئ فقط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/939-pancake-sort.apl
# apl-source:6

# apl-source:7
# فرز الفطائر: الفرز الوحيد المسموح هو قلب بادئة
# apl-source:8
# كل عنصر يصل لموضعه بقلبين كحد أقصى
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
def اقلب(م, حتى):
  # apl-source:19
  نتيجة = []
  # apl-source:20
  for i in range(حتى + 1):
    # apl-source:21
    نتيجة = نتيجة + [م[حتى - i]]
  # apl-source:22
  for i in range(حتى + 1, len(م)):
    # apl-source:23
    نتيجة = نتيجة + [م[i]]
  # apl-source:24
  return نتيجة
# apl-source:25

# apl-source:26
def فرز_فطائر(قيم):
  # apl-source:27
  م = []
  # apl-source:28
  for x in قيم:
    # apl-source:29
    م = م + [x]
  # apl-source:30
  قلبات = 0
  # apl-source:31
  حجم = len(م)
  # apl-source:32
  while حجم > 1:
    # apl-source:33
    # موضع الأكبر في أول حجم عنصر
    # apl-source:34
    أعظم = 0
    # apl-source:35
    for i in range(حجم):
      # apl-source:36
      if م[i] > م[أعظم]:
        # apl-source:37
        أعظم = i
    # apl-source:38
    if أعظم != حجم - 1:
      # apl-source:39
      if أعظم > 0:
        # apl-source:40
        م = اقلب(م, أعظم)
        # apl-source:41
        قلبات = قلبات + 1
      # apl-source:42
      م = اقلب(م, حجم - 1)
      # apl-source:43
      قلبات = قلبات + 1
    # apl-source:44
    حجم = حجم - 1
  # apl-source:45
  return [م, قلبات]
# apl-source:46

# apl-source:47
نتيجة = فرز_فطائر([3, 1, 2])
# apl-source:48
print("المرتبة:", نتيجة[0])
# apl-source:49
print("القلبات:", نتيجة[1])
# apl-source:50

# apl-source:51
تأكد_يساوي(نتيجة[0][0], 1, "أول")
# apl-source:52
تأكد_يساوي(نتيجة[0][1], 2, "ثانٍ")
# apl-source:53
تأكد_يساوي(نتيجة[0][2], 3, "ثالث")
# apl-source:54
تأكد_يساوي(نتيجة[1], 2, "قلبتان تكفيان")
# apl-source:55

# apl-source:56
# مرتبة أصلاً: صفر قلبات
# apl-source:57
تأكد_يساوي(فرز_فطائر([1, 2, 3])[1], 0, "مرتبة بلا قلبات")
# apl-source:58

# apl-source:59
# معكوسة كلياً
# apl-source:60
عكس = فرز_فطائر([4, 3, 2, 1])
# apl-source:61
تأكد_يساوي(عكس[0][0], 1, "عكس أول")
# apl-source:62
تأكد_يساوي(عكس[0][3], 4, "عكس أخير")
# apl-source:63
# حد أعلى نظري: 2ن-3 قلبات
# apl-source:64
if عكس[1] > 5:
  # apl-source:65
  print("فشل: تجاوز الحد النظري")
  # apl-source:66
  قياسي_نظام_اخرج(1)
# apl-source:67
print("ناجح: ضمن الحد النظري")
# apl-source:68
