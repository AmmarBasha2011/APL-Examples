
# apl-source:1
# مثال 1985 — حجم الملف بوحدة مقروءة
# apl-source:2
# Human readable file size
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1985-file-size-human-readable-units.apl
# apl-source:6

# apl-source:7
# # الوحدات B وKB وMB وGB
# apl-source:8
# # نقرب إلى منزلة عشرية واحدة
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
def حجم(ب):
  # apl-source:19
  وحدات = ["B", "KB", "MB", "GB"]
  # apl-source:20
  ق = ب
  # apl-source:21
  ك = 0
  # apl-source:22
  while ق >= 1024 and ك < 3:
    # apl-source:23
    ق = ق / 1024
    # apl-source:24
    ك = ك + 1
  # apl-source:25
  if ك == 0:
    # apl-source:26
    return str(ب) + " B"
  # apl-source:27
  return str(round(ق, 1)) + " " + وحدات[ك]
# apl-source:28

# apl-source:29
تأكد_يساوي(حجم(512), "512 B", "بايت")
# apl-source:30
تأكد_يساوي(حجم(1536), "1.5 KB", "كيلو")
# apl-source:31
تأكد_يساوي(حجم(1048576), "1.0 MB", "ميجا")
# apl-source:32
تأكد_يساوي(حجم(5368709120), "5.0 GB", "جيجا")
# apl-source:33
