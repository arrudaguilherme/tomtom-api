import requests
import pandas as pd
import time

# frc limit = 22

frc_limit = 0

def get_traffic_data(frc:int):
    url = f'https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/{frc}/json?key=z5AIOi9Npn7E79BCfuKthwzBOiNYp8bd&point=52.41072,4.84239'

    response = requests.get(url)

    data = response.json()
    
    try:
        if data:

            latitudes = []
            longitudes = []
            frcs = []
            velocidades = []
            current_speeds = []
            current_travel_times = []
            confidences = []
            read_closures = []


            for info in data['flowSegmentData']['coordinates']['coordinate']:
                frcs.append(data['flowSegmentData']['frc'])
                velocidades.append(data['flowSegmentData']['freeFlowSpeed'])
                current_speeds.append(data['flowSegmentData']['currentSpeed'])
                current_travel_times.append(data['flowSegmentData']['currentTravelTime'])
                confidences.append(data['flowSegmentData']['confidence'])
                read_closures.append(data['flowSegmentData']['roadClosure'])
                latitudes.append(info['latitude'])
                longitudes.append(info['longitude'])
                
            df = pd.DataFrame({
                'latitude': latitudes,  
                'longitude': longitudes,  
                'frc': frcs,  
                'velocidade': velocidades,  
                'current_speed': current_speeds,  
                'current_travel_time': current_travel_times,  
                'confidence': confidences,  
                'read_closure': read_closures  
            })
    
            print(df)
    except:
        print(f'Dado não encontra para o frc {frc}')
    
if __name__ == "__main__":
    while frc_limit <= 22:
        get_traffic_data(frc_limit)
        frc_limit+=1
        time.sleep(5)
        


    

    



