
# apl-source:1
# مثال 873 — طريقة أويلر
# apl-source:2
# Euler method
# apl-source:3
# Demonstrates: خطوة بميل ثابت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/873-euler-method.apl
# apl-source:6

# apl-source:7
# طريقة أويلر: أبسط تكامل عددي للمعادلات التفاضلية
# apl-source:8
# y' = y تعني النمو الأسي: e ≈ 2.5937 بخطوة 0.1
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
# y' = y ، y(0) = 1 ، حتى س = 1
# apl-source:19
def أويلر(ميلاد, خطوة, خطوات):
  # apl-source:20
  قيمة = ميلاد
  # apl-source:21
  for _ in range(خطوات):
    # apl-source:22
    قيمة = قيمة + خطوة * قيمة
  # apl-source:23
  return قيمة
# apl-source:24

# apl-source:25
ط1 = أويلر(1.0, 0.1, 10)
# apl-source:26
ط2 = أويلر(1.0, 0.01, 100)
# apl-source:27
ط3 = أويلر(1.0, 0.001, 1000)
# apl-source:28
print("خطوة 0.1:", ط1)
# apl-source:29
print("خطوة 0.01:", ط2)
# apl-source:30
print("خطوة 0.001:", ط3)
# apl-source:31

# apl-source:32
# (1.1)^10 = 2.5937424601
# apl-source:33
تأكد_يساوي(round(ط1, 6), 2.593742, "خطوة 0.1 تعطي 2.5937")
# apl-source:34

# apl-source:35
# الدقة تتحسن مع صغر الخطوة نحو e = 2.71828
# apl-source:36
تأكد_يساوي(ط2 > ط1, 1 == 1, "خطوة أصغر أدق")
# apl-source:37
تأكد_يساوي(ط3 > ط2, 1 == 1, "الأدق أقرب لـ e")
# apl-source:38
تأكد_يساوي(ط3 < 2.7183, 1 == 1, "لكنها تظل دون e")
# apl-source:39
