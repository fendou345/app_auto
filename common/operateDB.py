# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

import psycopg2
import re

conn = psycopg2.connect(dbname='airhospital', user='his', password='q1w2e3r4', host='192.168.1.136', port='5432')
cur = conn.cursor()

def get_verification_code():
    sql = 'SELECT msg_content FROM public.notify_message ORDER BY create_time DESC;'
    cur.execute(sql)
    data = cur.fetchone()
    if data is None:
        return None
    verifiCode = (re.search('(\d+)', data[0])).group()
    return verifiCode

if __name__=='__main__':
    get_verification_code()