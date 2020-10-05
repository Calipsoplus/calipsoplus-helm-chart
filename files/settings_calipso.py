import os

# define generic quota per user
MAX_RESOURCES_PER_USER = 5
MAX_RAM_PER_USER = "30G"
MAX_CPU_PER_USER = 10
MAX_STORAGE_PER_USER = "80G"

# define limit max experiments per page
PAGE_SIZE_EXPERIMENTS = 7

# define limit max users per page
PAGE_SIZE_USERS = 20

# 0: This would only allow Umbrella authentication. By default, the system does only allow Umbrella authentication.
# 1: This would allow the user to show the form in order to authenticate locally
ALLOW_LOCAL_AUTHENTICATION = 0

# 0: Check the endpoint (BACKEND_UO_IS_AUTHORIZED) if is authorized or not to manage own resources.
# 1: Always be able to create my own resources.
BACKEND_DEFAULT_AUTHORIZATION = 1

# Both volumes should be built dynamically, but root of both of them must be declared as settings variables
# (e.g EXPERIMENTS_DATASETS_ROOT - for the read-only - and EXPERIMENTS_OUTPUT - for the results)--
EXPERIMENTS_DATASETS_ROOT = "/tmp/data"
EXPERIMENTS_OUTPUT = "/tmp/results"

# which indicates whether getting the information from a REST endpoint (1) or the DB (0)
MOCKLOGIN_PORT = os.environ["MOCKLOGIN_PORT"]
DYNAMIC_EXPERIMENTS_DATA_RETRIEVAL = 0
DYNAMIC_EXPERIMENTS_DATA_RETRIEVAL_ENDPOINT = f"http://mock-login:{MOCKLOGIN_PORT}experiments/$USERNAME/"

ENABLE_ICAT_DATA_RETRIEVAL = 0
ICAT_DATA_RETRIEVAL_ENDPOINT = "https://icat.desy.de"
ICAT_PLUGIN = ""
ICAT_USERNAME = "username"
ICAT_PASSWORD = "password"
ICAT_OPENID_CONNECT = 0

# Used to run the container with a user's UID and GID for read/write NFS
# True: Run as the user
# False: (Default) Run as root. (No access to NFS)
ENABLE_NON_ROOT_UID_CONTAINER = False
ENABLE_NON_ROOT_GID_CONTAINER = False

# Add a user's home directory to each container created by them
# This requires the method in apprest/services/user.py to be completed by each facility with a method that returns
# the path to the user's home.
ADD_HOME_DIR_TO_ALL_CONTAINERS = False

API_URL_FOR_UID_AND_GID = os.environ["UID_GID_API_URL"]

# Kubernetes Settings
DEFAULT_KUBE_NAMESPACE = os.environ['DEFAULT_KUBE_NAMESPACE']
OTHER_DIRS_TO_MOUNT = os.environ['OTHER_DIRS_TO_MOUNT']
REMOTE_PODS_MACHINE_IP = os.environ['REMOTE_PODS_MACHINE_IP']
