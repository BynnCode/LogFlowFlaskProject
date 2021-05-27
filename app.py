from flask import Flask,render_template
import queryFuncs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    return index()

@app.route('/fastlog')
def fastlog():
    datalist= queryFuncs.queryFastlog()
    return render_template("suricata/fastlog.html", datalists = datalist)



@app.route('/srcip')
def srcip():
    datalist = queryFuncs.querySrcip()

    datalistIp = []
    datalistIpCount = []
    for item in range(0, 40):
        datalistIp.append(datalist[item][1])
    for item in range(0, 40):
        datalistIpCount.append(int(datalist[item][2]))
    return render_template("suricata/srcip.html", datalistIps=datalistIp, datalistIpCounts=datalistIpCount)

@app.route('/dstip')
def dstip():
    datalist = queryFuncs.queryDstip()
    datalistIp = []
    datalistIpCount = []
    for item in range(0, 40):
        datalistIp.append(datalist[item][1])
    print(datalistIp)
    for item in range(0, 40):
        datalistIpCount.append(int(datalist[item][2]))
        print(datalistIpCount)
    return render_template("suricata/dstip.html", datalistIps=datalistIp, datalistIpCounts=datalistIpCount)

@app.route('/type')
def type():
    TypeNum = queryFuncs.queryType()
    return render_template("suricata/type.html", TypeNum=TypeNum)

@app.route('/flow')
def flowData():
    flowData = queryFuncs.queryFlow()
    return render_template("suricata/flow.html", flowData=flowData)


@app.route('/attackFlow')
def attackFlow():
    attackFlow = queryFuncs.queryFlowTrend()
    return render_template("suricata/attackFlow.html", attackFlow=attackFlow)

@app.route('/assetvaluation')
def assetvaluation():
    return render_template("asset/assetValuation.html")\

@app.route('/assetview')
def assetview():
    return render_template("asset/assetView.html")

@app.route('/assetbug')
def assetbug():
    return render_template("asset/assetBug.html")

@app.route('/bugsource')
def bugsource():
    return render_template("asset/bugSource.html")

@app.route('/locasset')
def locasset():
    return render_template("asset/locAsset.html")

@app.route('/safetydevice')
def safetydevice():
    return render_template("asset/safetyDevice.html")

@app.route('/softtype')
def softtype():
    return render_template("asset/softType.html")

@app.route('/devicetype')
def devicetype():
    return render_template("asset/deviceType.html")

@app.route('/commentpart')
def commentPart():
    return render_template("logs/commentPart.html")

@app.route('/warnnum')
def warnnum():
    return render_template("logs/warnNum.html")

@app.route('/warnnumip')
def warnnumip():
    return render_template("logs/warnNumIp.html")

@app.route('/warnlog')
def warnlog():
    return render_template("logs/warnLog.html")

if __name__ == '__main__':
    app.run()
