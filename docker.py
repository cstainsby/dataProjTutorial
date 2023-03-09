import os

HOSTNAME = "gcr.io"
PROJECT_ID = "bonion"
TARG_IMG = "full-demo-app"
TAG = "latest-demo"


def build_container():
  CMD = """
    docker build -t {}/{}/{}:{} .
  """.format(HOSTNAME, PROJECT_ID, TARG_IMG, TAG)
  print("RUNNING:", CMD)
  os.system(CMD)

def run_local_container():
  CMD = """
    docker run --publish 8000:8000 {}/{}/{}:{}
  """.format(HOSTNAME, PROJECT_ID, TARG_IMG, TAG)
  print("RUNNING:", CMD)
  os.system(CMD)

def push_container():
  CMD = """
    docker push {}/{}/{}:{}
  """.format(HOSTNAME, PROJECT_ID, TARG_IMG, TAG)
  print("RUNNING:", CMD)
  os.system(CMD)

if __name__=="__main__":
  # build_container()
  # run_local_container()
  push_container()