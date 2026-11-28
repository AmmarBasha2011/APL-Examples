
# apl-source:1
# مثال 2069 — هل المصفوفة متناظرة
# apl-source:2
# Symmetric matrix check
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2069-matrix-symmetric-check-transpose-equal.apl
# apl-source:6

# apl-source:7
# # نقارن كل عنصر بنظيره
# apl-source:8
# # المصفوفة المستطيلة ليست متناظرة
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
def متناظرة(م):
  # apl-source:19
  for ي in range(len(م)):
    # apl-source:20
    if len(م[ي]) != len(م):
      # apl-source:21
      return False
    # apl-source:22
    for ك in range(len(م)):
      # apl-source:23
      if م[ي][ك] != م[ك][ي]:
        # apl-source:24
        return False
  # apl-source:25
  return True
# apl-source:26

# apl-source:27
تأكد_يساوي(متناظرة([[1, 2], [2, 1]]), True, "متناظرة")
# apl-source:28
تأكد_يساوي(متناظرة([[1, 2], [3, 1]]), False, "غير متناظرة")
# apl-source:29
تأكد_يساوي(متناظرة([[1, 2, 3], [4, 5, 6]]), False, "مستطيلة")
# apl-source:30
