import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PATHS = {
    "write_visuals": os.path.join(ROOT_DIR, 'public' , 'charts',),
    "write_heatmap": os.path.join(ROOT_DIR, 'djsite' , 'rental', 'templates','rental',),
    "write_data": os.path.join(ROOT_DIR, 'public' , 'data',)

}

# Make the dirs 
for key, value in PATHS.items():
    os.makedirs(os.path.dirname(value), exist_ok=True)