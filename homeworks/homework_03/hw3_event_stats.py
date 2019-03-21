#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.activity_cash = {}

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        if user_id in self.activity_cash:
            self.activity_cash[user_id].append(time)
        else:
            self.activity_cash[user_id] = [time]

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        count_of_people = 0
        for user, _time in self.activity_cash.items():
            if _time[0] <= time:
                count_act = len(list(
                    filter(
                        lambda x: time - self.FIVE_MIN < x <= time, _time
                    )
                ))
                if count_act == count:
                    count_of_people += 1
        return count_of_people
