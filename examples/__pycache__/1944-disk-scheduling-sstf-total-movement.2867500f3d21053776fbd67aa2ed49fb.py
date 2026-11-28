
# apl-source:1
# مثال 1944 — جدولة القرص: أقرب طلب أولا
# apl-source:2
# Disk scheduling SSTF head movement
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1944-disk-scheduling-sstf-total-movement.apl
# apl-source:6

# apl-source:7
# # في كل خطوة نختار أقرب أسطوانة غير مخدومة
# apl-source:8
# # ونجمع حركة الرأس الكلية
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
def حركة(طلبات, بداية):
  # apl-source:19
  متبقي = []
  # apl-source:20
  for ط in طلبات:
    # apl-source:21
    متبقي = متبقي + [ط]
  # apl-source:22
  موضع = بداية
  # apl-source:23
  مج = 0
  # apl-source:24
  while len(متبقي) > 0:
    # apl-source:25
    افضل = 0
    # apl-source:26
    for ك in range(len(متبقي)):
      # apl-source:27
      if abs(متبقي[ك] - موضع) < abs(متبقي[افضل] - موضع):
        # apl-source:28
        افضل = ك
    # apl-source:29
    مج = مج + abs(متبقي[افضل] - موضع)
    # apl-source:30
    موضع = متبقي[افضل]
    # apl-source:31
    متبقي.pop(افضل)
  # apl-source:32
  return مج
# apl-source:33

# apl-source:34
تأكد_يساوي(حركة([98, 183, 37, 122, 14, 124, 65, 67], 53), 236, "كلاسيكي")
# apl-source:35
تأكد_يساوي(حركة([], 10), 0, "فارغ")
# apl-source:36
تأكد_يساوي(حركة([5], 10), 5, "طلب واحد")
# apl-source:37
