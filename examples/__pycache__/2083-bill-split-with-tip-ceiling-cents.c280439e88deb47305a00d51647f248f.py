
# apl-source:1
# مثال 2083 — تقسيم الفاتورة مع البقشيش بالقروش
# apl-source:2
# Bill split with tip
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2083-bill-split-with-tip-ceiling-cents.apl
# apl-source:6

# apl-source:7
# # المبلغ بالقروش لتفادي الكسور
# apl-source:8
# # السقف يضمن تغطية المجموع
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
def نصيب(مبلغ, نسبة, اشخاص):
  # apl-source:19
  كلي = مبلغ + مبلغ * نسبة // 100
  # apl-source:20
  return (كلي + اشخاص - 1) // اشخاص
# apl-source:21

# apl-source:22
تأكد_يساوي(نصيب(10000, 15, 3), 3834, "ثلاثة")
# apl-source:23
تأكد_يساوي(نصيب(10000, 0, 4), 2500, "بلا بقشيش")
# apl-source:24
تأكد_يساوي(نصيب(100, 10, 1), 110, "شخص")
# apl-source:25
