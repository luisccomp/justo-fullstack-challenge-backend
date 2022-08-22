from importlib import import_module

from flask import Flask


class Settings:
    APPS = []


def configure(app: Flask):
    app.config.from_object(Settings)
    
    for module_path in app.config.get("APPS", []):
        module = import_module(module_path)
        
        if hasattr(module, "init_app"):
            module.init_app(app)
