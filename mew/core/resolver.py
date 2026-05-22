from mew.registry import Registry


class Resolver:

    def __init__(self):
        self.registry = Registry()

    def resolve(self, value: str):

        environments = self.registry.get_all()

        value = value.strip()

        exact_id = [
            env for env in environments
            if env.id == value
        ]

        if exact_id:
            return exact_id

        matched_name = [
            env for env in environments
            if env.name.lower() == value.lower()
        ]

        return matched_name