from aiogram.fsm.state import StatesGroup, State


class StaffStates(StatesGroup):
    INSERT_NAME = State()
    INSERT_POST = State()
    LOAD_DOCUMENT = State()
    UNLOAD_DOCUMENT = State()

class GeneralStates(StatesGroup):
    GET_HELP = State()