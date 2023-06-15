def commands(commands_dict: dict[int, dict]) -> str:
    """Выводит доступные команды в красивом виде.
    :param commands_dict: Словарь команд.
    :return str: Красиво фильтрованный текст
    """
    return '\n'.join(map(
        lambda com_items: f'{com_items[0]}: {com_items[1]["name"]}',
        commands_dict.items()
    ))
