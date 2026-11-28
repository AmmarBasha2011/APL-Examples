
# apl-source:1
# مثال 886 — متتابعة كولاكوسكي
# apl-source:2
# Kolakoski sequence
# apl-source:3
# Demonstrates: وصف ذاتي بأطوال الركضات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/886-kolakoski.apl
# apl-source:6

# apl-source:7
# متتابعة كولاكوسكي: متتابعة ذاتية الوصف من الواحدات والثنائيات
# apl-source:8
# أطوال ركضاتها هي المتتابعة نفسها
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
def كولاكوسكي(عدد):
  # apl-source:19
  ت = [1, 2, 2]
  # apl-source:20
  موضع = 2
  # apl-source:21
  while len(ت) < عدد:
    # apl-source:22
    تالية = 3 - ت[len(ت) - 1]
    # apl-source:23
    تكرار = ت[موضع]
    # apl-source:24
    for _ in range(تكرار):
      # apl-source:25
      if len(ت) < عدد:
        # apl-source:26
        ت = ت + [تالية]
    # apl-source:27
    موضع = موضع + 1
  # apl-source:28
  return ت
# apl-source:29

# apl-source:30
ت = كولاكوسكي(15)
# apl-source:31
print("أول 15 حداً:", ت)
# apl-source:32

# apl-source:33
تأكد_يساوي(len(ت), 15, "الطول")
# apl-source:34
تأكد_يساوي(ت[0], 1, "تبدأ 1")
# apl-source:35
تأكد_يساوي(ت[2], 2, "ت[2] = 2")
# apl-source:36
تأكد_يساوي(ت[4], 1, "ت[4] = 1")
# apl-source:37
تأكد_يساوي(ت[8], 2, "ت[8] = 2")
# apl-source:38
تأكد_يساوي(ت[14], 2, "ت[14] = 2")
# apl-source:39

# apl-source:40
# الوصف الذاتي: أطوال الركضات تعيد المتتابعة
# apl-source:41
ركضات = []
# apl-source:42
جارية = ت[0]
# apl-source:43
عد = 1
# apl-source:44
for i in range(1, len(ت)):
  # apl-source:45
  if ت[i] == جارية:
    # apl-source:46
    عد = عد + 1
  # apl-source:47
  else:
    # apl-source:48
    ركضات = ركضات + [عد]
    # apl-source:49
    جارية = ت[i]
    # apl-source:50
    عد = 1
# apl-source:51
ركضات = ركضات + [عد]
# apl-source:52
print("أطوال الركضات:", ركضات)
# apl-source:53

# apl-source:54
# كل ركضة مكتملة (ما عدا ربما الأخيرة) يطابق طولها الحد الموافق
# apl-source:55
for i in range(len(ركضات) - 1):
  # apl-source:56
  تأكد_يساوي(ركضات[i], ت[i], "الوصف الذاتي عند " + str(i))
# apl-source:57
