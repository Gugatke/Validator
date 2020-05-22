from validator.rules_src.required import Required


class RequiredIf(Required):
    """
    >>> TrueRequiredIf = RequiredIf('a')
    >>> TrueRequiredIf('abc')
    True

    >>> FalseRequiredIf = RequiredIf('z')
    >>> FalseRequiredIf('abc')
    False
    """

    def __init__(self, requirement):
        Required.__init__(self)
        self.requirement = requirement

    def __call__(self, arg):
        if Required.__call__(self, arg) and self.requirement in arg:
            return True

        self.set_errror_message(f"Required: {self.requirement} not in {arg}")
        return False

    def __from_str__(self):
        pass