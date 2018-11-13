from django.apps import AppConfig


class OrderingConfig(AppConfig):
    name = 'fastfoodrq.ordering'

    def ready(self):
        import fastfoodrq.ordering.signals  # noqa
