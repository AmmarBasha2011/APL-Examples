
# apl-source:1
# مثال 910 — فرز الدورات
# apl-source:2
# Cycle sort
# apl-source:3
# Demonstrates: تدوير العناصر لمواضعها
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/910-cycle-sort.apl
# apl-source:6

# apl-source:7
# فرز الدورات: أقل عدد ممكن من الكتابات على المصفوفة
# apl-source:8
# مفيد حين الكتابة مكلفة (ذاكرة فلاش)
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
def فرز_دورات(قيم):
  # apl-source:19
  م = []
  # apl-source:20
  for x in قيم:
    # apl-source:21
    م = م + [x]
  # apl-source:22
  ن = len(م)
  # apl-source:23
  كتابات = 0
  # apl-source:24
  for بداية in range(ن - 1):
    # apl-source:25
    عنصر = م[بداية]
    # apl-source:26
    موضع = بداية
    # apl-source:27
    for i in range(بداية + 1, ن):
      # apl-source:28
      if م[i] < عنصر:
        # apl-source:29
        موضع = موضع + 1
    # apl-source:30
    if موضع == بداية:
      # apl-source:31
      # لا دورة هنا
      # apl-source:32
      كتابات = كتابات + 0
    # apl-source:33
    else:
      # apl-source:34
      while عنصر == م[موضع]:
        # apl-source:35
        موضع = موضع + 1
      # apl-source:36
      مؤقت = م[موضع]
      # apl-source:37
      م[موضع] = عنصر
      # apl-source:38
      عنصر = مؤقت
      # apl-source:39
      كتابات = كتابات + 1
      # apl-source:40
      while موضع != بداية:
        # apl-source:41
        موضع = بداية
        # apl-source:42
        for i in range(بداية + 1, ن):
          # apl-source:43
          if م[i] < عنصر:
            # apl-source:44
            موضع = موضع + 1
        # apl-source:45
        while عنصر == م[موضع]:
          # apl-source:46
          موضع = موضع + 1
        # apl-source:47
        مؤقت = م[موضع]
        # apl-source:48
        م[موضع] = عنصر
        # apl-source:49
        عنصر = مؤقت
        # apl-source:50
        كتابات = كتابات + 1
  # apl-source:51
  return [م, كتابات]
# apl-source:52

# apl-source:53
نتيجة = فرز_دورات([4, 3, 2, 1])
# apl-source:54
م = نتيجة[0]
# apl-source:55
ك = نتيجة[1]
# apl-source:56
print("المرتبة:", م)
# apl-source:57
print("الكتابات:", ك)
# apl-source:58

# apl-source:59
تأكد_يساوي(م[0], 1, "أول")
# apl-source:60
تأكد_يساوي(م[3], 4, "أخير")
# apl-source:61
تأكد_يساوي(ك, 4, "أربع كتابات بالضبط")
# apl-source:62

# apl-source:63
# مرتبة أصلاً: صفر كتابات
# apl-source:64
نتيجة2 = فرز_دورات([1, 2, 3])
# apl-source:65
تأكد_يساوي(نتيجة2[1], 0, "لا كتابات للمرتبة")
# apl-source:66

# apl-source:67
# مع تكرارات
# apl-source:68
نتيجة3 = فرز_دورات([3, 1, 3, 1])
# apl-source:69
تأكد_يساوي(نتيجة3[0][0], 1, "تكرار أول")
# apl-source:70
تأكد_يساوي(نتيجة3[0][3], 3, "تكرار أخير")
# apl-source:71
