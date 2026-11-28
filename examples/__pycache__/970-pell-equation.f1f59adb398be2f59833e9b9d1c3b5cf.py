
# apl-source:1
# مثال 970 — معادلة بل
# apl-source:2
# Pell equation
# apl-source:3
# Demonstrates: بحث بجذر صحيح متزايد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/970-pell-equation.apl
# apl-source:6

# apl-source:7
# معادلة بل: س^2 - د ص^2 = 1 لأصغر الحلول الصحيحة
# apl-source:8
# بحث مباشر مع جذر صحيح بالتزايد
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
def جذر_صحيح(ن):
  # apl-source:19
  ك = 0
  # apl-source:20
  while ((ك + 1) * (ك + 1)) <= ن:
    # apl-source:21
    ك = ك + 1
  # apl-source:22
  return ك
# apl-source:23

# apl-source:24
def بل(د, حد):
  # apl-source:25
  حلول = []
  # apl-source:26
  ص = 1
  # apl-source:27
  while (ص <= حد) and (len(حلول) < 3):
    # apl-source:28
    مربع = 1 + (د * ص * ص)
    # apl-source:29
    س = جذر_صحيح(مربع)
    # apl-source:30
    if (س * س) == مربع:
      # apl-source:31
      حلول = حلول + [[س, ص]]
    # apl-source:32
    ص = ص + 1
  # apl-source:33
  return حلول
# apl-source:34

# apl-source:35
حلول = بل(2, 100)
# apl-source:36
تأكد_يساوي(len(حلول), 3, "ثلاثة حلول")
# apl-source:37
تأكد_يساوي(حلول[0][0], 3, "س الأول")
# apl-source:38
تأكد_يساوي(حلول[0][1], 2, "ص الأول")
# apl-source:39
تأكد_يساوي(حلول[1][0], 17, "س الثاني")
# apl-source:40
تأكد_يساوي(حلول[2][0], 99, "س الثالث")
# apl-source:41
تأكد_يساوي((9) - (8), 1, "تحقق المعادلة")
# apl-source:42
