# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: GardenLog
class UserProfile:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<UserProfile {self.name}>"


def get_profile(user_id):
    profiles = _load_profiles()
    return profiles.get(user_id)


def add_profile(name, email=None):
    profiles = _load_profiles()
    profiles[-1] = UserProfile(name, email)
    _save_profiles(profiles)
    return profiles[-1]


def _load_profiles():
    import importlib
    spec = importlib.util.spec_from_file_location("profiles", PROFILES_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "profiles", [])


def _save_profiles(profiles):
    import importlib
    spec = importlib.util.spec_from_file_location("profiles", PROFILES_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.profiles = profiles
    spec.loader.exec_module(module)
