import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DATASETS_PATH = os.path.join(ROOT_PATH, 'datasets')
ASSETS_PATH = os.path.join(ROOT_PATH, 'assets')
TRAIN_PATH = os.path.join(DATASETS_PATH, 'train')
VALIDATION_PATH = os.path.join(DATASETS_PATH, 'validation')
RESULTS_PATH = os.path.join(ROOT_PATH, 'results')

COLOURS = {
    'blue': '#4285F4',
    'green': (0.0, 1.0, 0.44)
}
