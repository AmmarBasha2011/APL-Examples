
# apl-source:1
# مثال 1418 — أقصر كلمة مكتملة
# apl-source:2
# Shortest completing word
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1418-shortest-completing-word.apl
# apl-source:6

# apl-source:7
# نعد حروف اللوحة الأبجدية بحروف صغيرة
# apl-source:8
# نفحص الكلمات بالترتيب ونحتفظ بأقصرها
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
def عد_الحروف(نص_):
  # apl-source:19
  عدّ = {}
  # apl-source:20
  for ح in نص_.lower():
    # apl-source:21
    if ح.isalpha():
      # apl-source:22
      عدّ[ح] = عدّ.get(ح, 0) + 1
  # apl-source:23
  return عدّ
# apl-source:24

# apl-source:25
def اقصر_مكتملة(لوحة, كلمات):
  # apl-source:26
  حروف_اللوحة = عد_الحروف(لوحة)
  # apl-source:27
  افضل = ""
  # apl-source:28
  for كلمة in كلمات:
    # apl-source:29
    عدّ_الكلمة = عد_الحروف(كلمة)
    # apl-source:30
    تكفي = True
    # apl-source:31
    for ح in حروف_اللوحة:
      # apl-source:32
      if عدّ_الكلمة.get(ح, 0) < حروف_اللوحة[ح]:
        # apl-source:33
        تكفي = False
    # apl-source:34
    if تكفي:
      # apl-source:35
      if (افضل == "") or (len(كلمة) < len(افضل)):
        # apl-source:36
        افضل = كلمة
  # apl-source:37
  return افضل
# apl-source:38

# apl-source:39
تأكد_يساوي(اقصر_مكتملة("1s3 PSt", ["step","steps","stripe","stepple"]), "steps", "steps")
# apl-source:40
تأكد_يساوي(اقصر_مكتملة("1s3 456", ["looks","pest","stew","show"]), "pest", "pest")
# apl-source:41
تأكد_يساوي(اقصر_مكتملة("a", ["b","ca"]), "ca", "ca")
# apl-source:42
