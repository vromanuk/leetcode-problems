def min_trucks_needed(
    quantity: list[int], truck_capacity: int, max_parcels: int
) -> int:
    if not quantity or truck_capacity <= 0 or max_parcels <= 0:
        return 0

    quantity.sort(reverse=True)  # Sort to optimize truck space usage
    current_weight = trucks = current_parcels = 0

    for q in quantity:
        while q > 0:
            if current_weight == truck_capacity or current_parcels == max_parcels:
                trucks += 1
                current_weight = 0
                current_parcels = 0

            parcels_to_take = min(
                q, truck_capacity - current_weight, max_parcels - current_parcels
            )

            q -= parcels_to_take
            current_weight += parcels_to_take
            current_parcels += parcels_to_take

    if current_weight > 0 or current_parcels > 0:
        trucks += 1

    return trucks


def main():
    assert min_trucks_needed([4, 4, 3], 3, 3) == 4
    assert min_trucks_needed([2, 4], 3, 2) == 3
    print("All tests passed!")


if __name__ == "__main__":
    main()
