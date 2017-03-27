"""Setup for if_p_or_q_then_r_xblock XBlock."""

import os
from setuptools import setup

def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                totalPath = os.path.relpath(os.path.join(dirname, fname), pkg)
                data.append(totalPath)

    return {pkg: data}


setup(
    name='if_p_or_q_then_r_xblock-xblock',
    version='0.75',
    description='CTAT Tutor Package',
    packages=[
        'if_p_or_q_then_r_xblock',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'if_p_or_q_then_r_xblock = if_p_or_q_then_r_xblock:IF_P_OR_Q_THEN_R_XBLOCKCLASS',
        ]
    },
    package_data=package_data("if_p_or_q_then_r_xblock", ["static", "public"]),
)
