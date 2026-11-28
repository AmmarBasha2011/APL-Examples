
# apl-source:1
# مثال 1413 — كلمات صف لوحة المفاتيح
# apl-source:2
# Words typed on one keyboard row
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1413-keyboard-row-words.apl
# apl-source:6

# apl-source:7
# نربط كل حرف برقم صفه
# apl-source:8
# ونتحقق أن كل حروف الكلمة في نفس الصف
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
def كلمات_صف(كلمات):
  # apl-source:19
  صفوف = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
  # apl-source:20
  رقم = {}
  # apl-source:21
  for ع in range(3):
    # apl-source:22
    for ح in صفوف[ع]:
      # apl-source:23
      رقم[ح] = ع
  # apl-source:24
  ناتج = []
  # apl-source:25
  for كلمة in كلمات:
    # apl-source:26
    صغيرة = كلمة.lower()
    # apl-source:27
    اول = رقم[صغيرة[0]]
    # apl-source:28
    سليمة = True
    # apl-source:29
    for ح in صغيرة:
      # apl-source:30
      if رقم[ح] != اول:
        # apl-source:31
        سليمة = False
    # apl-source:32
    if سليمة:
      # apl-source:33
      ناتج = ناتج + [كلمة]
  # apl-source:34
  return ناتج
# apl-source:35

# apl-source:36
تأكد_يساوي(كلمات_صف(["Hello","Alaska","Dad","Peace"]), ["Alaska","Dad"], "كلمتان")
# apl-source:37
تأكد_يساوي(كلمات_صف(["omk"]), [], "لا شيء")
# apl-source:38
تأكد_يساوي(كلمات_صف(["adsdf","sfd"]), ["adsdf","sfd"], "كلتاهما")
# apl-source:39
