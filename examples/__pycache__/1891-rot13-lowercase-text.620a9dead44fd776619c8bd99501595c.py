
# apl-source:1
# مثال 1891 — تشفير روت ١٣
# apl-source:2
# ROT13 cipher
# apl-source:3
# Demonstrates: تشفير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1891-rot13-lowercase-text.apl
# apl-source:6

# apl-source:7
# الأبجدية ٢٦ حرفا فالإزاحة ١٣ تعكس نفسها
# apl-source:8
# نفس الدالة تشفر وتفك
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
def روت(نص):
  # apl-source:21
  خرج = ""
  # apl-source:22
  for ح in نص:
    # apl-source:23
    ك = الحروف.find(ح)
    # apl-source:24
    if ك < 0:
      # apl-source:25
      خرج = خرج + ح
    # apl-source:26
    else:
      # apl-source:27
      خرج = خرج + الحروف[(ك + 13) % 26]
  # apl-source:28
  return خرج
# apl-source:29

# apl-source:30
تأكد_يساوي(روت("hello"), "uryyb", "تشفير")
# apl-source:31
تأكد_يساوي(روت(روت("world")), "world", "فك")
# apl-source:32
تأكد_يساوي(روت("a-n"), "n-a", "رمز")
# apl-source:33
