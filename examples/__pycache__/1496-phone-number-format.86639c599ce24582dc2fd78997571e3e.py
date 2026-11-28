
# apl-source:1
# مثال 1496 — تنسيق رقم الهاتف
# apl-source:2
# Format a phone number
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1496-phone-number-format.apl
# apl-source:6

# apl-source:7
# نحتفظ بالأرقام فقط
# apl-source:8
# ثم نقسمها ثلاثة وثلاثة وما تبقى
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
def نسّق_الهاتف(نص_):
  # apl-source:19
  أرقام = ""
  # apl-source:20
  for ح in نص_:
    # apl-source:21
    if ح.isdigit():
      # apl-source:22
      أرقام = أرقام + ح
  # apl-source:23
  if len(أرقام) != 10:
    # apl-source:24
    return "غير صالح"
  # apl-source:25
  return أرقام[0:3] + "-" + أرقام[3:6] + "-" + أرقام[6:10]
# apl-source:26

# apl-source:27
تأكد_يساوي(نسّق_الهاتف("(555) 123 4567"), "555-123-4567", "أقواس")
# apl-source:28
تأكد_يساوي(نسّق_الهاتف("5551234567"), "555-123-4567", "متصل")
# apl-source:29
تأكد_يساوي(نسّق_الهاتف("12345"), "غير صالح", "قصير")
# apl-source:30
