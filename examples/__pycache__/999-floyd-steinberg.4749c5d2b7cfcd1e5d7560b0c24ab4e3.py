
# apl-source:1
# مثال 999 — تنقيط فلويد-ستاينبرغ
# apl-source:2
# Floyd-Steinberg dithering
# apl-source:3
# Demonstrates: توزيع الخطأ على الجيران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/999-floyd-steinberg.apl
# apl-source:6

# apl-source:7
# تنقيط فلويد-ستاينبرغ: تحويل تدرج رمادي إلى ثنائي بأقل تشوه مرئي
# apl-source:8
# فرق كل بكسل يوزع على جيرانه الأربعة اللاحقين
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
صورة = [[100, 150, 100, 150], [150, 100, 150, 100], [100, 150, 100, 150], [150, 100, 150, 100]]
# apl-source:19
ناتج = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# apl-source:20

# apl-source:21
for صف in range(4):
  # apl-source:22
  for عمود in range(4):
    # apl-source:23
    قديم = صورة[صف][عمود]
    # apl-source:24
    if قديم >= 128:
      # apl-source:25
      جديد = 255
    # apl-source:26
    else:
      # apl-source:27
      جديد = 0
    # apl-source:28
    ناتج[صف][عمود] = جديد
    # apl-source:29
    فرق = قديم - جديد
    # apl-source:30
    if عمود < 3:
      # apl-source:31
      صورة[صف][عمود + 1] = صورة[صف][عمود + 1] + (فرق * 7 / 16)
    # apl-source:32
    if صف < 3:
      # apl-source:33
      if عمود > 0:
        # apl-source:34
        صورة[صف + 1][عمود - 1] = صورة[صف + 1][عمود - 1] + (فرق * 3 / 16)
      # apl-source:35
      صورة[صف + 1][عمود] = صورة[صف + 1][عمود] + (فرق * 5 / 16)
      # apl-source:36
      if عمود < 3:
        # apl-source:37
        صورة[صف + 1][عمود + 1] = صورة[صف + 1][عمود + 1] + (فرق * 1 / 16)
# apl-source:38

# apl-source:39
تأكد_يساوي(ناتج[0][0], 0, "البكسل الأول")
# apl-source:40
تأكد_يساوي(ناتج[0][1], 255, "البكسل الثاني")
# apl-source:41
تأكد_يساوي(ناتج[1][0], 255, "بكسل الصف الثاني")
# apl-source:42
تأكد_يساوي(ناتج[3][3], 0, "البكسل الأخير")
# apl-source:43
مجموع = 0
# apl-source:44
for صف in range(4):
  # apl-source:45
  for عمود in range(4):
    # apl-source:46
    if ناتج[صف][عمود] == 255:
      # apl-source:47
      مجموع = مجموع + 1
# apl-source:48
تأكد_يساوي(مجموع, 8, "نصف البكسلات مضاءة")
# apl-source:49
