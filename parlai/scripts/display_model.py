#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""
Basic example which iterates through the tasks specified and runs the given model on
them.

Examples
--------

.. code-block:: shell

  python examples/display_model.py -t babi:task1k:1 -m "repeat_label"
  python examples/display_model.py -t "#MovieDD-Reddit" -m "ir_baseline" -mp "-lp 0.5" -dt test
"""  # noqa: E501

from parlai.core.params import ParlaiParser
from parlai.core.agents import create_agent
from parlai.core.worlds import create_task

import random, json


def setup_args():
    parser = ParlaiParser(True, True, 'Display model predictions.')
    parser.add_argument('-n', '-ne', '--num-examples', default=10)
    parser.add_argument('--display-ignore-fields', type=str, default='')
    parser.add_argument(
        '--verbose',
        type='bool',
        default=False,
        hidden=True,
        help='Display additional debug info, e.g. the per-token loss breakdown for generative models.',
    )
    # by default we want to display info about the validation set
    parser.set_defaults(datatype='valid')
    return parser


def display_model(opt):
    random.seed(42)

    # Create model and assign it to the specified task
    agent = create_agent(opt)
    world = create_task(opt, agent)
    allPreds = []
    currentConv = []
    # Show some example dialogs.
    with world:
        for _k in range(int(opt['num_examples'])):
            acts = world.parley()
            #print(world.display() + "\n~~")
            model = {}
            res = {}

            if (_k % 100 is 0):
                print(str(_k) + "done")

            convDone = False
            for act in acts:
                if (act['id'] == 'WizardTransformerRanker'):
                    model['text'] = act['text']
                    model['text_candidates'] = act['text_candidates'][:5]

                    res[act['id']] = model

                    currentConv.append(res)
                    if(convDone):
                        allPreds.append(currentConv)
                        currentConv = []
                        convDone = False

                else:
                    res['wizard_of_wikipedia'] = act['text']
                    res['knowledge'] = act['knowledge'].split("\n")[:20]
                    if(act['episode_done']):
                        convDone = True





            if world.epoch_done():
                print("EPOCH DONE")
                break

    with open('/home/naman/Downloads/raw/predictionsRet.json', 'w') as outfile:
        json.dump(allPreds, outfile)

if __name__ == '__main__':
    # Get command line arguments
    parser = setup_args()
    opt = parser.parse_args()
    display_model(opt)
