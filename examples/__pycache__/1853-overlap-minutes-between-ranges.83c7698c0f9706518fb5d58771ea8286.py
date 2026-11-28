
# apl-source:1
# مثال 1853 — دقائق التداخل بين فترتين
# apl-source:2
# Overlap minutes between two ranges
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1853-overlap-minutes-between-ranges.apl
# apl-source:6

# apl-source:7
# أكبر البدايتين وأصغر النهايتين
# apl-source:8
# السالب يعني لا تداخل
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
def تداخل(أ, ب):
  # apl-source:19
  بداية = max(أ[0], ب[0])
  # apl-source:20
  نهاية = min(أ[1], ب[1])
  # apl-source:21
  if نهاية > بداية:
    # apl-source:22
    return نهاية - بداية
  # apl-source:23
  return 0
# apl-source:24

# apl-source:25
تأكد_يساوي(تداخل([60, 120], [90, 150]), 30, "تداخل")
# apl-source:26
تأكد_يساوي(تداخل([0, 10], [20, 30]), 0, "منفصلتان")
# apl-source:27
تأكد_يساوي(تداخل([0, 100], [10, 20]), 10, "داخل")
# apl-source:28
