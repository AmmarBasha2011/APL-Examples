
# apl-source:1
# مثال 967 — إطفاء قرض عقاري
# apl-source:2
# Mortgage amortization
# apl-source:3
# Demonstrates: دفعة ثابتة بمعادلة القيمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/967-mortgage-amortization.apl
# apl-source:6

# apl-source:7
# إطفاء قرض عقاري: الدفعة الشهرية الثابتة بمعادلة القيمة الحالية
# apl-source:8
# ثم جدول يوضح تناقص الفائدة ونمو سداد الأصل
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
def دفعة(أصل, فائدة, أشهر):
  # apl-source:19
  معامل = (1 + فائدة) ** (0 - أشهر)
  # apl-source:20
  return (أصل * فائدة) / (1 - معامل)
# apl-source:21

# apl-source:22
د = دفعة(12000, 0.01, 12)
# apl-source:23
تأكد_يساوي(round(د, 2), 1066.19, "الدفعة الشهرية")
# apl-source:24
تأكد_يساوي(round(د * 12, 2), 12794.23, "إجمالي المدفوع")
# apl-source:25
تأكد_يساوي(round((د * 12) - 12000, 2), 794.23, "إجمالي الفائدة")
# apl-source:26

# apl-source:27
رصيد = 12000
# apl-source:28
فائدة_أول = رصيد * 0.01
# apl-source:29
أصل_أول = د - فائدة_أول
# apl-source:30
رصيد = رصيد - أصل_أول
# apl-source:31
فائدة_ثان = رصيد * 0.01
# apl-source:32
تأكد_يساوي(round(فائدة_أول, 2), 120, "فائدة الشهر الأول")
# apl-source:33
تأكد_يساوي(round(أصل_أول, 2), 946.19, "أصل الشهر الأول")
# apl-source:34
تأكد_يساوي(فائدة_ثان < فائدة_أول, 1 == 1, "الفائدة تتناقص")
# apl-source:35
