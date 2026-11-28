
# apl-source:1
# مثال 921 — الكسر المستمر
# apl-source:2
# Continued fractions
# apl-source:3
# Demonstrates: قسمة صحيحة متكررة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/921-continued-fraction.apl
# apl-source:6

# apl-source:7
# الكسر المستمر: تمثيل العدد [أ0; أ1, أ2, ...] بالقسمة الصحيحة المتكررة
# apl-source:8
# يعطي أفضل التقريبيات الكسرية
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
# كسر مستمر لعدد كسري بسط/مقام بحساب صحيح خالص
# apl-source:19
def كسر_مستمر(بسط, مقام):
  # apl-source:20
  حدود = []
  # apl-source:21
  ب = بسط
  # apl-source:22
  م = مقام
  # apl-source:23
  while م != 0:
    # apl-source:24
    حدود = حدود + [ب // م]
    # apl-source:25
    باقي = ب % م
    # apl-source:26
    ب = م
    # apl-source:27
    م = باقي
  # apl-source:28
  return حدود
# apl-source:29

# apl-source:30
ك = كسر_مستمر(415, 93)
# apl-source:31
print("415/93 =", ك)
# apl-source:32

# apl-source:33
# 415/93 = [4; 2, 6, 7]
# apl-source:34
تأكد_يساوي(len(ك), 4, "أربعة حدود")
# apl-source:35
تأكد_يساوي(ك[0], 4, "أول")
# apl-source:36
تأكد_يساوي(ك[1], 2, "ثانٍ")
# apl-source:37
تأكد_يساوي(ك[2], 6, "ثالث")
# apl-source:38
تأكد_يساوي(ك[3], 7, "رابع")
# apl-source:39

# apl-source:40
# 39/14 = [2; 1, 3, 1, 2]
# apl-source:41
ك2 = كسر_مستمر(39, 14)
# apl-source:42
تأكد_يساوي(len(ك2), 5, "خمسة حدود لـ 39/14")
# apl-source:43
تأكد_يساوي(ك2[0], 2, "39/14 أول")
# apl-source:44

# apl-source:45
# إعادة التقييم من الأسفل تعيد الكسر الأصلي
# apl-source:46
def قيّم(حدود):
  # apl-source:47
  ب = 1
  # apl-source:48
  م = 0
  # apl-source:49
  for i in range(len(حدود)):
    # apl-source:50
    ح = حدود[len(حدود) - 1 - i]
    # apl-source:51
    مؤقت = ب
    # apl-source:52
    ب = ح * ب + م
    # apl-source:53
    م = مؤقت
  # apl-source:54
  return [ب, م]
# apl-source:55

# apl-source:56
ناتج = قيّم(ك)
# apl-source:57
تأكد_يساوي(ناتج[0], 415, "بسط معاد")
# apl-source:58
تأكد_يساوي(ناتج[1], 93, "مقام معاد")
# apl-source:59
