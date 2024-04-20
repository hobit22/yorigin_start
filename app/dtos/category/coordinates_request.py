import dataclasses


@dataclasses.dataclass
class CoordinatesRequest:
    longitude: float
    latitude: float

    # 데이터 클래스가 만들어 진 후 호출됨
    # validation, parsing 등 할 수 있음
    def __post_init__(self) -> None:
        self.longitude = round(self.longitude, 5)
        self.latitude = round(self.latitude, 5)


coordinates_request = CoordinatesRequest(longitude=127.005926, latitude=37.490061)
print(coordinates_request.longitude, coordinates_request.latitude)
