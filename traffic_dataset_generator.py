import csv
import random
import numpy as np

# Define the categories and their corresponding points
incidents = {"none": 0, "minor-accident": 1, "major-accident": 2, "partial-roadwork": 1, "full-roadwork": 2, "partial-blockage": 1, "full-blockage": 2}
time = {"early-morning": 1, "morning": 2, "afternoon": 1, "evening": 2, "night": 1}
weather = {"clear": 0, "foggy": 1, "light-rain": 1, "heavy": 2, "snow/storm": 3}
road_infrastructure = {"good": 0, "average": 1, "bad": 2}
types_of_roads = {"freeway": 0, "highways": 1, "arterial": 1, "collector": 2, "local": 2}
traffic_volume = {"0-249": 0, "250-499": 1, "500-749": 2, "750-1000": 3, "1000+": 4}

# Define the severity of traffic based on total points
def get_severity(points):
    if points <= 4:
        return "very-low"
    elif points <= 6:
        return "low"
    elif points <= 9:
        return "medium"
    elif points <= 12:
        return "high"
    else:
        return "very-high"

# Generate the dataset with random noise
with open('traffic_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["roadblock", "time", "weather", "infrastructure", "type", "volume", "severity"])
    for _ in range(1000):
        incident = random.choice(list(incidents.keys()))
        time_of_day = random.choice(list(time.keys()))
        weather_condition = random.choice(list(weather.keys()))
        road_infra = random.choice(list(road_infrastructure.keys()))
        road_type = random.choice(list(types_of_roads.keys()))
        traffic_vol = random.choice(list(traffic_volume.keys()))

        # Calculate total points with random noise
        total_points = incidents[incident] + time[time_of_day] + weather[weather_condition] + road_infrastructure[road_infra] + types_of_roads[road_type] + traffic_volume[traffic_vol] + np.random.normal(0, 1)

        # Determine severity of traffic
        severity = get_severity(total_points)

        # Write the data to the CSV file
        writer.writerow([incident, time_of_day, weather_condition, road_infra, road_type, traffic_vol, severity])
