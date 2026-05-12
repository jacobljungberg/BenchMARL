#  Copyright (c) Meta Platforms, Inc. and affiliates.
#
#  This source code is licensed under the license found in the
#  LICENSE file in the root directory of this source tree.
#
import argparse
from pathlib import Path

from benchmarl.hydra_config import reload_experiment_from_file

if __name__ == "__main__":
    """
    Usage: ./evaluate.py <path_to_checkpoint>
    The checkpoint file is typically named
    checkpoint_iteration.pt

    Inside info_relay_env_v2.py set pre_determined_actions = True
    on row 70 to load scenario from test set.

    Running this script with experiment.config.render = True will
    save video into the same directory as the chosen checkpoint. 
    If running the last checkpoint, the video is typically named
    eval_video_1500.mp4

    Evaluation output (csv) is saved in working directory.
    
    """
    parser = argparse.ArgumentParser(
        description="Evaluates the experiment from a checkpoint file."
    )
    parser.add_argument(
        "checkpoint_file", type=str, help="The name of the checkpoint file"
    )
    args = parser.parse_args()
    checkpoint_file = str(Path(args.checkpoint_file).resolve())
    experiment = reload_experiment_from_file(checkpoint_file)

    experiment.config.evaluation_episodes = 10000 + 1 # used to evaluate over more episodes than the ones during training.
    experiment.logger.calculate_extra = True
    experiment.config.render = False # Use only if fewer evaluation_episodes are set
    experiment.config.evaluation_deterministic_actions = True # use the slighlty noisy policy for evaluation
    experiment.evaluate()
