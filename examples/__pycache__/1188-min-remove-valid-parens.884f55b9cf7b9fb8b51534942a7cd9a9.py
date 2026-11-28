
# apl-source:1
# مثال 1188 — حذف أقل أقواس
# apl-source:2
# Minimum remove to make valid parentheses
# apl-source:3
# Demonstrates: مسحان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1188-min-remove-valid-parens.apl
# apl-source:6

# apl-source:7
# نمسح من اليسار ونحذف الإغلاق الزائد
# apl-source:8
# ثم من اليمين ونحذف الفتح الزائد
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
def نظف(س):
  # apl-source:19
  رصيد = 0
  # apl-source:20
  أ = []
  # apl-source:21
  for ح in س:
    # apl-source:22
    if ح == "(":
      # apl-source:23
      رصيد = رصيد + 1
      # apl-source:24
      أ = أ + [ح]
    # apl-source:25
    elif ح == ")":
      # apl-source:26
      if رصيد > 0:
        # apl-source:27
        رصيد = رصيد - 1
        # apl-source:28
        أ = أ + [ح]
    # apl-source:29
    else:
      # apl-source:30
      أ = أ + [ح]
  # apl-source:31
  ب = []
  # apl-source:32
  رصيد = 0
  # apl-source:33
  for ح in أ[::-1]:
    # apl-source:34
    if ح == ")":
      # apl-source:35
      رصيد = رصيد + 1
      # apl-source:36
      ب = ب + [ح]
    # apl-source:37
    elif ح == "(":
      # apl-source:38
      if رصيد > 0:
        # apl-source:39
        رصيد = رصيد - 1
        # apl-source:40
        ب = ب + [ح]
    # apl-source:41
    else:
      # apl-source:42
      ب = ب + [ح]
  # apl-source:43
  return "".join(ب[::-1])
# apl-source:44

# apl-source:45
تأكد_يساوي(نظف("lee(t(c)o)de)"), "lee(t(c)o)de", "إغلاق زائد")
# apl-source:46
تأكد_يساوي(نظف("a)b(c)d"), "ab(c)d", "في الوسط")
# apl-source:47
تأكد_يساوي(نظف("))(("), "", "كلها زائدة")
# apl-source:48
تأكد_يساوي(نظف("(a(b(c)d)"), "a(b(c)d)", "فتح زائد")
# apl-source:49
