#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        # user_act = {user_id: (added_posts, follows)}
        self.user_actions = {}

        # post_reads = {post_id: set_of_user)
        self.post_reads = {}

        self._added = 0
        self._follows = 1

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id in self.user_actions:
            self.user_actions[user_id][self._added].append(post_id)
        else:
            self.user_actions[user_id] = [post_id], []

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id in self.post_reads:
            self.post_reads[post_id].add(user_id)
        else:
            self.post_reads[post_id] = {user_id}

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id in self.user_actions:
            self.user_actions[follower_user_id][self._follows].append(followee_user_id)
        else:
            self.user_actions[follower_user_id] = [], [followee_user_id]

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        if user_id in self.user_actions:
            recent_posts = []
            list_of_followees = self.user_actions[user_id][self._follows]
            for followee_id in list_of_followees:
                k_post_of_user = self.user_actions[followee_id][self._added]
                recent_posts += k_post_of_user
            return sorted(recent_posts, reverse=True)[:k]
        else:
            return []

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        tmp = sorted(self.post_reads, reverse=True)
        return sorted(tmp, key=lambda rp: len(self.post_reads[rp]), reverse=True)[:k]
