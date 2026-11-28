
# apl-source:1
# مثال 931 — ترميز ساوندكس
# apl-source:2
# Soundex
# apl-source:3
# Demonstrates: فئات نطق مرقمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/931-soundex.apl
# apl-source:6

# apl-source:7
# ترميز ساوندكس: تمثيل صوتي للأسماء الإنجليزية
# apl-source:8
# حرف أول + ثلاثة أرقام من فئات النطق
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
def حرف_كبير(حرف):
  # apl-source:19
  رمز = ord(حرف)
  # apl-source:20
  if رمز >= 97 and رمز <= 122:
    # apl-source:21
    return chr(رمز - 32)
  # apl-source:22
  return حرف
# apl-source:23

# apl-source:24
def رقم_حرف(حرف0):
  # apl-source:25
  حرف = حرف_كبير(حرف0)
  # apl-source:26
  if حرف == "B" or حرف == "F" or حرف == "P" or حرف == "V":
    # apl-source:27
    return 1
  # apl-source:28
  if حرف == "C" or حرف == "G" or حرف == "J" or حرف == "K" or حرف == "Q" or حرف == "S" or حرف == "X" or حرف == "Z":
    # apl-source:29
    return 2
  # apl-source:30
  if حرف == "D" or حرف == "T":
    # apl-source:31
    return 3
  # apl-source:32
  if حرف == "L":
    # apl-source:33
    return 4
  # apl-source:34
  if حرف == "M" or حرف == "N":
    # apl-source:35
    return 5
  # apl-source:36
  if حرف == "R":
    # apl-source:37
    return 6
  # apl-source:38
  return 0
# apl-source:39

# apl-source:40
def ساوندكس(اسم):
  # apl-source:41
  أول = اسم[0]
  # apl-source:42
  خرج = أول
  # apl-source:43
  سابق = رقم_حرف(أول)
  # apl-source:44
  for i in range(1, len(اسم)):
    # apl-source:45
    رقم = رقم_حرف(اسم[i])
    # apl-source:46
    if (رقم != 0) and (رقم != سابق):
      # apl-source:47
      خرج = خرج + str(رقم)
    # apl-source:48
    if رقم != 0:
      # apl-source:49
      سابق = رقم
  # apl-source:50
  # اقتطع لثلاثة أرقام واملأ بالأصفار
  # apl-source:51
  while len(خرج) < 4:
    # apl-source:52
    خرج = خرج + "0"
  # apl-source:53
  if len(خرج) > 4:
    # apl-source:54
    خرج = خرج[:4]
  # apl-source:55
  return خرج
# apl-source:56

# apl-source:57
print("Robert:", ساوندكس("Robert"))
# apl-source:58
print("Rupert:", ساوندكس("Rupert"))
# apl-source:59
print("Ashcraft:", ساوندكس("Ashcraft"))
# apl-source:60

# apl-source:61
تأكد_يساوي(ساوندكس("Robert"), "R163", "روبرت")
# apl-source:62
تأكد_يساوي(ساوندكس("Rupert"), "R163", "روبرت مثل روبرت")
# apl-source:63
تأكد_يساوي(ساوندكس("Ashcraft"), "A261", "آشكرافت")
# apl-source:64
تأكد_يساوي(ساوندكس("Lee"), "L000", "حشوة أصفار")
# apl-source:65
