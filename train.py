"""YOLOv12 training."""

import argparse
from ultralytics.cfg import get_cfg
from ultralytics.models.yolo.detect import DetectionTrainer


def main():
    """Parse config file and start training process."""
    parser = argparse.ArgumentParser(description='YOLOv12 training')
    parser.add_argument(
        '--config',
        default='config.yaml',
        type=str,
        help='Path to configuration file'
    )
    args = parser.parse_args()
    
    config_args = get_cfg(args.config)
    trainer = DetectionTrainer(overrides=config_args)
    trainer.train()


if __name__ == '__main__':
    main()
