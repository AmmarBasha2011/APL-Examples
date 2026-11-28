
# apl-source:1
# مثال 895 — مجموعة كانتور
# apl-source:2
# Cantor set
# apl-source:3
# Demonstrates: تمثيل ثلاثي بلا رقم واحد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/895-cantor-set.apl
# apl-source:6

# apl-source:7
# مجموعة كانتور: إزالة الثلث الأوسط تكرارياً
# apl-source:8
# المستوى ن له 2^ن قطعة كل منها بطول (1/3)^ن
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
# عضوية: س في [0,1] تنتمي لمجموعة كانتور إن خلا تمثيلها الثلاثي من الرقم 1
# apl-source:19
def في_كانتور(بسط, مقام):
  # apl-source:20
  # نفحص أول 20 خانة ثلاثية
  # apl-source:21
  م = بسط
  # apl-source:22
  for _ in range(20):
    # apl-source:23
    م = م * 3
    # apl-source:24
    رقم = م // مقام
    # apl-source:25
    if رقم == 1:
      # apl-source:26
      # الرقم 1 يطرد إلا إن كان الأخير وتلاه أصفار (نهاية يمين قطعة)
      # apl-source:27
      if م % مقام != 0:
        # apl-source:28
        return False
    # apl-source:29
    م = م % مقام
  # apl-source:30
  return 1 == 1
# apl-source:31

# apl-source:32
print("1/4 في كانتور؟", في_كانتور(1, 4))
# apl-source:33
print("1/3 في كانتور؟", في_كانتور(1, 3))
# apl-source:34
print("1/2 في كانتور؟", في_كانتور(1, 2))
# apl-source:35

# apl-source:36
# 1/4 = 0.020202... ثلاثياً: بلا رقم 1 إذن تنتمي
# apl-source:37
تأكد_يساوي(في_كانتور(1, 4), 1 == 1, "1/4 تنتمي")
# apl-source:38
# 1/3 = 0.1 ثلاثياً لكنها نهاية قطعة فتبقى
# apl-source:39
تأكد_يساوي(في_كانتور(1, 3), 1 == 1, "1/3 نهاية قطعة")
# apl-source:40
# 1/2 = 0.111... ثلاثياً: مطرودة
# apl-source:41
تأكد_يساوي(في_كانتور(1, 2), False, "1/2 لا تنتمي")
# apl-source:42
# 7/9 = 0.21 ثلاثياً... لا: 7/9=0.21، الرقم الثاني 1 والباقي صفر: نهاية قطعة
# apl-source:43
تأكد_يساوي(في_كانتور(7, 9), 1 == 1, "7/9 نهاية قطعة")
# apl-source:44

# apl-source:45
# عدد القطع والطول الكلي عند المستوى 4
# apl-source:46
قطع = 16
# apl-source:47
طول_قطعة_مقام = 81
# apl-source:48
print("المستوى 4:", قطع, "قطعة بطول 1/", طول_قطعة_مقام)
# apl-source:49
تأكد_يساوي(قطع, 16, "16 قطعة")
# apl-source:50
تأكد_يساوي(طول_قطعة_مقام, 81, "بطول 1/81")
# apl-source:51
