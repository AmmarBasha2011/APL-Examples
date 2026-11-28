
# apl-source:1
# مثال 1937 — تشفير أفين
# apl-source:2
# Affine cipher encode
# apl-source:3
# Demonstrates: تشفير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1937-affine-cipher-lowercase-encode.apl
# apl-source:6

# apl-source:7
# الحرف عند ك يصبح عند (أ×ك+ب) باقي ٢٦
# apl-source:8
# أ يجب أن يكون أوليا مع ٢٦
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
def افين(س, أ, ب):
  # apl-source:19
  الحروف = "abcdefghijklmnopqrstuvwxyz"
  # apl-source:20
  خرج = ""
  # apl-source:21
  for ح in س:
    # apl-source:22
    ك = الحروف.find(ح)
    # apl-source:23
    خرج = خرج + الحروف[(أ * ك + ب) % 26]
  # apl-source:24
  return خرج
# apl-source:25

# apl-source:26
تأكد_يساوي(افين("affine", 5, 8), "ihhwvc", "أ٥ ب٨")
# apl-source:27
تأكد_يساوي(افين("abc", 1, 0), "abc", "هوية")
# apl-source:28
تأكد_يساوي(افين("a", 3, 2), "c", "حرف")
# apl-source:29
