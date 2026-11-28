
# apl-source:1
# مثال 842 — غربال أتكن
# apl-source:2
# Sieve of Atkin
# apl-source:3
# Demonstrates: معادلات تربيعية modulo 60
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/842-sieve-of-atkin.apl
# apl-source:6

# apl-source:7
# غربال أتكن: غربال أولي حديث يعتمد معادلات تربيعية modulo 60
# apl-source:8
# أسرع نظرياً من غربال إراتوستينس للنطاقات الكبيرة
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
def غربال_أتكن(حد):
  # apl-source:19
  مرشح = []
  # apl-source:20
  for _ in range(حد + 1):
    # apl-source:21
    مرشح = مرشح + [False]
  # apl-source:22
  if حد > 2:
    # apl-source:23
    مرشح[2] = 1 == 1
  # apl-source:24
  if حد > 3:
    # apl-source:25
    مرشح[3] = 1 == 1
  # apl-source:26
  if حد > 5:
    # apl-source:27
    مرشح[5] = 1 == 1
  # apl-source:28
  for س in range(1, حد + 1):
    # apl-source:29
    س2 = س * س
    # apl-source:30
    # أقصى س نافع: الحالة الثالثة تحتاج 2س²+2س-1 <= حد (عند ص=س-1)
    # apl-source:31
    if 2 * س2 + 2 * س - 1 <= حد:
      # apl-source:32
      for ص in range(1, حد + 1):
        # apl-source:33
        ص2 = ص * ص
        # apl-source:34
        # ن = 4س² + ص²
        # apl-source:35
        ن = 4 * س2 + ص2
        # apl-source:36
        if ن <= حد:
          # apl-source:37
          باقي = ن % 60
          # apl-source:38
          if باقي == 1 or باقي == 13 or باقي == 17 or باقي == 29 or باقي == 37 or باقي == 41 or باقي == 49 or باقي == 53:
            # apl-source:39
            مرشح[ن] = not مرشح[ن]
        # apl-source:40
        # ن = 3س² + ص²
        # apl-source:41
        ن = 3 * س2 + ص2
        # apl-source:42
        if ن <= حد:
          # apl-source:43
          باقي = ن % 60
          # apl-source:44
          if باقي == 7 or باقي == 19 or باقي == 31 or باقي == 43:
            # apl-source:45
            مرشح[ن] = not مرشح[ن]
        # apl-source:46
        # ن = 3س² - ص² (فقط عندما س > ص)
        # apl-source:47
        if س > ص:
          # apl-source:48
          ن = 3 * س2 - ص2
          # apl-source:49
          if ن <= حد:
            # apl-source:50
            باقي = ن % 60
            # apl-source:51
            if باقي == 11 or باقي == 23 or باقي == 47 or باقي == 59:
              # apl-source:52
              مرشح[ن] = not مرشح[ن]
  # apl-source:53
  # إلغاء مربعات الأولية
  # apl-source:54
  أولية = []
  # apl-source:55
  for ن in range(6, حد + 1):
    # apl-source:56
    if مرشح[ن]:
      # apl-source:57
      أولية = أولية + [ن]
      # apl-source:58
      مربع = ن * ن
      # apl-source:59
      مضاعف = مربع
      # apl-source:60
      while مضاعف <= حد:
        # apl-source:61
        مرشح[مضاعف] = False
        # apl-source:62
        مضاعف = مضاعف + مربع
  # apl-source:63
  نتيجة = []
  # apl-source:64
  if حد >= 2:
    # apl-source:65
    نتيجة = نتيجة + [2]
  # apl-source:66
  if حد >= 3:
    # apl-source:67
    نتيجة = نتيجة + [3]
  # apl-source:68
  if حد >= 5:
    # apl-source:69
    نتيجة = نتيجة + [5]
  # apl-source:70
  for ن in أولية:
    # apl-source:71
    if مرشح[ن]:
      # apl-source:72
      نتيجة = نتيجة + [ن]
  # apl-source:73
  return نتيجة
# apl-source:74

# apl-source:75
أولية100 = غربال_أتكن(100)
# apl-source:76
print("أولية حتى 100:", أولية100)
# apl-source:77

# apl-source:78
تأكد_يساوي(len(أولية100), 25, "عدد الأولية حتى 100 هو 25")
# apl-source:79
تأكد_يساوي(أولية100[0], 2, "أول أولي")
# apl-source:80
تأكد_يساوي(أولية100[24], 97, "آخر أولي قبل 100")
# apl-source:81
تأكد_يساوي(أولية100[8], 23, "الأولي التاسع")
# apl-source:82
تأكد_يساوي(أولية100[13], 43, "الأولي الرابع عشر")
# apl-source:83
