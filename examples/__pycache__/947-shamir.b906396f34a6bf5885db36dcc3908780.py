
# apl-source:1
# مثال 947 — مشاركة شامير للسر
# apl-source:2
# Shamir secret sharing
# apl-source:3
# Demonstrates: كثير حدود على حقل منتهٍ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/947-shamir.apl
# apl-source:6

# apl-source:7
# مشاركة شامير للسر: كثير حدود على حقل منتهٍ
# apl-source:8
# أي ك حصة تكفي لإعادة السر وأقل منها لا يكشف شيئاً
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
أولي = 257
# apl-source:19

# apl-source:20
def قيّم_حدود(معاملات, س):
  # apl-source:21
  ناتج = 0
  # apl-source:22
  قوة_س = 1
  # apl-source:23
  for معامل in معاملات:
    # apl-source:24
    ناتج = (ناتج + معامل * قوة_س) % أولي
    # apl-source:25
    قوة_س = (قوة_س * س) % أولي
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
# السر 42 بعتبة 3: معاملات [42, 15, 90]
# apl-source:29
معاملات = [42, 15, 90]
# apl-source:30
حصص = []
# apl-source:31
for س in [1, 2, 3, 4]:
  # apl-source:32
  حصص = حصص + [[س, قيّم_حدود(معاملات, س)]]
# apl-source:33
print("الحصص:", حصص)
# apl-source:34

# apl-source:35
تأكد_يساوي(حصص[0][1], 147, "الحصة الأولى")
# apl-source:36
تأكد_يساوي(حصص[1][1], 175, "الحصة الثانية")
# apl-source:37
تأكد_يساوي(حصص[2][1], 126, "الحصة الثالثة")
# apl-source:38
تأكد_يساوي(حصص[3][1], 0, "الحصة الرابعة")
# apl-source:39

# apl-source:40
# إعادة البناء عند س=0 باستيفاء لاغرانج من أول 3 حصص
# apl-source:41
def معكوس(أ):
  # apl-source:42
  # صغيرة فيرما: أ^(أولي-2)
  # apl-source:43
  ناتج = 1
  # apl-source:44
  ب = أ % أولي
  # apl-source:45
  ه = أولي - 2
  # apl-source:46
  while ه > 0:
    # apl-source:47
    if ه % 2 == 1:
      # apl-source:48
      ناتج = (ناتج * ب) % أولي
    # apl-source:49
    ب = (ب * ب) % أولي
    # apl-source:50
    ه = ه // 2
  # apl-source:51
  return ناتج
# apl-source:52

# apl-source:53
def أعد_السر(حصص_مختارة):
  # apl-source:54
  سر = 0
  # apl-source:55
  for i in range(3):
    # apl-source:56
    بسط = 1
    # apl-source:57
    مقام = 1
    # apl-source:58
    for ج in range(3):
      # apl-source:59
      if i != ج:
        # apl-source:60
        بسط = (بسط * (أولي - حصص_مختارة[ج][0])) % أولي
        # apl-source:61
        مقام = (مقام * (حصص_مختارة[i][0] - حصص_مختارة[ج][0])) % أولي
    # apl-source:62
    حد = (حصص_مختارة[i][1] * بسط * معكوس(مقام)) % أولي
    # apl-source:63
    سر = (سر + حد) % أولي
  # apl-source:64
  return سر
# apl-source:65

# apl-source:66
سر = أعد_السر([حصص[0], حصص[1], حصص[2]])
# apl-source:67
print("السر المعاد:", سر)
# apl-source:68
تأكد_يساوي(سر, 42, "السر من الحصص 1-3")
# apl-source:69

# apl-source:70
# أي ثلاث حصص تعيد السر
# apl-source:71
تأكد_يساوي(أعد_السر([حصص[1], حصص[2], حصص[3]]), 42, "السر من الحصص 2-4")
# apl-source:72
تأكد_يساوي(أعد_السر([حصص[0], حصص[1], حصص[3]]), 42, "السر من الحصص 1,2,4")
# apl-source:73
