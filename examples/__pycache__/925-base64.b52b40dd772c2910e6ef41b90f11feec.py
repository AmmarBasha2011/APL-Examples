import base64
# apl-source:1
# مثال 925 — ترميز Base64
# apl-source:2
# Base64 encoding
# apl-source:3
# Demonstrates: ثلاثة بايتات لأربعة أحرف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/925-base64.apl
# apl-source:6

# apl-source:7
# ترميز Base64: تمثيل البايتات بأبجدية 64 حرفاً قابلة للطباعة
# apl-source:8
# كل 3 بايتات تتحول لـ 4 أحرف سداسية البتات
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
أبجدية = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# apl-source:19

# apl-source:20
def رمز64(نص):
  # apl-source:21
  خرج = ""
  # apl-source:22
  بايتات = []
  # apl-source:23
  for i in range(len(نص)):
    # apl-source:24
    بايتات = بايتات + [ord(نص[i])]
  # apl-source:25
  i = 0
  # apl-source:26
  while i < len(بايتات):
    # apl-source:27
    عدد = 0
    # apl-source:28
    for ج in range(3):
      # apl-source:29
      if i + ج < len(بايتات):
        # apl-source:30
        عدد = عدد * 256 + بايتات[i + ج]
      # apl-source:31
      else:
        # apl-source:32
        عدد = عدد * 256
    # apl-source:33
    حروف = ""
    # apl-source:34
    for ج in range(4):
      # apl-source:35
      حروف = حروف + أبجدية[(عدد >> (18 - ج * 6)) & 63]
    # apl-source:36
    # حشوة = للبايتات الناقصة
    # apl-source:37
    ناقص = 3 - (len(بايتات) - i)
    # apl-source:38
    if ناقص > 2:
      # apl-source:39
      ناقص = 2
    # apl-source:40
    if ناقص < 0:
      # apl-source:41
      ناقص = 0
    # apl-source:42
    حروف = حروف[:4 - ناقص]
    # apl-source:43
    for _ in range(ناقص):
      # apl-source:44
      حروف = حروف + "="
    # apl-source:45
    خرج = خرج + حروف
    # apl-source:46
    i = i + 3
  # apl-source:47
  return خرج
# apl-source:48

# apl-source:49
print("APL ->", رمز64("APL"))
# apl-source:50
print("Ma ->", رمز64("Ma"))
# apl-source:51
print("M ->", رمز64("M"))
# apl-source:52

# apl-source:53
تأكد_يساوي(رمز64("APL"), "QVBM", "ثلاثة بايتات كاملة")
# apl-source:54
تأكد_يساوي(رمز64("Ma"), "TWE=", "بايتان وحشوة")
# apl-source:55
تأكد_يساوي(رمز64("M"), "TQ==", "بايت وحشوتان")
# apl-source:56
تأكد_يساوي(رمز64("hello"), "aGVsbG8=", "كلمة أطول")
# apl-source:57

# apl-source:58
# كل حرف ناتج من الأبجدية أو حشوة
# apl-source:59
ناتج = رمز64("Instinct")
# apl-source:60
for i in range(len(ناتج)):
  # apl-source:61
  حرف = ناتج[i]
  # apl-source:62
  موجود = حرف == "="
  # apl-source:63
  for ج in range(64):
    # apl-source:64
    if أبجدية[ج] == حرف:
      # apl-source:65
      موجود = 1 == 1
  # apl-source:66
  if موجود == False:
    # apl-source:67
    print("فشل: حرف غريب", حرف)
    # apl-source:68
    قياسي_نظام_اخرج(1)
# apl-source:69
print("ناجح: كل الأحرف شرعية")
# apl-source:70
