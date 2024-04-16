import dataclasses
from typing import Literal, Sequence


@dataclasses.dataclass(kw_only=True)
class GeoJsonPolygon:
    coordinates: Sequence[Sequence[Sequence[float]]]
    type: Literal["Polygon"] = "Polygon"


@dataclasses.dataclass(kw_only=True)
class GeoJsonPoint:
    coordinates: Sequence[float]
    type: Literal["Point"] = "Point"


point = dataclasses.asdict(GeoJsonPoint(coordinates=[127.027667, 37.498563]))
print(point)  # {'coordinates': [127.027667, 37.498563], 'type': 'Point'}

print(
    dataclasses.asdict(
        GeoJsonPolygon(
            coordinates=[[[0, 0], [0, 2], [2, 2], [2, 0], [0, 0]], [[1, 0], [1.5, 0.5], [1, 1], [0.5, 0.5], [1, 0]]]
        )
    )
)

# {'coordinates': [[[0, 0], [0, 2], [2, 2], [2, 0], [0, 0]], [[1, 0], [1.5, 0.5], [1, 1], [0.5, 0.5], [1, 0]]], 'type': 'Polygon'}
