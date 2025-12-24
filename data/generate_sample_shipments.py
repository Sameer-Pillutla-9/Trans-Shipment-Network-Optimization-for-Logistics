import random
from datetime import datetime, timedelta
from pathlib import Path

HUBS = ["ATL", "MEM", "IND", "DFW", "LAX", "EWR"]
SERVICE_TYPES = ["EXPRESS", "ECONOMY"]


def main(num_shipments: int = 600) -> None:
    start = datetime(2024, 1, 1)
    lines = ["shipment_id,origin_hub,destination_hub,ship_date,weight_kg,service_type,actual_transit_days"]

    for sid in range(1, num_shipments + 1):
        origin = random.choice(HUBS)
        dest = random.choice([h for h in HUBS if h != origin])
        ship_date = (start + timedelta(days=random.randint(0, 59))).strftime("%Y-%m-%d")
        weight = round(random.uniform(1.0, 50.0), 2)
        service_type = random.choice(SERVICE_TYPES)
        base = 1 if service_type == "EXPRESS" else 3
        noise = random.choice([0, 0, 1, 2])
        transit = base + noise
        lines.append(
            f"{sid},{origin},{dest},{ship_date},{weight},{service_type},{transit}"
        )

    Path("data").mkdir(exist_ok=True)
    out = Path("data/shipments.csv")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out} ({num_shipments} rows)")


if __name__ == "__main__":
    main()
