
# apl-source:1
# مثال 659 — تحليل الأرقام العربية
# apl-source:2
# Arabic-Indic digit parsing
# apl-source:3
# Demonstrates: أرقام عربية، تحليل، إشارة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/659-arabic-number-parse.apl
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
# تحليل الأرقام العربية المشرقية
# apl-source:25
# Demonstrates: خريطة أرقام ٠١٢٣, رفض غير الصالح, إشارة سالبة
# apl-source:26
# يقرأ ١٢٣٤٥ كما يكتبها مستخدم عربي
# apl-source:27

# apl-source:28
def قيمة_رقم(حرف):
  # apl-source:29
  أرقام = "٠١٢٣٤٥٦٧٨٩"
  # apl-source:30
  for ي in range(len(أرقام)):
    # apl-source:31
    if أرقام[ي] == حرف:
      # apl-source:32
      return ي
  # apl-source:33
  لاتيني = "0123456789"
  # apl-source:34
  for ي in range(len(لاتيني)):
    # apl-source:35
    if لاتيني[ي] == حرف:
      # apl-source:36
      return ي
  # apl-source:37
  return -1
# apl-source:38

# apl-source:39
def حلل_رقم(نص):
  # apl-source:40
  if len(نص) == 0:
    # apl-source:41
    return None
  # apl-source:42
  إشارة = 1
  # apl-source:43
  بداية = 0
  # apl-source:44
  if نص[0] == "-":
    # apl-source:45
    إشارة = -1
    # apl-source:46
    بداية = 1
  # apl-source:47
  if بداية >= len(نص):
    # apl-source:48
    return None
  # apl-source:49
  قيمة = 0
  # apl-source:50
  for ي in range(بداية, len(نص)):
    # apl-source:51
    ق = قيمة_رقم(نص[ي])
    # apl-source:52
    if ق == -1:
      # apl-source:53
      return None
    # apl-source:54
    قيمة = قيمة * 10 + ق
  # apl-source:55
  return إشارة * قيمة
# apl-source:56

# apl-source:57
تأكد_يساوي(حلل_رقم("٤٢"), 42, "رقمان عربيان")
# apl-source:58
تأكد_يساوي(حلل_رقم("١٢٣٤٥"), 12345, "خمسة أرقام")
# apl-source:59
تأكد_يساوي(حلل_رقم("3٤"), 34, "مزيج لاتيني عربي")
# apl-source:60
تأكد_يساوي(حلل_رقم("0"), 0, "صفر")
# apl-source:61
تأكد_يساوي(حلل_رقم("٠"), 0, "صفر عربي")
# apl-source:62
تأكد_يساوي(حلل_رقم("-١٧"), -17, "سالب")
# apl-source:63
تأكد_يساوي(حلل_رقم("أب"), None, "حروف مرفوضة")
# apl-source:64
تأكد_يساوي(حلل_رقم(""), None, "فارغ مرفوض")
# apl-source:65
تأكد_يساوي(حلل_رقم("-"), None, "إشارة وحدها مرفوضة")
# apl-source:66
print("انتهى التحليل")
# apl-source:67
