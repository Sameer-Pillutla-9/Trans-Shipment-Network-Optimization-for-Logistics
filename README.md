# Trans-Shipment & Network Optimization for Logistics

This project models hub-to-hub transit times and identifies underperforming lanes
in a parcel network (similar to FedEx).

Components:

- `data/generate_sample_shipments.py` – creates synthetic shipment data
- `src/train_eta_model.py` – trains a RandomForest ETA model
- `src/report_lanes.py` – lane-level performance report

## Quick start

```bash
pip install -r requirements.txt
python data/generate_sample_shipments.py
python -m src.train_eta_model
python -m src.report_lanes
