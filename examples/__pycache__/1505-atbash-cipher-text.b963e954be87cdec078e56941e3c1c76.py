
# apl-source:1
# مثال 1505 — تشفير أتباش
# apl-source:2
# Atbash cipher
# apl-source:3
# Demonstrates: تشفير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1505-atbash-cipher-text.apl
# apl-source:6

# apl-source:7
# a تصبح z وb تصبح y
# apl-source:8
# نحسب الموضع ثم نعكسه
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
def أتباش(نص_):
  # apl-source:19
  أبجدية = "abcdefghijklmnopqrstuvwxyz"
  # apl-source:20
  ناتج = ""
  # apl-source:21
  for ح in نص_:
    # apl-source:22
    موضع = أبجدية.find(ح)
    # apl-source:23
    if موضع >= 0:
      # apl-source:24
      ناتج = ناتج + أبجدية[25 - موضع]
    # apl-source:25
    else:
      # apl-source:26
      ناتج = ناتج + ح
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(أتباش("abc"), "zyx", "بداية")
# apl-source:30
تأكد_يساوي(أتباش("hello world"), "svool dliow", "جملة")
# apl-source:31
تأكد_يساوي(أتباش(أتباش("apl")), "apl", "عكس نفسه")
# apl-source:32
