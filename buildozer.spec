[app]

# (필수) عنوان التطبيق
title = Captcha Automation Tool

# (필수) اسم حزمة التطبيق، يجب أن يكون فريدًا
package.name = org.example.captchaapp

# (필수) نطاق الحزمة، يُستخدم في أماكن أخرى
package.domain = org.example

# (필수) الملف المصدر الرئيسي لتطبيقك أو المجلد الذي يحتوي على main.py
source.dir = .

# (필수) قائمة بالامتدادات التي سيتم تضمينها في الحزمة (بأحرف صغيرة)
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# (اختياري) قائمة بالامتدادات التي سيتم استبعادها (بأحرف صغيرة)
# source.exclude_exts = spec

# (اختياري) نسخة التطبيق
version = 0.1

# (필수) قائمة بالمتطلبات لتطبيقك، مفصولة بفواصل
# يتضمن python3, kivy, والمكتبات الأخرى المستخدمة
# Pillow يتم استيرادها كـ PIL.Image
# numpy لمعالجة الصور
# requests للطلبات الشبكية
# urllib3 يتم استخدامها لتعطيل تحذيرات SSL، وهي عادةً تابعة لـ requests
requirements = python3,kivy==2.3.0,requests,Pillow,numpy,urllib3

# (اختياري) اتجاه التطبيق (landscape, portrait, all)
orientation = portrait

# (اختياري) مكتبات Python C التي سيتم تضمينها. Cython سيقوم بتجميعها.
# kivy تعتمد على cython ضمناً.
# cython_requirements =

# (اختياري) أيقونة التطبيق
icon.filename = %(source.dir)s/icon.png

# (اختياري) صورة شاشة البداية
# presplash.filename = %(source.dir)s/presplash.png

# (اختياري) شاشة التحميل (لا تستخدم في الأغلب مع Kivy)
# loadscreen.filename = %(source.dir)s/loadingscreen.png

# (اختياري) إذا كان تطبيقك يستخدم خدمات Android
# services = ServiceName:filepath

# (اختياري) إذا كنت تريد تعطيل التدوير التلقائي لشاشة البداية
# presplash.fit_mode = cover

# (اختياري) وضع ملء الشاشة
fullscreen = 0

# (اختياري) خطوط مخصصة ليتم تضمينها. إذا كنت تستخدم خطًا عربيًا خاصًا، أضفه هنا.
# على سبيل المثال، إذا كان لديك NotoSansArabic-Regular.ttf في مجلد assets:
# android.add_fonts = assets/NotoSansArabic-Regular.ttf

[buildozer]

# (اختياري) مستوى الإسهاب في الإخراج (0 = صامت، 1 = عادي، 2 = مفصل)
log_level = 2

# (اختياري) عدد التحذيرات التي ستظهر (0 = لا شيء، 1 = عادي، 2 = الكل)
warn_on_root = 1

# (اختياري) مسار إلى SDK Android. إذا لم يتم تعيينه، سيقوم Buildozer بتنزيله.
# android.sdk_path =

# (اختياري) مسار إلى NDK Android. إذا لم يتم تعيينه، سيقوم Buildozer بتنزيله.
# android.ndk_path =

# -----------------------------------------------------------------------------
# إعدادات Android

# (필수) الحد الأدنى لمستوى API المدعوم من قبل تطبيقك.
# Android 9 (Pie) هو API level 28.
android.minapi = 28

# (필수) مستوى API الذي يستهدفه تطبيقك.
# اعتبارًا من أغسطس 2024، يجب أن تستهدف التطبيقات الجديدة API level 34 على الأقل.
# تحقق من متطلبات Google Play Console الحالية لأحدث قيمة.
android.api = 34

# (اختياري) إصدار Android SDK الذي سيتم استخدامه.
# عادة ما يكون نفس `android.api` أو قيمة قريبة منه.
android.sdk = 34

# (필수) إصدار Android NDK الذي سيتم استخدامه.
# تأكد من توافقه مع إصدار python-for-android.
# NDK 25b أو 26b هي خيارات جيدة حاليًا (مايو 2025).
android.ndk = 26b # أو 25b. قد تحتاج إلى تجربة ما يعمل بشكل أفضل مع التبعيات الخاصة بك.

# (اختياري) بنى المعالجات التي سيتم البناء لها.
# `arm64-v8a` مطلوب لـ 64-bit. `armeabi-v7a` للأجهزة القديمة 32-bit.
android.archs = arm64-v8a, armeabi-v7a

# (필수) الأذونات التي يحتاجها تطبيقك.
# INTERNET مطلوب لـ requests.
# WRITE_EXTERNAL_STORAGE و READ_EXTERNAL_STORAGE قد تكون مطلوبة إذا كنت تكتب إلى مساحة تخزين خارجية بشكل صريح.
# JsonStore في user_data_dir عادة ما يستخدم مساحة تخزين داخلية ولا يتطلب هذه الأذونات.
android.permissions = INTERNET

# (اختياري) قائمة بملفات Java أو المجلدات التي سيتم تضمينها.
# android.add_src =

# (اختياري) قائمة بملفات jar التي سيتم تضمينها.
# android.add_jars =

# (اختياري) قائمة بملفات AAR التي سيتم تضمينها.
# android.add_aars =

# (اختياري) المكتبات التي سيتم تضمينها من python-for-android.
# android.p4a_whitelist =

# (اختياري) أي مكتبات إضافية يتم تضمينها.
# android.p4a_blacklist =

# (اختياري) إذا كنت تريد تضمين ملفات .so مجمعة مسبقًا.
# android.add_libs_arm64_v8a = libs/arm64-v8a/*.so
# android.add_libs_armeabi_v7a = libs/armeabi-v7a/*.so

# (اختياري) وسائط إضافية لـ AndroidManifest.xml.
# android.manifest.meta_data = name=value,name2=value2

# (اختياري) وسائط إضافية لوسم التطبيق في AndroidManifest.xml.
# android.manifest.application_attributes = android:largeHeap="true"

# (اختياري) لتمكين دعم AndroidX (مطلوب لمعظم التطبيقات الحديثة).
android.enable_androidx = True

# (اختياري) لتعطيل نسخ ملفات assets إذا كنت لا تحتاج إليها (نادراً).
# android.copy_libs = 0

# (اختياري) إصدار Gradle المستخدم. Buildozer عادة ما يختار إصدارًا مناسبًا.
# android.gradle_version =

# (اختياري) أداة بناء NDK. الافتراضي هو `cmake`. `ndk-build` هو خيار آخر.
# android.ndk_build_tool = cmake

# (اختياري) لتحديد إصدار Java JDK.
# تأكد من تثبيت JDK متوافق (عادة JDK 11 أو 17 لإصدارات Gradle الحديثة).
# buildozer.java_home = /usr/lib/jvm/java-17-openjdk-amd64 (مثال لينكس)
# إذا لم يتم تعيينه، سيحاول Buildozer العثور على JDK مناسب.

# (اختياري) إذا كنت بحاجة إلى تمرير خيارات إضافية إلى python-for-android
# p4a.local_recipes = ./recipes
# p4a.hook =

# (اختياري) اسم ملف keystore لتوقيع الإصدار (release builds).
# android.release_keystore = /path/to/your.keystore
# android.release_keystore_alias = your_alias
# (سيطلب كلمة المرور عند البناء)

# (اختياري) اسم حزمة Android App Bundle.
# android.aab_path = %(source.dir)s/bin/%(app.name)s-%(app.version)s-%(android.arch)s-release.aab

# -----------------------------------------------------------------------------
# إعدادات iOS (غير مستخدمة في هذا المثال)

# -----------------------------------------------------------------------------
# إعدادات خاصة بـ Buildozer

# (اختياري) مسار لتخزين تنزيلات buildozer (SDK, NDK, إلخ).
# buildozer_dir = ./.buildozer

# (اختياري) مسار لتخزين dlcache لـ python-for-android.
# p4a.cache_dir = ./.p4a_cache
