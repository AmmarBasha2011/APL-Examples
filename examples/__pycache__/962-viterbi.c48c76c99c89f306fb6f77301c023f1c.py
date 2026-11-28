
# apl-source:1
# مثال 962 — خوارزمية فيتربي
# apl-source:2
# Viterbi algorithm
# apl-source:3
# Demonstrates: أرجح مسار حالات خفية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/962-viterbi.apl
# apl-source:6

# apl-source:7
# خوارزمية فيتربي: أكثر تسلسل حالات خفية احتمالاً لملاحظات متتابعة
# apl-source:8
# نموذج الطقس الكلاسيكي: حالتان وثلاث ملاحظات
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
# 0 = ممطر، 1 = مشمس
# apl-source:19
بداية = [0.6, 0.4]
# apl-source:20
انتقال = [[0.7, 0.3], [0.4, 0.6]]
# apl-source:21
انبعاث = [[0.1, 0.4, 0.5], [0.6, 0.3, 0.1]]
# apl-source:22
ملاحظات = [0, 1, 2]
# apl-source:23

# apl-source:24
جدول = [[0, 0], [0, 0], [0, 0]]
# apl-source:25
مؤشرات = [[0, 0], [0, 0], [0, 0]]
# apl-source:26
for ح in range(2):
  # apl-source:27
  جدول[0][ح] = بداية[ح] * انبعاث[ح][ملاحظات[0]]
# apl-source:28
for ت in range(1, 3):
  # apl-source:29
  for ح in range(2):
    # apl-source:30
    أفضل = -1
    # apl-source:31
    أفضل_ج = 0
    # apl-source:32
    for ج in range(2):
      # apl-source:33
      ق = جدول[ت - 1][ج] * انتقال[ج][ح]
      # apl-source:34
      if ق > أفضل:
        # apl-source:35
        أفضل = ق
        # apl-source:36
        أفضل_ج = ج
    # apl-source:37
    جدول[ت][ح] = أفضل * انبعاث[ح][ملاحظات[ت]]
    # apl-source:38
    مؤشرات[ت][ح] = أفضل_ج
# apl-source:39

# apl-source:40
if جدول[2][0] > جدول[2][1]:
  # apl-source:41
  أخير = 0
# apl-source:42
else:
  # apl-source:43
  أخير = 1
# apl-source:44
مسار = [أخير]
# apl-source:45
حالي = أخير
# apl-source:46
for ت in range(2, 0, -1):
  # apl-source:47
  حالي = مؤشرات[ت][حالي]
  # apl-source:48
  مسار = مسار + [حالي]
# apl-source:49

# apl-source:50
تأكد_يساوي(مسار[2], 1, "اليوم الأول مشمس")
# apl-source:51
تأكد_يساوي(مسار[1], 0, "اليوم الثاني ممطر")
# apl-source:52
تأكد_يساوي(مسار[0], 0, "اليوم الثالث ممطر")
# apl-source:53
تأكد_يساوي(round(جدول[2][0], 6), 0.01344, "احتمال المسار الأرجح")
# apl-source:54
