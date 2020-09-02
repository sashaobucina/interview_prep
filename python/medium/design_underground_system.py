class UndergroundSystem:
    """
    # 1396: Implement the class UndergroundSystem that supports three methods:

    1. checkIn(int id, string stationName, int t)
        - A customer with id card equal to id, gets in the station stationName at time t.
        - A customer can only be checked into one place at a time.

    2. checkOut(int id, string stationName, int t)
        - A customer with id card equal to id, gets out from the station stationName at time t.

    3. getAverageTime(string startStation, string endStation) 
        - Returns the average time to travel between the startStation and the endStation.
        - The average time is computed from all the previous traveling from startStation to endStation that happened directly.
        - Call to getAverageTime is always valid.

    You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets 
    in at time t1 at some station, then it gets out at time t2 with t2 > t1. All events happen in chronological 
    order.
    """

    def __init__(self):
        self.customers = {}
        self.station_times = {}

    def check_in(self, id: int, station_name: str, t: int) -> None:
        self.customers[id] = (station_name, t)

    def check_out(self, id: int, station_name: str, t: int) -> None:
        start_station, start_t = self.customers[id]

        # keep track of total times to station, and how many times used
        path = (start_station, station_name)
        if path not in self.station_times:
            self.station_times[path] = (t - start_t, 1)
        else:
            total_t, count = self.station_times[path]
            total_t += (t - start_t)
            count += 1
            self.station_times[path] = (total_t, count)

        del self.customers[id]

    def get_average_time(self, start_station: str, end_station: str) -> float:
        path = (start_station, end_station)
        total_t, count = self.station_times[path]

        return total_t / count


if __name__ == "__main__":
    ug = UndergroundSystem()
    ug.check_in(10, "Leyton", 3)
    ug.check_out(10, "Paradise", 8)
    ug.get_average_time("Leyton", "Paradise") == 5.00000
    ug.check_in(5, "Leyton", 10)
    ug.check_out(5, "Paradise", 16)
    ug.get_average_time("Leyton", "Paradise") == 5.50000
    ug.check_in(2, "Leyton", 21)
    ug.check_out(2, "Paradise", 30)
    ug.get_average_time("Leyton", "Paradise") == 6.66667

    print("Passed all tests!")
