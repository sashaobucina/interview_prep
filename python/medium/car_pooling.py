from typing import List


def car_pooling(trips: List[List[int]], capacity: int) -> bool:
    """
    # 1094: You are driving a vehicle that has capacity empty seats initially available for passengers.

    The vehicle only drives east (ie. it cannot turn around and drive west.)

    Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information
    about the i-th trip: the number of passengers that must be picked up, and the locations to pick them
    up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's
    initial location.

    Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.
    """
    if not trips:
        return True

    start_trips = sorted(trips, key=lambda x: x[1])
    end_trips = sorted(trips, key=lambda x: x[2])

    end_idx = 0
    for i in range(len(start_trips)):
        start_pass, start, _ = start_trips[i]
        end_pass, _, end = end_trips[end_idx]

        while end <= start:
            end_idx += 1
            capacity += end_pass
            end_pass, _, end = end_trips[end_idx]
        capacity -= start_pass

        if capacity < 0:
            return False

    return True


if __name__ == "__main__":
    trips = [[2, 1, 5], [3, 3, 7]]
    assert not car_pooling(trips, 4)
    assert car_pooling(trips, 5)

    trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
    assert car_pooling(trips, 11)

    print("Passed all tests!")
