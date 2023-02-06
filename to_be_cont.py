from typing import Tuple, Optional, Dict

class State:
   unauthorized = 1
   authorized = 2

class Action:
   login = 1
   logout = 2
   deposit = 3
   withdraw = 4
   balance = 5

def login_checker(action_param: Optional, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]:
    if action_param == atm_password:
        return True, atm_current_balance, None
    else:
        return False, atm_current_balance, None

def logout_checker(action_param: Optional, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]:
    return True, atm_current_balance, None

def deposit_checker(action_param: Optional, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]:
    if action_param:
        return True, atm_current_balance + int(action_param), None
    else:
        return False, atm_current_balance, None

def withdraw_checker(action_param: Optional, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]:
    if action_param and atm_current_balance >= int(action_param):
        return True, atm_current_balance - int(action_param), None
    else:
        return False, atm_current_balance, None

def balance_checker(action_param: Optional, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]:
    return True, atm_current_balance, atm_current_balance

class ATM:
    def __init__(self, init_state: State, init_balance: int, password: str, transition_table: Dict):
        self.state = init_state
        self._balance = init_balance
        self._password = password
        self._transition_table = transition_table

    def next(self, action: Action, param: Optional) -> Tuple[bool, Optional]:
        try:
            for transition_action, check, next_state in self._transition_table[self.state]:
                if action == transition_action:
                    passed, new_balance, res = check(param, self._password, self._balance)
                    if passed:
                        self._balance = new_balance
                        self.state = next_state
                        return True, res
        except KeyError:
            pass
        return False, None

def run_atm():
    password = input().strip()
    init_balance = int(input().strip())
    n = int(input().strip())

    transition_table = {
        State.unauthorized: [
            ('login', login_checker, State.authorized)
        ],
        State.authorized: [
            ('logout', logout_checker, State.unauthorized),
            ('deposit', deposit_checker, State.authorized),
            ('withdraw', withdraw_checker, State.
