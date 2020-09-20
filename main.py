import os
import sys
import shutil
import argparse

import numpy as np
import pandas as pd
import tensorflow as tf
import pathResolver as pathRes


class DataLoader :
    def __init__ (self, data) :

        self.data = data

        self.inputs = None
        self.outputs = None
        self.prepare_data()

    
    def prepare_data(self) :
        pass


    def get_batch(self, batch_size = 64, shuffle = True) :
        pass


class Model :
    def __init__(self, local_model_path, local_checkpoint_file) :
        
        self.X = None
        self.Y = None
        self.loss = None
        self.train = None
        self.output = None
        self.local_model_path = local_model_path
        self.local_checkpoint_file = local_checkpoint_file

    def build_graph (self) :
        pass

    def train_graph(self, loader) :
        pass

    def export(self, session) :
        pass



def main() :
    pass


if __name__ == "__main__" :
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", type = str)
    
    main()