class AccountNotFoundError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class ForbiddenTransferError(Exception):
    pass