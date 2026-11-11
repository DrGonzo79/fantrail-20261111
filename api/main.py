from pathlib import Path
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app=FastAPI(title="FanTrail API",version="0.1.0")
DATA=json.loads((Path(__file__).parents[1]/"data"/"demo.json").read_text())
STOPS={s["id"]:s for s in DATA["stops"]}

class TrailRequest(BaseModel):
    stopIds:list[str]=Field(min_length=2,max_length=6)
    startHour:int=Field(ge=9,le=22)

class CheckinRequest(BaseModel):
    stopId:str=Field(min_length=1,max_length=80)
    code:str=Field(min_length=1,max_length=12)

def plan_trail(req:TrailRequest):
    missing=[sid for sid in req.stopIds if sid not in STOPS]
    if missing: raise HTTPException(status_code=404,detail=f"Unknown activation: {missing[0]}")
    chosen=sorted((STOPS[sid] for sid in req.stopIds),key=lambda s:(s["zone"],s["open"]))
    elapsed=0;warnings=[]
    for stop in chosen:
        arrival=req.startHour+elapsed/60
        if arrival<stop["open"]: elapsed+=(stop["open"]-arrival)*60
        if req.startHour+elapsed/60>stop["close"]: warnings.append(f'{stop["name"]} may be closed before arrival.')
        elapsed+=stop["minutes"]+12
    return {"stops":chosen,"totalMinutes":round(elapsed),"checkins":len(chosen),"reward":"Quest finisher patch" if len(chosen)>=4 else "Explorer badge","warnings":warnings}

@app.get("/health")
def health(): return {"status":"ok","rules":"2026-11-11.1"}

@app.get("/demo")
def demo(): return DATA

@app.post("/trail")
def trail(req:TrailRequest): return plan_trail(req)

@app.post("/checkin")
def checkin(req:CheckinRequest):
    stop=STOPS.get(req.stopId)
    if not stop: raise HTTPException(status_code=404,detail="Unknown activation")
    return {"valid":req.code.strip().upper()==stop["code"],"stop":stop["name"],"brand":stop["brand"]}
