
# apl-source:1
# مثال 1460 — خصم بشرائح الكمية
# apl-source:2
# Tiered quantity discount
# apl-source:3
# Demonstrates: حسابات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1460-tiered-discount.apl
# apl-source:6

# apl-source:7
# كل شريحة لها سعرها
# apl-source:8
# نحسب كل شريحة على حدة
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
def إجمالي_السعر(كمية):
  # apl-source:19
  شرائح = [[10, 5], [20, 4], [1000000, 3]]
  # apl-source:20
  سابق = 0
  # apl-source:21
  مجموع = 0
  # apl-source:22
  for ش in شرائح:
    # apl-source:23
    if كمية > سابق:
      # apl-source:24
      داخل = min(كمية, ش[0]) - سابق
      # apl-source:25
      مجموع = مجموع + داخل * ش[1]
    # apl-source:26
    سابق = ش[0]
  # apl-source:27
  return مجموع
# apl-source:28

# apl-source:29
تأكد_يساوي(إجمالي_السعر(5), 25, "شريحة أولى")
# apl-source:30
تأكد_يساوي(إجمالي_السعر(15), 70, "شريحتان")
# apl-source:31
تأكد_يساوي(إجمالي_السعر(30), 120, "ثلاث شرائح")
# apl-source:32
