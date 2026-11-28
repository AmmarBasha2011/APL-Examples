
# apl-source:1
# مثال 1975 — تحويل كلمة إلى أرقام لوحة T9
# apl-source:2
# T9 word to digits
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1975-t9-word-to-digit-sequence.apl
# apl-source:6

# apl-source:7
# # نبني جدولا من الحرف إلى الزر
# apl-source:8
# # ثم نحول كل حرف في الكلمة
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
def رقمي(كلمة):
  # apl-source:19
  ازرار = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
  # apl-source:20
  جدول = {}
  # apl-source:21
  for ز in ازرار:
    # apl-source:22
    for ح in ازرار[ز]:
      # apl-source:23
      جدول[ح] = ز
  # apl-source:24
  خرج = ""
  # apl-source:25
  for ح in كلمة:
    # apl-source:26
    خرج = خرج + جدول[ح]
  # apl-source:27
  return خرج
# apl-source:28

# apl-source:29
تأكد_يساوي(رقمي("hello"), "43556", "hello")
# apl-source:30
تأكد_يساوي(رقمي("apl"), "275", "apl")
# apl-source:31
تأكد_يساوي(رقمي("world"), "96753", "world")
# apl-source:32
