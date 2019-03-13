#!/usr/bin/env python
# coding: utf-8


class Requester:
    '''
    Какой-то класс, который умеет делать запросы
     к удаленному серверу
    '''
    def get(self, host, port, filename):
        return "Fail"

    def post(self, host, port, filename, data):
        return False


class RemoteFileReader(Requester):
    '''
    Класс для работы с файлами на удаленном сервере
    '''
    def __init__(self, host, port):
        self._host = host
        self._port = port

    def read_file(self, filename):
        return super().get(self._host, self._port, filename)

    def write_file(self, filename, data):
        return super().post(self._host, self._port, filename, data)


class OrdinaryFileWorker(RemoteFileReader):
    '''
    Класс, который работает как с локальными
     так и с удаленными файлами
    '''
    def transfer_to_remote(self, filename):
        with open(filename, "r") as f:
            super().write_file(filename, f.readlines())

    def transfer_to_local(self, filename):
        with open(filename, "w") as f:
            f.write(super().read_file(filename))


class MockOrdinaryFileWorker(OrdinaryFileWorker):
    '''
    Необходимо отнаследовать данный класс так, чтобы
     он вместо запросов на удаленный сервер:
      при transfer_to_remote считывал filename
     из локальной директории ./test_dir и сохранял filename.tmp
     в локальной директории ./tmpf
      при transfer_to_local считывал filename.tmp
     из локальной директории ./test_dir и сохранял в filename
     в локальной директории ./tmpf
      при удалении объекта директория ./tmp должна удаляться
      при создании объекта, директория ./tmp должна создаваться
     если еще не создана
    '''
    def __init__(self):
        raise NotImplementedError
