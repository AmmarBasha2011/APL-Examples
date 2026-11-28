
# apl-source:1
# مثال 1566 — حذف حروف العلة
# apl-source:2
# Remove vowels from text
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1566-remove-vowels-text.apl
# apl-source:6

# apl-source:7
# نفحص كل حرف
# apl-source:8
# نتجاهل aeiou بحالتيها
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
def بلا_علة(نص_):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  for ح in نص_:
    # apl-source:21
    if ح.lower() in "aeiou":
      # apl-source:22
      ناتج = ناتج
    # apl-source:23
    else:
      # apl-source:24
      ناتج = ناتج + ح
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(بلا_علة("Hello World"), "Hll Wrld", "جملة")
# apl-source:28
تأكد_يساوي(بلا_علة("AEIOU"), "", "كلها علة")
# apl-source:29
تأكد_يساوي(بلا_علة("xyz"), "xyz", "بدون علة")
# apl-source:30
