import argparse

class ToolAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values > 12:
            values = 12
        setattr(namespace, self.dest, values)

class RuneAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values > 3:
            values = 3
        setattr(namespace, self.dest, values)
