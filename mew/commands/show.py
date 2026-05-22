from mew.registry import Registry
from mew.ui.display import show_envs


registry = Registry()


def run():
    environments = registry.get_all()
    show_envs(environments)