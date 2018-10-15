from datetime import datetime, timedelta

champions = ('human', 'wizard', 'spirit', 'giant', 'vampire')


def calculate_champion_health(champion, date_string_intervals):
    """
    calculate amount of health remained for a champion
    at the end of day

    @param champion - type of the champion (e.g. 'Wizard', 'human')
    @param date_string_intervals - list of date intervals strings
        when a champion passing the gate (e.g. ['XXXX-XX-XX XX:XX'])

    """
    if champion.lower() not in champions:
        raise ValueError(f'{champion} is not a valid champion!')

    dates = sorted([datetime.strptime(date_string, "%Y-%m-%d %H:%M") for date_string in date_string_intervals])
    total_damage = 0
    for i, date in enumerate(dates):
        try:
            date_next = dates[i + 1]
        except IndexError:
            date_next = date

        interval = (date_next - date).total_seconds()
        for hour in range(int(interval // 3600)):
            total_damage += calculate_damage_taken(date + timedelta(hours=hour), champion)

    return champion_health(champion) - total_damage


def calculate_damage_taken(date, champion):
    if holly_day(date) or invincible_champion(champion):
        return 0
    # "Janna" demon of Wind, "Kalista" demon of agony, or "Skarner" the scorpion demon spawned
    if (date.hour == 6 and 0 <= date.minute <= 29) or (8 <= date.hour <= 14 and 30 <= date.minute <= 59) or (
            18 <= date.hour <= 19 and 0 <= date.minute <= 59):
        return 7
    # "Tiamat" goddess of Oceans / "Warwick" God of war / "Rumble" god of lightning spawned
    elif (date.hour == 6 and 30 <= date.minute <= 59) or (date.hour == 8 and 0 <= date.minute <= 29) or (
            date.hour == 17 and 0 <= date.minute <= 59):
        return 18
    # "Mithra" goddess of sun spawned / "Brand" god of fire spawned
    elif (date.hour == 7 and 0 <= date.minute <= 59) or (
            date.hour == 15 and date.minute >= 30 or date.hour == 16 and date.minute <= 59):
        return 25
    # "Ahri" goddess of wisdom spawned / "Luna" The goddess of the moon spawned
    elif (date.hour == 15 and 0 <= date.minute <= 29) or (date.hour == 20 and date.minute <= 59):
        return 13
    else:
        return 0


def holly_day(date):
    return date.weekday() in (1, 3)


def invincible_champion(champion):
    if champion.lower() in ('wizard', 'spirit'):
        return True
    else:
        return False


def champion_health(champion):
    if champion.lower() == 'giant':
        return 150
    if champion.lower() == 'vampire':
        return 110
    else:
        return 100

