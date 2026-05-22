import os
import sys

def fix_android_manifest():
    """Add required permissions to AndroidManifest.xml after build"""
    
    manifest_path = "build/flutter/android/app/src/main/AndroidManifest.xml"
    
    if not os.path.exists(manifest_path):
        print(f"❌ AndroidManifest.xml not found at: {manifest_path}")
        print("⚠️  Run 'flet build apk' first!")
        return False
    
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    permissions = [
        'android.permission.POST_NOTIFICATIONS',
        'android.permission.WAKE_LOCK',
        'android.permission.FOREGROUND_SERVICE',
        'android.permission.RECEIVE_BOOT_COMPLETED'
    ]
    
    if 'POST_NOTIFICATIONS' in content:
        print("✅ Permissions already added!")
        return True
    
    internet_line = '<uses-permission android:name="android.permission.INTERNET" />'
    
    if internet_line not in content:
        print("❌ Could not locate INTERNET permission line")
        return False
    
    new_permissions_lines = [f'    <uses-permission android:name="{perm}" />' for perm in permissions]
    replacement = internet_line + '\n' + '\n'.join(new_permissions_lines)
    content = content.replace(internet_line, replacement)
    
    try:
        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Permissions added successfully!")
        print("\n📱 Added permissions:")
        for perm in permissions:
            print(f"   ✓ {perm}")
        print("\n🎯 Next: Run 'flet build apk' again")
        return True
        
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Fixing AndroidManifest.xml...\n")
    success = fix_android_manifest()
    sys.exit(0 if success else 1)