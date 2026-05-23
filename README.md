# Flet Local Notifications

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![Flet Version](https://img.shields.io/badge/flet-0.28.3-green.svg)](https://flet.dev)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A comprehensive Flet extension that demonstrates how to manage and send notifications across multiple platforms. This project provides a simple yet powerful interface for requesting notification permissions and sending them using native APIs, with cross-platform support for Android, Windows, and Linux devices.

## 🙏 Credits

Special thanks to **[@ITAkademi](https://www.youtube.com/@ITAkademi)** for the inspiration and guidance.

## 🌐 Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| Android  | ✅ Fully Supported | Native API integration |
| iOS      | ⏳ Planned | Cannot test currently |
| Windows  | ✅ Fully Supported | Desktop notifications |
| macOS    | ✅ Fully Supported | Desktop notifications |
| Linux    | ✅ Fully Supported | Desktop notifications |

## ✨ Features

- **🔐 Permission Management**: Check and request notification permissions seamlessly
- **📱 Notification Sending**: Send custom notifications with title and text
- **🤖 Android Integration**: Uses native Android NotificationManager via JNI
- **🖥️ Desktop Support**: Cross-platform desktop notifications
- **⏰ Scheduled Notifications**: Plan notifications for future delivery
- **🎨 User-Friendly Interface**: Simple and intuitive GUI built with Flet framework
- **🔧 Advanced Configuration**: Extensive customization options

## 📋 Requirements

- **Python 3.9+** - Modern Python features support
- **Flet framework** - Cross-platform UI framework
- **Android device or emulator** - For mobile testing
- **Required permissions** - Configured in `pyproject.toml` or in `AndroidManifest.xml`

## 🚀 Installation

<!-- ```bash
git clone https://github.com/MasterA5/flet-local-notifications.git
cd flet-local-notifications
pip install -e .
``` -->

### pip CLI
```bash
pip install flet-local-notifications
```

### uv CLI
```bash
uv add flet-local-notifications
```

## 💻 Usage

```python
from flet_local_notifications import (
    AndroidNotificationConfig, 
    DesktopNotificationConfig,
    FletLocalNotification,
)
from flet import *

def main(page:Page):

    noti = FletLocalNotification(page, lambda e: page.open(SnackBar(Text("Permission Acepted"))))

    async def send(e):
        await noti.send(
            AndroidNotificationConfig(
                title="Hello World",
                message="Hello"
            ),
            DesktopNotificationConfig(
                title="Hello World",
                message="Hello",
                app_name="Flet-Test",
            )
        )

    page.add(
        Button(
            text="Send", 
            on_click=lambda e: page.run_task(send, e) # <- use page.run_task() for run async functions if your main entry point is not async
        )
    )

app(target=main)

```

## ⚙️ Configuration

### Pyproject.toml Setup

```toml
[tool.flet]

# Permissions For The App
permissions = [
  "notification",
  "access_notification_policy", 
  "post_notifications",
  "wake_lock",
  "foreground_service"
]

[tool.flet.android.permissions]
"android.permission.ACCESS_NOTIFICATION" = true
"android.permission.POST_NOTIFICATIONS" = true
"android.permission.WAKE_LOCK" = true
"android.permission.FOREGROUND_SERVICE" = true
"android.permission.INTERNET" = true
"android.permission.RECEIVE_BOOT_COMPLETED" = true
```

### ⚠️ Important Notice

For Android SDK > 35, you must manually add permissions to `AndroidManifest.xml` in your build project or use the custom build template.

### Example 1: Manual Permission Addition

Add this line to your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
```

### Example 2: Custom Build Template

**Toml Configuration:**
```toml
[tool.flet.template]
url = "gh:MasterA5/flet-build-template"
ref = "0.28.3"
```

**Terminal Command:**
```bash
flet build apk --template "gh:MasterA5/flet-build-template" --template-ref "0.28.3"
```

---

### Example 3: Automatically patch AndroidManifest.xml after build (recommended)

If you are using Android SDK > 35 and prefer not to manually edit the manifest or rely on a custom build template, you can use the provided helper script.

### 💻 Terminal
```bash
flet build apk
python scripts/fix_manifest.py
```

## 🎯 Application Interface

The application provides comprehensive functionality:

1. **🔍 Check Notification Permission**: Verifies if the app has notification permissions
2. **📋 Request Notification Permission**: Requests notification permissions from the user
3. **📤 Send Notification**: Sends test notifications (enabled when permissions are granted)
4. **⏰ Schedule Notifications**: Plan notifications for specific times
5. **🎨 Customize Notifications**: Advanced styling and configuration options

## 🔧 Key Components

### FletLocalNotification Class

The main class that handles cross-platform notification functionality:

- **Platform Detection**: Automatically detects Android vs Desktop environments
- **Permission Handling**: Manages notification permissions across platforms
- **Unified API**: Single interface for multiple platforms
- **Async Support**: Full asynchronous implementation

### AndroidNotification Class

Located in `flet_local_notifications/android/AndroidNotification.py`:

- **Native Integration**: Uses Android NotificationManager via JNI
- **Channel Management**: Creates and manages notification channels
- **Advanced Features**: Progress bars, buttons, images, and more
- **Permission Requests**: Handles Android runtime permissions

### DesktopNotification Class

Located in `flet_local_notifications/desktop/DesktopNotification.py`:

- **Cross-Platform**: Windows, macOS, and Linux support
- **Native Notifications**: Uses system notification services
- **Interactive Elements**: Buttons, reply fields, and callbacks
- **Custom Styling**: Icons, sounds, and attachments

## 📦 Dependencies

### Core Dependencies
- **`flet==0.28.3`**: Main UI framework
- **`desktop-notifier`**: Desktop notification management
- **`android-notify==1.60.8.dev0`**: Android notification support

## 🔐 Android Permissions

The app requests the following permissions (configured in `pyproject.toml`):

| Permission | Purpose |
|------------|---------|
| `notification` | Basic notification access |
| `access_notification_policy` | Access to notification policies |
| `post_notifications` | Ability to post notifications |
| `wake_lock` | Keep device awake for notifications |
| `foreground_service` | Run as foreground service |
| `INTERNET` | Network access (if needed, be deafult in a ``flet build`` template) |
| `RECEIVE_BOOT_COMPLETED` | Auto-start on boot |

## 🚀 Quick Start Examples

### 📱 | 💻 Basic Notification

```python
import flet as ft
from flet_local_notifications import FletLocalNotification, AndroidNotificationConfig, DesktopNotificationConfig

async def main(page: ft.Page):
    notifier = FletLocalNotification(page)
    
    android_config = AndroidNotificationConfig(
        title="Hello World!",
        message="This is a test notification"
    )
    
    desktop_config = DesktopNotificationConfig(
        title="Hello World!", 
        message="This is a test notification"
    )
    
    await notifier.send(android_config, desktop_config)

ft.app(target=main)
```

### 📱 | 💻 -> ⏰ Scheduled Notification

```python
from datetime import datetime, timedelta
from flet_local_notifications import (
    FletLocalNotifications, 
    AndroidNotificationConfig, 
    DesktopNotificationConfig, 
    AndroidScheduleNotificationConfig, 
    DesktopScheduleNotificationConfig,
)
import flet as ft
 
def main(page: ft.Page):
    notifier = FletLocalNotification(page)
    
    # ... notification configs ...
    android_schedule_config = AndroidScheduleNotificationConfig(
        android_config=AndroidNotificationConfig(
            title="Schedule Notification",
            message="Schedule Notification In Android Device",
        ),
        notify_time=datetime.now() + timedelta(secconds=5)
    )

    desktop_schedule_config = DesktopScheduleNotificationConfig(
        desktop_config=AndroidNotificationConfig(
            title="Schedule Notification",
            message="Schedule Notification In Android Device",
        ),
        notify_time=datetime.now() + timedelta(secconds=5)
    )
    
    # Send Function
    async def send_schedule(e):
        await notifier.schedule(android_schedule_config, desktop_schedule_config)

    page.add(ft.Button("Send Schedule", on_click=lambda e: page.run_task(send_schedule, e)))

ft.app(target=main)
```

## 🔮 Future Improvements

- [ ] **iOS Support**: Add iOS notification capabilities
- [ ] **Notification Groups**: Implement notification categories
- [ ] **Advanced Actions**: Enhanced notification interactions
- [ ] **Rich Media**: Audio, video, and interactive content
- [ ] **Cloud Sync**: Cross-device notification synchronization
- [ ] **Analytics**: Notification engagement tracking

## 📝 Notes

- **Permission Requirements**: Notification functionality requires proper permissions to be granted by the user
- **Native APIs**: The app uses native platform APIs for reliable notification delivery
- **Platform Differences**: Some features may vary between platforms due to OS limitations
- **Testing**: Always test on target platforms before deployment

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add type hints for new functions
- Include docstrings for public APIs
- Add tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**MasterA5** - *Creator and Maintainer* - [GitHub Profile](https://github.com/MasterA5)

## 🙏 Acknowledgments

- **[@ITAkademi](https://www.youtube.com/@ITAkademi)** - For the inspiration and guidance
- **[Flet](https://flet.dev/)** - The amazing framework that makes this possible
- **[android_notify](https://github.com/Fector101/android_notify)** - Android notification support
- **[desktop-notifier](https://github.com/samschott/desktop-notifier)** - Desktop notification support

## 🆘 Support

If you encounter any issues or have questions:

1. **Check** the [Issues](https://github.com/MasterA5/flet-local-notifications/issues) page
2. **Create** a new issue with detailed information
3. **Include** your platform, Python version, and minimal reproduction code
4. **Provide** screenshots or error messages when applicable

---

**⭐ Star this repository** to stay updated with new features and improvements!

**📢 Share** this project with other Flet developers who might find it useful!
