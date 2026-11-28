
# apl-source:1
# مثال 952 — جدولة الفترات
# apl-source:2
# Interval scheduling
# apl-source:3
# Demonstrates: جشع بالأبكر انتهاءً
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/952-interval-scheduling.apl
# apl-source:6

# apl-source:7
# جدولة الفترات: أكبر عدد مهام غير متداخلة
# apl-source:8
# الجشع الأمثل: اختر دائماً الأ earliest انتهاءً
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
def جدول(مهام):
  # apl-source:19
  # فرز بالنهاية (فقاعي)
  # apl-source:20
  م = []
  # apl-source:21
  for مهمة in مهام:
    # apl-source:22
    م = م + [مهمة]
  # apl-source:23
  ن = len(م)
  # apl-source:24
  for i in range(ن):
    # apl-source:25
    for ج in range(i + 1, ن):
      # apl-source:26
      if م[ج][1] < م[i][1]:
        # apl-source:27
        مؤقت = م[i]
        # apl-source:28
        م[i] = م[ج]
        # apl-source:29
        م[ج] = مؤقت
  # apl-source:30
  مختارة = []
  # apl-source:31
  آخر_نهاية = -1
  # apl-source:32
  for مهمة in م:
    # apl-source:33
    if مهمة[0] >= آخر_نهاية:
      # apl-source:34
      مختارة = مختارة + [مهمة]
      # apl-source:35
      آخر_نهاية = مهمة[1]
  # apl-source:36
  return مختارة
# apl-source:37

# apl-source:38
مهام = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 9], [5, 9], [6, 10], [8, 11]]
# apl-source:39
مختارة = جدول(مهام)
# apl-source:40
print("المختارة:", مختارة)
# apl-source:41

# apl-source:42
تأكد_يساوي(len(مختارة), 3, "ثلاث مهام")
# apl-source:43
تأكد_يساوي(مختارة[0][0], 1, "أولى تبدأ 1")
# apl-source:44
تأكد_يساوي(مختارة[0][1], 4, "أولى تنتهي 4")
# apl-source:45
تأكد_يساوي(مختارة[1][0], 5, "ثانية تبدأ 5")
# apl-source:46
تأكد_يساوي(مختارة[2][0], 8, "ثالثة تبدأ 8")
# apl-source:47

# apl-source:48
# لا تداخل
# apl-source:49
for i in range(len(مختارة) - 1):
  # apl-source:50
  if مختارة[i][1] > مختارة[i + 1][0]:
    # apl-source:51
    print("فشل: تداخل")
    # apl-source:52
    قياسي_نظام_اخرج(1)
# apl-source:53
print("ناجح: لا تداخل")
# apl-source:54

# apl-source:55
# مهام متطابقة البداية: الأقصر أولاً
# apl-source:56
تأكد_يساوي(len(جدول([[1, 3], [1, 2], [2, 5]])), 2, "أقصر أولاً")
# apl-source:57
