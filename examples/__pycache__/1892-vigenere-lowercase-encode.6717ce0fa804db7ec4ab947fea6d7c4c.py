
# apl-source:1
# مثال 1892 — تشفير فيجينير
# apl-source:2
# Vigenere cipher encode
# apl-source:3
# Demonstrates: تشفير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1892-vigenere-lowercase-encode.apl
# apl-source:6

# apl-source:7
# كل حرف من المفتاح يعطي إزاحة
# apl-source:8
# المفتاح يتكرر على طول النص
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
الحروف = "abcdefghijklmnopqrstuvwxyz"
# apl-source:19

# apl-source:20
def فيجينير(نص, مفتاح):
  # apl-source:21
  خرج = ""
  # apl-source:22
  for ك in range(len(نص)):
    # apl-source:23
    أ = الحروف.find(نص[ك])
    # apl-source:24
    ب = الحروف.find(مفتاح[ك % len(مفتاح)])
    # apl-source:25
    خرج = خرج + الحروف[(أ + ب) % 26]
  # apl-source:26
  return خرج
# apl-source:27

# apl-source:28
تأكد_يساوي(فيجينير("attackatdawn", "lemon"), "lxfopvefrnhr", "مثال كلاسيكي")
# apl-source:29
تأكد_يساوي(فيجينير("abc", "a"), "abc", "مفتاح a")
# apl-source:30
تأكد_يساوي(فيجينير("aaa", "bcd"), "bcd", "نص a")
# apl-source:31
