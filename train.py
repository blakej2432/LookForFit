import wandb
wandb.login()

from ultralytics import YOLO
import ultralytics
from wandb.integration.ultralytics import add_wandb_callback

sweep_config = {
    'method': 'random',
    'metric': {'goal': 'maximize', 'name': 'metrics/mAP50(B)'},
    'parameters': {
        'batch_size': {
            'values': [32]
        },
        'learning_rate': {
            'values': [0.0001]
        }
        
    }
}

sweep_id = wandb.sweep(sweep=sweep_config, project='yolov9')

def yolo_train():
    wandb.init(dir='/data/sds/jmc/wandb')
    
    config = wandb.config

    model = YOLO('yolov9c.pt')
    add_wandb_callback(model, enable_model_checkpointing=True)
    results = model.train(data='/data/sds/datasets/gym/data.yaml', name='gym_',
                          plots=True, batch=config.batch_size, epochs=600, imgsz=(640,480), patience=20,
                          cos_lr=True, lrf=0.01, lr0=config.learning_rate)
    
    wandb.finish()


wandb.agent(sweep_id, function=yolo_train, count=10)

print("train All complete")