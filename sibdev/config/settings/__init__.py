from split_settings.tools import optional, include

include(
    "components/base.py",
    "components/database.py",
    "components/extra.py",
    optional("environments/local_settings.py"),
)
