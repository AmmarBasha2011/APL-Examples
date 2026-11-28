
# apl-source:1
# مثال 909 — مسألة العلم الهولندي
# apl-source:2
# Dutch national flag
# apl-source:3
# Demonstrates: ثلاثة مؤشرات بتمريرة واحدة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/909-dutch-national-flag.apl
# apl-source:6

# apl-source:7
# مسألة العلم الهولندي: فرز ثلاث قيم بتمريرة واحدة
# apl-source:8
# ثلاثة مؤشرات: أدنى، وسط، أعلى
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
def علم_هولندي(قيم):
  # apl-source:19
  م = []
  # apl-source:20
  for x in قيم:
    # apl-source:21
    م = م + [x]
  # apl-source:22
  أدنى = 0
  # apl-source:23
  وسط = 0
  # apl-source:24
  أعلى = len(م) - 1
  # apl-source:25
  while وسط <= أعلى:
    # apl-source:26
    if م[وسط] == 0:
      # apl-source:27
      مؤقت = م[أدنى]
      # apl-source:28
      م[أدنى] = م[وسط]
      # apl-source:29
      م[وسط] = مؤقت
      # apl-source:30
      أدنى = أدنى + 1
      # apl-source:31
      وسط = وسط + 1
    # apl-source:32
    elif م[وسط] == 1:
      # apl-source:33
      وسط = وسط + 1
    # apl-source:34
    else:
      # apl-source:35
      مؤقت = م[وسط]
      # apl-source:36
      م[وسط] = م[أعلى]
      # apl-source:37
      م[أعلى] = مؤقت
      # apl-source:38
      أعلى = أعلى - 1
  # apl-source:39
  return م
# apl-source:40

# apl-source:41
نتيجة = علم_هولندي([2, 0, 2, 1, 1, 0])
# apl-source:42
print("النتيجة:", نتيجة)
# apl-source:43

# apl-source:44
تأكد_يساوي(len(نتيجة), 6, "الطول")
# apl-source:45
تأكد_يساوي(نتيجة[0], 0, "صفر أولاً")
# apl-source:46
تأكد_يساوي(نتيجة[1], 0, "صفر ثانياً")
# apl-source:47
تأكد_يساوي(نتيجة[2], 1, "واحد")
# apl-source:48
تأكد_يساوي(نتيجة[5], 2, "اثنان أخيراً")
# apl-source:49

# apl-source:50
# حالات حدية
# apl-source:51
تأكد_يساوي(len(علم_هولندي([])), 0, "فارغة")
# apl-source:52
تأكد_يساوي(علم_هولندي([1])[0], 1, "عنصر واحد")
# apl-source:53
مرتبة = علم_هولندي([2, 2, 2])
# apl-source:54
تأكد_يساوي(مرتبة[0], 2, "كلها متساوية")
# apl-source:55
تأكد_يساوي(len(مرتبة), 3, "طول المتساوية")
# apl-source:56
