from __future__ import absolute_import

from datasets.tools import Sequence

if __name__ == '__main__':

    seq = Sequence()

    seq.check_sequences()

    sequence = seq.get_sequence("COCO")['type']

    print(sequence)
