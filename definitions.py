import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PATHS = {
    "write_visuals": os.path.join(ROOT_DIR, 'public' , 'charts'),
    "write_heatmap": os.path.join(ROOT_DIR, 'djsite' , 'rental', 'templates','rental'),
    "read":""
}