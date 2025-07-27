import heapq
import math

drivers = {
    "driver1": (12.9, 77.6),
    "driver2": (13.0, 77.5),
    "driver3": (12.8, 77.7),
    "driver4": (13.2, 77.6),
    "driver5": (12.85, 77.65),
}
rider_location = (12.95, 77.58)

def euclidean_distance(coord1, coord2):
    """Calculate squared Euclidean distance between two points."""
    return (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2

def find_n_closest_drivers(rider_location, drivers, N):
    max_heap = [] 
    
    for driver_id, location in drivers.items():
        distance = euclidean_distance(rider_location, location)
        heapq.heappush(max_heap, (-distance, driver_id))
        
        if len(max_heap) > N:
            heapq.heappop(max_heap)  
    
    return [driver_id for _, driver_id in max_heap]

closest_drivers = find_n_closest_drivers(rider_location, drivers, 3)
print("N closest drivers:", closest_drivers)
