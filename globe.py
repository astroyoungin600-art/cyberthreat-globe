import random,datetime
from flask import Flask,jsonify,render_template_string as R
app=Flask(__name__)
C={"d":[],"t":None}
H=[(37,-95,"US"),(51,10,"DE"),(55,37,"RU"),(39,116,"CN"),(55,-3,"GB"),(-14,-51,"BR"),(20,78,"IN"),(-30,22,"ZA"),(35,139,"JP")]
def rw():
 a=H[random.randint(0,len(H)-1)]
 return a[0]+random.uniform(-6,6),a[1]+random.uniform(-10,10),a[2]
def fetch():
 import datetime,random
 if C["d"] and C["t"] and (datetime.datetime.now()-C["t"]).seconds<20:
  return C["d"]
 d=[]
 for i in range(10):
  lat,lon,c=rw()
  d.append({"id":3846100+i,"lat":lat,"lon":lon,"type":"RANSOM","color":"#ff1a1a","family":"LockBit","name":f"Victim {c}","url":f"{random.randint(20,500)}GB","country":c,"sev":99,"srcLat":55,"srcLng":37,"time":datetime.datetime.now().isoformat()})
 for i in range(8):
  lat,lon,c=rw()
  d.append({"id":4102100+i,"lat":lat,"lon":lon,"type":"BREACH","color":"#ffaa00","family":"Breach","name":f"{random.randint(10,200)}k creds","url":"forum","country":c,"sev":88,"srcLat":0,"srcLng":0,"time":datetime.datetime.now().isoformat()})
 for i in range(8):
  lat,lon,c=rw()
  d.append({"id":7000000+i,"lat":lat,"lon":lon,"type":"ODS","color":"#00e5ff","family":"Emotet","name":f"C2 {i}","url":"C2","country":c,"sev":98,"srcLat":52,"srcLng":13,"time":datetime.datetime.now().isoformat()})
 C["d"]=d;C["t"]=datetime.datetime.now();return d

@app.route("/")
def g():
 return R('''<html><head><meta name=viewport content="width=device-width,initial-scale=1"><script src="https://unpkg.com/globe.gl@2.34/dist/globe.gl.min.js"></script><style>body{margin:0;background:#000;overflow:hidden;font-family:monospace}#globe{width:100vw;height:100vh}#top{position:absolute;top:0;left:0;right:0;z-index:500;background:#000;padding:10px;display:flex;align-items:center}#burger{margin-left:auto;width:32px;height:22px;display:flex;flex-direction:column;justify-content:space-between;cursor:pointer}#burger div{height:3px;background:#5ee9c0}#menu{position:absolute;top:44px;right:8px;z-index:600;background:#0a1414;border:1px solid #2a4a4a;border-radius:10px;padding:6px;width:240px;display:none}#menu a{display:block;padding:12px;color:#cbd5e1;text-decoration:none;background:#0f1f1f;margin:3px 0;border-radius:6px}#bottom{position:absolute;bottom:10px;left:50%;transform:translateX(-50%);display:flex;background:#000;border:1px solid #222;border-radius:4px;overflow-x:auto;max-width:95vw}#bottom div{padding:10px;color:#5ee9c0;font-size:11px;white-space:nowrap;cursor:pointer}#bottom div.on{color:#ff3344}#info{position:absolute;top:50px;left:8px;width:280px;background:rgba(5,15,15,0.9);border:1px solid #1f4d4d;border-radius:8px;padding:8px;color:#a5b4fc;font-size:11px}</style></head><body><div id=globe></div><div id=top><b style="color:#fff">WORLDWIDE</b><small id=clock style="color:#555;margin-left:8px"></small><div id=burger onclick="event.stopPropagation();document.getElementById('menu').style.display=document.getElementById('menu').style.display=='block'?'none':'block'"><div></div><div></div><div></div></div></div><div id=menu><a href="/">Globe Worldwide</a><a href="/dashboard">Dashboard Live</a><a href="/investigate/3846100">Investigate 3846100</a><a href="javascript:void(0)" onclick="setT('RANSOM')">RANSOM</a><a href="javascript:void(0)" onclick="setT('ALL')">ALL WORLD</a></div><div id=bottom><div id=t-ALL class=on onclick="setT('ALL')">ALL WORLD</div><div id=t-RANSOM onclick="setT('RANSOM')">RANSOM</div><div id=t-BREACH onclick="setT('BREACH')">BREACH</div><div id=t-ODS onclick="setT('ODS')">ODS</div></div><div id=info><b style="color:#5ee9c0">WORLD INTEL</b><div id=sel style="margin-top:6px">Tap dot -> Investigate<br>Menu top-right fixed, low RAM mode</div></div><script>
let all=[],cur='ALL';
const globe=Globe()(document.getElementById('globe')).globeImageUrl('https://unpkg.com/three-globe@2.34/example/img/earth-dark.jpg').showAtmosphere(true).pointsData([]).pointLat('lat').pointLng('lon').pointColor('color').pointAltitude(0.05).pointRadius(0.6).onPointClick(d=>{document.getElementById('sel').innerHTML=`<b style="color:${d.color}">${d.family} ${d.type}</b><br>${d.name} ${d.country}<br>ID ${d.id}<br><br><a href="/investigate/${d.id}" style="background:#5ee9c0;color:#000;padding:5px 10px;border-radius:10px;text-decoration:none">Investigate ${d.id}</a>`;}).arcsData([]).arcStartLat('srcLat').arcStartLng('srcLng').arcEndLat('lat').arcEndLng('lon').arcColor(d=>d.color).arcStroke(0.5);
globe.pointOfView({lat:20,lng:0,altitude:2.8});globe.controls().autoRotate=true;globe.controls().autoRotateSpeed=0.3;
function setT(t){cur=t;document.querySelectorAll('#bottom div').forEach(e=>e.classList.remove('on'));document.getElementById('t-'+t).classList.add('on');let f=cur=='ALL'?all:all.filter(x=>x.type==cur);globe.pointsData(f);globe.arcsData(f.slice(0,15));}
function load(){fetch('/api/all').then(r=>r.json()).then(d=>{all=d;setT(cur);});}
setInterval(()=>document.getElementById('clock').innerText=new Date().toLocaleTimeString(),1000);
document.getElementById('globe').addEventListener('click',()=>document.getElementById('menu').style.display='none');
load();setInterval(load,25000);
</script></body></html>''')

@app.route("/dashboard")
def d():
 return R('''<html><head><meta name=viewport content="width=device-width,initial-scale=1"><script src="https://cdn.jsdelivr.net/npm/chart.js"></script><style>body{margin:0;background:#020608;color:#a5b4fc;font-family:monospace}.top{background:#000;padding:10px;display:flex;justify-content:space-between;border-bottom:1px solid #222}#burger{width:32px;height:22px;display:flex;flex-direction:column;justify-content:space-between;cursor:pointer}#burger div{height:3px;background:#5ee9c0}#menu{position:absolute;top:44px;right:8px;z-index:600;background:#0a1414;border:1px solid #2a4a4a;border-radius:10px;padding:6px;width:240px;display:none}#menu a{display:block;padding:12px;color:#cbd5e1;text-decoration:none;background:#0f1f1f;margin:3px 0;border-radius:6px}.card{background:#080f14;border:1px solid #1a2a2a;border-radius:10px;padding:10px;margin:8px}.btn{background:#0a1a1a;border:1px solid #1f4d4d;color:#5ee9c0;padding:5px 10px;border-radius:12px;font-size:11px;text-decoration:none}</style></head><body><div class=top><b style="color:#fff">DASHBOARD LIVE - LOW RAM</b><div style="display:flex;gap:10px"><a href="/" style="color:#5ee9c0">Globe</a><div id=burger onclick="event.stopPropagation();document.getElementById('menu').style.display=document.getElementById('menu').style.display=='block'?'none':'block'"><div></div><div></div><div></div></div></div><div id=menu><a href="/">Globe</a><a href="/dashboard">Dashboard</a></div></div><div class=card><b>TOTAL WORLDWIDE</b><div id=total style="font-size:22px;color:#5ee9c0">--</div><canvas id=typeDoughnut height=120></canvas></div><div class=card><b>FEED - TAP INVESTIGATE</b><div id=tbl></div></div><script>
let typeChart;
function init(){typeChart=new Chart(document.getElementById('typeDoughnut'),{type:'doughnut',data:{labels:[],[STRIPPED]
function load(){fetch('/api/all').then(r=>r.json()).then(data=>{document.getElementById('total').innerText=data.length+' WORLD';let types={};data.forEach(d=>types[d.type]=(types[d.type]||0)+1);typeChart.data.labels=Object.keys(types);typeChart.data.datasets[0].data=Object.values(types);typeChart.update();document.getElementById('tbl').innerHTML=data.map(d=>`<div style="padding:6px 0;border-bottom:1px solid #111;display:flex;justify-content:space-between"><span style="color:${d.color}">${d.type} ${d.country}</span><a href="/investigate/${d.id}" class=btn>Investigate ${d.id}</a></div>`).join('');});}
init();load();setInterval(load,5000);
</script></body></html>''')

@app.route("/investigate/<int:tid>")
@app.route("/investigate")
def inv(tid=None):
 return R('''<html><body style="margin:0;background:#020608;color:#fff;font-family:monospace"><div style="padding:10px;background:#000;display:flex;justify-content:space-between"><b>INVESTIGATE ID <span id=idLabel></span></b><div><a href="/" style="color:#5ee9c0">Globe</a> <a href="/dashboard" style="color:#5ee9c0">Dash</a></div></div><div style="padding:12px"><div id=main></div><div id=related style="margin-top:12px"></div></div><script>
let id=location.pathname.split('/').pop();if(id=='investigate')id=3846100;document.getElementById('idLabel').innerText=id;
fetch('/api/all').then(r=>r.json()).then(data=>{let item=data.find(x=>x.id==parseInt(id))||data[0];document.getElementById('main').innerHTML=`<b style="color:${item.color};font-size:18px">${item.family} [${item.type}] ID ${item.id}</b><br><br>Country ${item.country}<br>Name ${item.name}<br>URL ${item.url}<br>SEV ${item.sev}<br>Src ${item.srcLat},${item.srcLng}<br>Dst ${item.lat},${item.lon}<br>Time ${item.time}<br><br><a href="https://www.virustotal.com/gui/search/${item.url}" target=_blank style="color:#5ee9c0">VirusTotal</a>`;document.getElementById('related').innerHTML='<b>RELATED</b><br>'+data.filter(x=>x.country==item.country).slice(0,8).map(x=>`<a href="/investigate/${x.id}" style="color:${x.color}">${x.id} ${x.type} ${x.country}</a>`).join('<br>');});
</script></body></html>''')

@app.route("/api/all")
def api(): return jsonify(fetch())
if __name__=="__main__": app.run(host="0.0.0.0",port=8000,threaded=False)
