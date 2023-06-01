import sys

sys.path.append("/home/ubuntu/code/mediapipe-0.8.10.1/build/lib.linux-x86_64-cpython-38")
sys.path.append("/home/ubuntu/code/mediapipe-0.8.10.1")


from mediapipe.python.solutions import pose as mp_pose




def main():
    try:
        pose_tracker = mp_pose.Pose()
    except Exception as e:
        print("Pose error---------: ",e)
        return
    print("success")


if __name__ =='__main__':
    main()