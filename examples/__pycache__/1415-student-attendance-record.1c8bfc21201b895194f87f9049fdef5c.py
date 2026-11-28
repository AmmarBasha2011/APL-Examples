
# apl-source:1
# مثال 1415 — سجل حضور الطالب
# apl-source:2
# Student attendance record eligibility
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1415-student-attendance-record.apl
# apl-source:6

# apl-source:7
# أقل من غيابين
# apl-source:8
# ولا ثلاث مرات تأخر متتالية
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
def يستحق(سجل):
  # apl-source:19
  if سجل.count("A") >= 2:
    # apl-source:20
    return False
  # apl-source:21
  if "LLL" in سجل:
    # apl-source:22
    return False
  # apl-source:23
  return True
# apl-source:24

# apl-source:25
تأكد_يساوي(يستحق("PPALLP"), True, "مستحق")
# apl-source:26
تأكد_يساوي(يستحق("PPALLL"), False, "تأخر ثلاثاً")
# apl-source:27
تأكد_يساوي(يستحق("AA"), False, "غائب مرتين")
# apl-source:28
