import os
import importlib.util

_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PLUGIN_FOLDER = os.path.join(_CURRENT_DIR, "..", "plugins")

def load_plugins():
    plugin_registry = {}

    for filename in os.listdir(PLUGIN_FOLDER):
        if filename.endswith(".py") and filename != "__init__.py":
            plugin_name = filename[:-3]
            filepath = os.path.join(PLUGIN_FOLDER, filename)

            spec = importlib.util.spec_from_file_location(plugin_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "register"):
                plugin = module.register()
                trigger = plugin["trigger"]
                plugin_registry[trigger] = plugin
    return plugin_registry
