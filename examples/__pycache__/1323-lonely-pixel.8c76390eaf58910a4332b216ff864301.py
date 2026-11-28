
# apl-source:1
# مثال 1323 — بكسل وحيد
# apl-source:2
# Lonely pixel count
# apl-source:3
# Demonstrates: شبكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1323-lonely-pixel.apl
# apl-source:6

# apl-source:7
# نعد السود في كل صف وعمود
# apl-source:8
# ونحسب البكسلات التي صفها وعمودها كل منهما بواحد
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
def وحيدة(ل):
  # apl-source:19
  ر_ = len(ل)
  # apl-source:20
  ك_ = len(ل[0])
  # apl-source:21
  صفوف = [0] * ر_
  # apl-source:22
  اعمدة = [0] * ك_
  # apl-source:23
  for ص in range(ر_):
    # apl-source:24
    for ج in range(ك_):
      # apl-source:25
      if ل[ص][ج] == "B":
        # apl-source:26
        صفوف[ص] = صفوف[ص] + 1
        # apl-source:27
        اعمدة[ج] = اعمدة[ج] + 1
  # apl-source:28
  ع = 0
  # apl-source:29
  for ص in range(ر_):
    # apl-source:30
    for ج in range(ك_):
      # apl-source:31
      if (ل[ص][ج] == "B") and (صفوف[ص] == 1) and (اعمدة[ج] == 1):
        # apl-source:32
        ع = ع + 1
  # apl-source:33
  return ع
# apl-source:34

# apl-source:35
تأكد_يساوي(وحيدة([["W","W","B"],["W","B","W"],["B","W","W"]]), 3, "ثلاثة")
# apl-source:36
تأكد_يساوي(وحيدة([["B","B"],["B","B"]]), 0, "مزدحمة")
# apl-source:37
تأكد_يساوي(وحيدة([["W","W"],["W","W"]]), 0, "بيضاء")
# apl-source:38
