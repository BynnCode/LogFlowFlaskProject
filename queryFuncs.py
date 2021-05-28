import taos

#配置TDengine的全局主机名
hostname = "td1"

def queryFastlog():
    conn = taos.connect(host=hostname, user="root", password="taosdata", config="C:\\TDengine\\cfg")
    c1 = conn.cursor()
    try:
        c1.execute('use suricata')
        c1.execute('select * from suricata.fastlog limit 100')
    except Exception as err:
        conn.close()
        raise (err)
    datalist = c1.fetchall()
    conn.close()
    return datalist

def querySrcip():
    conn = taos.connect(host=hostname, user="root", password="taosdata", config="C:\\TDengine\\cfg")
    c1 = conn.cursor()
    try:
        c1.execute('use suricata')
        c1.execute('select * from suricata.T_YIPGJTJ limit 500')
    except Exception as err:
        conn.close()
        raise (err)
    datalist = c1.fetchall()

    conn.close
    return datalist

def queryDstip():
    conn = taos.connect(host=hostname, user="root", password="taosdata", config="C:\\TDengine\\cfg")
    c1 = conn.cursor()
    try:
        c1.execute('use suricata')
        c1.execute('select * from suricata.T_MDIPGJTJ limit 1000')
    except Exception as err:
        conn.close()
        raise (err)
    datalist = c1.fetchall()

    conn.close
    return datalist

def queryType():
    conn = taos.connect(host=hostname, user="root", password="taosdata", config="C:\\TDengine\\cfg")
    c1 = conn.cursor()
    try:
        c1.execute('use suricata')
        c1.execute('select * from t_gjlxtj')
    except Exception as err:
        conn.close()
        raise (err)

    TypeNum = c1.fetchall()[0]

    conn.close()
    return TypeNum

def queryFlowTrend():
    conn = taos.connect(host=hostname, user="root", password="taosdata", config="C:\\TDengine\\cfg")
    c1 = conn.cursor()
    try:
        c1.execute('use suricata')
        c1.execute('select * from T_GJLLQS limit 100')
    except Exception as err:
        conn.close()
        raise (err)

    dataTemp = c1.fetchall()
    datalists = []
    for data in dataTemp:
        datalists.append(list(data))
    for data in datalists:
        dt = data[0]
        data[0] = str(dt)
    conn.close()
    return datalists

def queryFlow():
    conn = taos.connect(host=hostname, user="root", password="taosdata", config="C:\\TDengine\\cfg")
    c1 = conn.cursor()
    try:
        c1.execute('use suricata')
        c1.execute('select * from T_ZCYCLLTJ')
    except Exception as err:
        conn.close()
        raise (err)

    data = c1.fetchall()[0]

    conn.close()
    return data
