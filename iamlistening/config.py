"""
 IAmListening Config
"""
import os

from dynaconf import Dynaconf

# Define the root path of the project
ROOT = os.path.dirname(__file__)

# Load the default settings file
settings = Dynaconf(
    envvar_prefix="TT",
    root_path=os.path.dirname(ROOT),
    settings_files=[
        os.path.join(ROOT, "default_settings.toml"),
        'talky_settings.toml',
        'settings.toml',
        '.secrets.toml'
    ],
    load_dotenv=True,
    environments=True,
    default_env="default",
)
