
# apl-source:1
# مثال 1419 — مطابقة الحالة الجملية
# apl-source:2
# Camelcase matching queries
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1419-camelcase-matching.apl
# apl-source:6

# apl-source:7
# الحروف الصغيرة الزائدة مسموحة
# apl-source:8
# أي حرف كبير زائد يفسد المطابقة
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
def يطابق(استعلام, نمط):
  # apl-source:19
  ج = 0
  # apl-source:20
  for ح in استعلام:
    # apl-source:21
    if (ج < len(نمط)) and (ح == نمط[ج]):
      # apl-source:22
      ج = ج + 1
    # apl-source:23
    elif ح.isupper():
      # apl-source:24
      return False
  # apl-source:25
  return ج == len(نمط)
# apl-source:26

# apl-source:27
def طابق_الكل(استعلامات, نمط):
  # apl-source:28
  ناتج = []
  # apl-source:29
  for س in استعلامات:
    # apl-source:30
    ناتج = ناتج + [يطابق(س, نمط)]
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
تأكد_يساوي(طابق_الكل(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"), [True,False,True,True,False], "نمط FB")
# apl-source:34
تأكد_يساوي(طابق_الكل(["FooBar","FooBarTest"], "FoBa"), [True,False], "نمط FoBa")
# apl-source:35
