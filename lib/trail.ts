import fixture from "../data/demo.json";
export type Stop={id:string;name:string;brand:string;zone:string;minutes:number;open:number;close:number;featured:boolean;code:string};
export type TrailResult={stops:Stop[];totalMinutes:number;checkins:number;reward:string;warnings:string[]};
export const stops=fixture.stops as Stop[];
export function planTrail(selected:string[],startHour:number):TrailResult{
  if(!Number.isInteger(startHour)||startHour<9||startHour>22)throw new Error("Start time must be between 9:00 and 22:00.");
  if(selected.length<2)throw new Error("Choose at least two activations to build a trail.");
  if(selected.length>6)throw new Error("Keep a demo trail to six stops or fewer.");
  const chosen=selected.map(id=>stops.find(s=>s.id===id)).filter((s):s is Stop=>Boolean(s));
  if(chosen.length!==selected.length)throw new Error("One selected activation is unavailable.");
  const ordered=[...chosen].sort((a,b)=>a.zone.localeCompare(b.zone)||a.open-b.open);
  let elapsed=0;const warnings:string[]=[];
  for(const stop of ordered){const arrival=startHour+elapsed/60;if(arrival<stop.open)elapsed+=(stop.open-arrival)*60;if(startHour+elapsed/60>stop.close)warnings.push(`${stop.name} may be closed before arrival.`);elapsed+=stop.minutes+12;}
  return {stops:ordered,totalMinutes:Math.round(elapsed),checkins:ordered.length,reward:ordered.length>=4?"Quest finisher patch":"Explorer badge",warnings};
}
export function verifyCheckin(stopId:string,code:string){const stop=stops.find(s=>s.id===stopId);if(!stop)throw new Error("Choose an activation.");if(!code.trim())throw new Error("Enter the four-letter demo code.");return {valid:code.trim().toUpperCase()===stop.code,stop:stop.name,brand:stop.brand};}
