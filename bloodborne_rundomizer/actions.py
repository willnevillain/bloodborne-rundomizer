import argparse

class ToolAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values > 12:
            values = 12
        setattr(namespace, self.dest, values)
