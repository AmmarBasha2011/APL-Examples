
# apl-source:1
# مثال 176 — تسجيل الأحداث بمستويات
# apl-source:2
# Logging with levels
# apl-source:3
# Demonstrates: logging، المستويات، التنسيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/176-logging-levels.apl
# apl-source:6

# apl-source:7
import logging
# apl-source:8

# apl-source:9
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
# apl-source:10

# apl-source:11
logging.debug("رسالة تصحيح لن تظهر")
# apl-source:12
logging.info("بدأ البرنامج")
# apl-source:13
logging.warning("تحذير: مساحة قليلة")
# apl-source:14
logging.error("خطأ غير قاتل")
# apl-source:15

# apl-source:16
print("انتهى التسجيل (راجع stderr أعلاه).")
# apl-source:17
