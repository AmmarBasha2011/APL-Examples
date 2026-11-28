
# apl-source:1
# مثال 866 — المجموع الثلاثي
# apl-source:2
# 3Sum
# apl-source:3
# Demonstrates: فرز ومؤشران متقابلان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/866-three-sum.apl
# apl-source:6

# apl-source:7
# مجموع ثلاثي: كل ثلاثيات فريدة مجموعها صفر
# apl-source:8
# فرز + مؤشران متقابلان لكل عنصر أول
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
def فرز(قائمة):
  # apl-source:19
  م = []
  # apl-source:20
  for ق in قائمة:
    # apl-source:21
    م = م + [ق]
  # apl-source:22
  ن = len(م)
  # apl-source:23
  for i in range(ن):
    # apl-source:24
    for ج in range(ن - 1):
      # apl-source:25
      if م[ج] > م[ج + 1]:
        # apl-source:26
        مؤقت = م[ج]
        # apl-source:27
        م[ج] = م[ج + 1]
        # apl-source:28
        م[ج + 1] = مؤقت
  # apl-source:29
  return م
# apl-source:30

# apl-source:31
def مجموع_ثلاثي(أرقام):
  # apl-source:32
  م = فرز(أرقام)
  # apl-source:33
  ن = len(م)
  # apl-source:34
  نتائج = []
  # apl-source:35
  for i in range(ن - 2):
    # apl-source:36
    if i == 0 or م[i] != م[i - 1]:
      # apl-source:37
      يسار = i + 1
      # apl-source:38
      يمين = ن - 1
      # apl-source:39
      while يسار < يمين:
        # apl-source:40
        مجموع = م[i] + م[يسار] + م[يمين]
        # apl-source:41
        if مجموع < 0:
          # apl-source:42
          يسار = يسار + 1
        # apl-source:43
        elif مجموع > 0:
          # apl-source:44
          يمين = يمين - 1
        # apl-source:45
        else:
          # apl-source:46
          نتائج = نتائج + [[م[i], م[يسار], م[يمين]]]
          # apl-source:47
          while يسار < يمين and م[يسار] == م[يسار + 1]:
            # apl-source:48
            يسار = يسار + 1
          # apl-source:49
          while يسار < يمين and م[يمين] == م[يمين - 1]:
            # apl-source:50
            يمين = يمين - 1
          # apl-source:51
          يسار = يسار + 1
          # apl-source:52
          يمين = يمين - 1
  # apl-source:53
  return نتائج
# apl-source:54

# apl-source:55
نتائج = مجموع_ثلاثي([-1, 0, 1, 2, -1, -4])
# apl-source:56
print("الثلاثيات:", نتائج)
# apl-source:57

# apl-source:58
تأكد_يساوي(len(نتائج), 2, "ثلاثيتان")
# apl-source:59
تأكد_يساوي(نتائج[0][0], -1, "الأولى تبدأ بـ -1")
# apl-source:60
تأكد_يساوي(نتائج[0][1], -1, "الأولى: -1,-1,2")
# apl-source:61
تأكد_يساوي(نتائج[1][2], 1, "الثانية: -1,0,1")
# apl-source:62

# apl-source:63
تأكد_يساوي(len(مجموع_ثلاثي([1, 2, 3])), 0, "لا ثلاثية صفرية")
# apl-source:64
