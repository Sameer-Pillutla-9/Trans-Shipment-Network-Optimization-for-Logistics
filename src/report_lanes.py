import pandas as pd
from pathlib import Path


def main() -> None:
    df = pd.read_csv(Path("data/shipments.csv"))
    lane = (
        df.groupby(["origin_hub", "destination_hub"], as_index=False)
          .agg(
              avg_transit=("actual_transit_days", "mean"),
              shipments=("shipment_id", "count"),
          )
    )
    lane = lane.sort_values("avg_transit", ascending=False)
    print("Top 10 slowest lanes by avg transit days:")
    print(lane.head(10))


if __name__ == "__main__":
    main()
