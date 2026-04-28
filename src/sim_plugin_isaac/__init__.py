"""Isaac driver plugin for sim-cli.

Distributed as an out-of-tree plugin; discovered by sim-cli via the
``sim.drivers`` entry-point group. Bundled skill files (under
``_skills/``) are exposed via the ``sim.skills`` entry-point group, and
lightweight metadata via ``sim.plugins``.
"""
from importlib.resources import files

from .driver import IsaacDriver

skills_dir = files(__name__) / "_skills"

plugin_info = {
    "name": "isaac",
    "summary": "Isaac Sim driver for sim (v1: one-shot subprocess).",
    "homepage": "https://github.com/svd-ai-lab/sim-plugin-isaac",
    "license_class": "oss",
    "solver_name": "Isaac",
}

__all__ = ["IsaacDriver", "skills_dir", "plugin_info"]
