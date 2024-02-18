#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
import module

if __name__ == "__main__":
    count = int(input("Введите кол-во учащихся: "))
    pprint(module(count))
