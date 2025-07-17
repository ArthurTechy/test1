import streamlit as st
import sys
import pandas as pd
import numpy as np
import sklearn
import joblib

# Check for additional packages
def check_package_version(package_name, import_name=None):
    """Check if a package is available and return its version"""
    try:
        if import_name:
            module = __import__(import_name)
        else:
            module = __import__(package_name)
        
        # Try different ways to get version
        if hasattr(module, '__version__'):
            return module.__version__
        elif hasattr(module, 'VERSION'):
            return module.VERSION
        elif hasattr(module, 'version'):
            return module.version
        else:
            return "Version not found"
    except ImportError:
        return "Not installed"

st.title("Package Version Checker")
st.write("Current package versions in this environment:")

# Core packages
st.write(f"**Python**: {sys.version}")
st.write(f"**Streamlit**: {st.__version__}")
st.write(f"**Pandas**: {pd.__version__}")
st.write(f"**Numpy**: {np.__version__}")
st.write(f"**Scikit-learn**: {sklearn.__version__}")
st.write(f"**Joblib**: {joblib.__version__}")

# Additional packages
packages_to_check = [
    ('dill', 'dill'),
    ('xgboost', 'xgboost'),
    ('catboost', 'catboost'),
    ('matplotlib', 'matplotlib'),
    ('seaborn', 'seaborn'),
    ('plotly', 'plotly')
]

for package_name, import_name in packages_to_check:
    version = check_package_version(package_name, import_name)
    st.write(f"**{package_name.capitalize()}**: {version}")

# Generate requirements.txt content
st.subheader("Generated requirements.txt content:")
requirements = []
requirements.append(f"streamlit=={st.__version__}")
requirements.append(f"pandas=={pd.__version__}")
requirements.append(f"numpy=={np.__version__}")
requirements.append(f"scikit-learn=={sklearn.__version__}")
requirements.append(f"joblib=={joblib.__version__}")

for package_name, import_name in packages_to_check:
    version = check_package_version(package_name, import_name)
    if version != "Not installed" and version != "Version not found":
        requirements.append(f"{package_name}=={version}")

requirements_text = "\n".join(requirements)
st.code(requirements_text, language="text")

# Google Colab installation commands
st.subheader("Google Colab Installation Commands:")
colab_commands = []
for req in requirements:
    colab_commands.append(f"!pip install {req}")

colab_text = "\n".join(colab_commands)
st.code(colab_text, language="bash")
