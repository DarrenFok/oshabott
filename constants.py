import os

# directory paths
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
ENV_PATH = os.path.join(CURR_DIR, 'secrets', '.env')
COGS_PATH = os.path.join(CURR_DIR, 'cogs')