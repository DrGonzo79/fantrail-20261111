from fastapi.testclient import TestClient
from api.main import app

client=TestClient(app)
def test_health_and_fixture():
    assert client.get("/health").json()["status"]=="ok"
    data=client.get("/demo").json();assert data["fictional"] is True;assert len(data["stops"])==6
def test_trail_plans_real_domain_operation():
    response=client.post("/trail",json={"stopIds":["lantern-yard","orbit-lab","creator-court"],"startHour":10})
    assert response.status_code==200
    body=response.json();assert body["checkins"]==3;assert body["totalMinutes"]>100;assert body["reward"]=="Explorer badge"
def test_invalid_trail_and_unknown_stop():
    assert client.post("/trail",json={"stopIds":["lantern-yard"],"startHour":10}).status_code==422
    assert client.post("/trail",json={"stopIds":["lantern-yard","missing"],"startHour":10}).status_code==404
def test_checkin_valid_and_invalid():
    assert client.post("/checkin",json={"stopId":"lantern-yard","code":"glow"}).json()["valid"] is True
    assert client.post("/checkin",json={"stopId":"lantern-yard","code":"nope"}).json()["valid"] is False
