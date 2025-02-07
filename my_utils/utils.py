import importlib
import subprocess
import os
import sys
from math import ceil
from arabic_reformer import strip_last_diacritic
from my_utils.package_details import PackageDetails
from paths import ROOT_DIR
try:
    from PySide6.QtCore import QCoreApplication
except ImportError:
    print("Warning: PySide6 not installed")
from my_utils.my_enums import *


def resource_path(relative_path):
    """Get the absolute path to the resource (works for both PyInstaller bundle and during development)."""
    if hasattr(sys, '_MEIPASS'):
        # When bundled by PyInstaller, files are unpacked into a temporary directory
        return os.path.join(sys._MEIPASS, relative_path)
    elif 'COLAB_JUPYTER_IP' in os.environ:
        return f"{ROOT_DIR}/{relative_path}"
    else:
        # When running in development mode (not bundled), just use the relative path
        return relative_path


class DynamicTranslationSrcLang:
    ARABIC = 'Ar'
    ENGLISH = 'En'

def translate_text(text, src_lang: DynamicTranslationSrcLang = DynamicTranslationSrcLang.ARABIC):
    return QCoreApplication.translate(f"{src_lang} Src Dynamic", text)

def load_translation(translator, path):
    return translator.load(resource_path(path))


def equal_words(w1, w2):
    return strip_last_diacritic(w1) == strip_last_diacritic(w2)


def scale(x, old_min, old_max, new_min, new_max, rounding:ScaleRounding=ScaleRounding.NONE):
    new_x = new_min + ((x - old_min) * (new_max - new_min)) / (old_max - old_min)
    match rounding:
        case ScaleRounding.NORMAL:
            new_x = round(new_x)
        case ScaleRounding.CEIL:
            new_x = ceil(new_x)
        case ScaleRounding.FLOOR:
            new_x = int(new_x)
        case _:
            pass
    return new_x

def is_package_installed(package_name: PackageDetails|str):
    try:
        importlib.import_module(package_name if isinstance(package_name, str) else package_name.package_import_name)
        return True
    except (ImportError, ModuleNotFoundError):
        return False

def is_torch_installed_with_gpu():
    is_installed = is_package_installed("torch")
    if is_installed:
        import torch
        return hasattr(torch._C, "_cuda_getDeviceCount")
    return False

def is_cuda_available():
    try:
        subprocess.run(["nvidia-smi"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cuda_available = True
    except FileNotFoundError:
        cuda_available = False
    except subprocess.CalledProcessError:
        cuda_available = False

    return cuda_available

def is_topics_model_available():
    model_name = resource_path('embedding_models/topic_sim_model')
    print(f"{model_name = }")
    return os.path.exists(model_name)

def is_topics_model_zip_available():
    model_name = resource_path('embedding_models/topic_sim_model')
    return os.path.exists(f"{model_name}.zip")