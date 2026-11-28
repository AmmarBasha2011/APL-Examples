
# apl-source:1
# مثال 884 — تمثيل زيكندورف
# apl-source:2
# Zeckendorf representation
# apl-source:3
# Demonstrates: فيبوناتشي غير متتالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/884-zeckendorf.apl
# apl-source:6

# apl-source:7
# تمثيل زيكندورف: كل عدد مجموع أرقام فيبوناتشي غير متتالية
# apl-source:8
# الجشع (أكبر فيبوناتشي أولاً) يعطي التمثيل الفريد
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
def زيكندورف(ن):
  # apl-source:19
  فيب = [1, 2]
  # apl-source:20
  while فيب[len(فيب) - 1] <= ن:
    # apl-source:21
    فيب = فيب + [فيب[len(فيب) - 1] + فيب[len(فيب) - 2]]
  # apl-source:22
  أجزاء = []
  # apl-source:23
  متبقي = ن
  # apl-source:24
  for i in range(len(فيب)):
    # apl-source:25
    ق = فيب[len(فيب) - 1 - i]
    # apl-source:26
    if ق <= متبقي:
      # apl-source:27
      أجزاء = أجزاء + [ق]
      # apl-source:28
      متبقي = متبقي - ق
  # apl-source:29
  return أجزاء
# apl-source:30

# apl-source:31
ز100 = زيكندورف(100)
# apl-source:32
ز50 = زيكندورف(50)
# apl-source:33
print("100 =", ز100)
# apl-source:34
print("50 =", ز50)
# apl-source:35

# apl-source:36
تأكد_يساوي(len(ز100), 3, "100 بثلاثة أجزاء")
# apl-source:37
تأكد_يساوي(ز100[0], 89, "أكبر جزء 89")
# apl-source:38
تأكد_يساوي(ز100[1], 8, "ثم 8")
# apl-source:39
تأكد_يساوي(ز100[2], 3, "ثم 3")
# apl-source:40
تأكد_يساوي(ز50[0], 34, "50 تبدأ بـ 34")
# apl-source:41
تأكد_يساوي(ز50[1], 13, "ثم 13")
# apl-source:42

# apl-source:43
def مجموع(قائمة):
  # apl-source:44
  ج = 0
  # apl-source:45
  for ق in قائمة:
    # apl-source:46
    ج = ج + ق
  # apl-source:47
  return ج
# apl-source:48

# apl-source:49
تأكد_يساوي(مجموع(ز100), 100, "المجموع يعيد 100")
# apl-source:50
تأكد_يساوي(مجموع(ز50), 50, "المجموع يعيد 50")
# apl-source:51

# apl-source:52
# لا جزأين متتاليين في متتابعة فيبوناتشي
# apl-source:53
فيب = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# apl-source:54
def فهرس_فيب(ق):
  # apl-source:55
  for i in range(len(فيب)):
    # apl-source:56
    if فيب[i] == ق:
      # apl-source:57
      return i
  # apl-source:58
  return -1
# apl-source:59

# apl-source:60
for i in range(len(ز100) - 1):
  # apl-source:61
  فرق = فهرس_فيب(ز100[i]) - فهرس_فيب(ز100[i + 1])
  # apl-source:62
  تأكد_يساوي(فرق > 1, 1 == 1, "لا متتالية بين الجزأين " + str(i))
# apl-source:63
