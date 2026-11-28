
# apl-source:1
# مثال 715 — ترميز ساوندكس
# apl-source:2
# Soundex
# apl-source:3
# Demonstrates: تقارب صوتي، دمج، حشو
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/715-soundex-en.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# ترميز ساوندكس للأسماء الإنجليزية
# apl-source:25
# Demonstrates: خريطة حروف لأرقام, دمج المتجاورات المتماثلة, حشو بأصفار
# apl-source:26
# الأسماء المتقاربة صوتيا تتشارك الرمز: Robert و Rupert كلاهما R163
# apl-source:27

# apl-source:28
def رقم_حرف(ح):
  # apl-source:29
  if ح in "BFPV":
    # apl-source:30
    return "1"
  # apl-source:31
  if ح in "CGJKQSXZ":
    # apl-source:32
    return "2"
  # apl-source:33
  if ح in "DT":
    # apl-source:34
    return "3"
  # apl-source:35
  if ح == "L":
    # apl-source:36
    return "4"
  # apl-source:37
  if ح in "MN":
    # apl-source:38
    return "5"
  # apl-source:39
  if ح == "R":
    # apl-source:40
    return "6"
  # apl-source:41
  return ""
# apl-source:42

# apl-source:43
def ساوندكس(خام):
  # apl-source:44
  اسم = خام.upper()
  # apl-source:45
  أول = اسم[0]
  # apl-source:46
  رموز = ""
  # apl-source:47
  سابق = رقم_حرف(أول)
  # apl-source:48
  for ي in range(1, len(اسم)):
    # apl-source:49
    ر = رقم_حرف(اسم[ي])
    # apl-source:50
    if ر != "" and ر != سابق:
      # apl-source:51
      رموز = رموز + ر
    # apl-source:52
    if (اسم[ي] in "HW") == False:
      # apl-source:53
      سابق = ر
  # apl-source:54
  ناتج = أول + رموز
  # apl-source:55
  while len(ناتج) < 4:
    # apl-source:56
    ناتج = ناتج + "0"
  # apl-source:57
  return ناتج[:4]
# apl-source:58

# apl-source:59
تأكد_يساوي(ساوندكس("Robert"), "R163", "روبرت")
# apl-source:60
تأكد_يساوي(ساوندكس("Rupert"), "R163", "روبرت مثل روبرت")
# apl-source:61
تأكد_يساوي(ساوندكس("Rubin"), "R150", "روبين")
# apl-source:62
تأكد_يساوي(ساوندكس("Ashcraft"), "A261", "أشكرافت")
# apl-source:63
تأكد_يساوي(ساوندكس("Lee"), "L000", "لي بلا أرقام")
# apl-source:64
تأكد_يساوي(ساوندكس("Gutierrez"), "G362", "جوتيريز")
# apl-source:65
print(ساوندكس("Robert"), "=", ساوندكس("Rupert"))
# apl-source:66
