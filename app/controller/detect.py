import torch
import cv2
from ultralytics import YOLO

device = device = torch.device('0') if torch.cuda.is_available() else torch.device('cpu')

CLS_EQUIPMENT_MAP = {0: 'Back Extension', 1: 'Chest Fly', 2: 'Chest Press', 3: 'Lat Pulldown', 4: 'Leg Extension', 5: 'Leg Press', 6: 'Shoulder Press'}

detect_model = YOLO('/home/blakej/lookforfit/app/model/best.pt')
# input_image = '/home/blakej/lookforfit/app/model/랫풀다운.jpg'

def detect_equipment(input_image):
    result = detect_model.predict(
        source=input_image,
        conf=0.1,
        iou=0.4,
        device=device
    )
    equip_idx = int(result[0].boxes.cls) if len(result[0].boxes.cls) == 1 else 0
    equipment = CLS_EQUIPMENT_MAP[equip_idx]

    equip_plot = result[0].plot(font_size=5, probs=False, line_width=2,
                   show=True, conf=False)
    
    equip_img = cv2.cvtColor(equip_plot, cv2.COLOR_BGR2RGB)

    return equipment, equip_img

 