
# apl-source:1
# مثال 1088 — استخدام الأحرف الكبيرة
# apl-source:2
# Detect capital use
# apl-source:3
# Demonstrates: عد الأحرف الكبيرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1088-detect-capital.apl
# apl-source:6

# apl-source:7
# صحيحة لو كانت كلها كبيرة أو كلها صغيرة أو الأول فقط كبير
# apl-source:8
# نعد الأحرف الكبيرة ونفحص الحالات
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
def كبير(ح):
  # apl-source:19
  return (ح >= "A") and (ح <= "Z")
# apl-source:20

# apl-source:21
def استخدام_صحيح(كلمة):
  # apl-source:22
  عدد_ = 0
  # apl-source:23
  for ح in كلمة:
    # apl-source:24
    if كبير(ح):
      # apl-source:25
      عدد_ = عدد_ + 1
  # apl-source:26
  if (عدد_ == 0) or (عدد_ == len(كلمة)):
    # apl-source:27
    return True
  # apl-source:28
  return (عدد_ == 1) and كبير(كلمة[0])
# apl-source:29

# apl-source:30
تأكد_يساوي(استخدام_صحيح("USA"), True, "كلها كبيرة")
# apl-source:31
تأكد_يساوي(استخدام_صحيح("FlaG"), False, "كبير في النهاية")
# apl-source:32
تأكد_يساوي(استخدام_صحيح("leetcode"), True, "كلها صغيرة")
# apl-source:33
تأكد_يساوي(استخدام_صحيح("Google"), True, "الأول فقط")
# apl-source:34
تأكد_يساوي(استخدام_صحيح("gOogle"), False, "كبير في الوسط")
# apl-source:35
