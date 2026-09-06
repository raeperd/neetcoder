class TimeMap:
    def __init__(self):
        raise NotImplementedError("Implement TimeMap.__init__")

    def set(self, key: str, value: str, timestamp: int) -> None:
        raise NotImplementedError("Implement TimeMap.set")

    def get(self, key: str, timestamp: int) -> str:
        raise NotImplementedError("Implement TimeMap.get")
